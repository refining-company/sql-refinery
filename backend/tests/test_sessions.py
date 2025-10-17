"""
Session-Based Testing

Tests complete pipeline (SQL → parse → AST → variations → LSP) by replaying
LSP sessions through direct handler calls (no threads/IO).
"""

import dataclasses
import re
from collections import defaultdict
from contextlib import contextmanager
from functools import wraps
from pathlib import Path

import lsprotocol.types as lsp
import pygls.workspace
import pytest

import tests.utils as utils
from src import code, server, sql, variations

TEST_DIR = Path(__file__).parent
SESSIONS_DIR = TEST_DIR / "sessions"
SNAPSHOTS_DIR = TEST_DIR / "snapshots"


def simplify(obj, terminal=()) -> dict | list | tuple | str | int | float | bool | None:
    """Simplify complex objects for snapshot comparison"""
    # Terminal class handling - stop recursion here
    if isinstance(obj, terminal):
        match obj:
            case sql.Node():
                return simplify(obj.text, terminal)
            case _ if dataclasses.is_dataclass(obj):
                return repr(obj)
            case _:
                return f"<{obj.__class__.__name__}>"

    # Non-terminal class handling - recurse into structure
    match obj:
        # Dataclasses
        case _ if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
            obj_dict = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
            obj_key = repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            return {obj_key: simplify(obj_dict, terminal)}

        # Tree-sitter objects
        case sql.Tree():
            return [simplify(obj.root_node, terminal)]

        case sql.Node():
            node_type = sql.get_type(obj, meta=True, helper=False, original=False)
            children = simplify(obj.children, terminal)
            children = [child for child in children if child]  # type: ignore[union-attr]
            children = sum([child if isinstance(child, list) else [child] for child in children], [])

            if node_type:
                key = "{} ({} at {}:{}) = {}".format(
                    node_type,
                    obj.grammar_name,
                    obj.start_point.row + 1,
                    obj.start_point.column + 1,
                    re.sub(r"\s+", " ", simplify(obj.text, terminal))[:20],  # type: ignore[arg-type]
                )
                return {key: children}
            else:
                return children

        # Built-in types
        case dict():
            return {str(simplify(key, terminal)): simplify(value, terminal) for key, value in obj.items()}
        case list():
            return [simplify(item, terminal) for item in obj]
        case tuple():
            return tuple(simplify(item, terminal) for item in obj)
        case set() | frozenset():
            return tuple(sorted((simplify(item, terminal) for item in obj), key=str))
        case Path():
            return simplify(str(obj), terminal)
        case bytes():
            return obj.decode("utf-8")
        case float():
            return round(obj, 2)
        case str():
            return obj.replace(str(Path.cwd()), ".")
        case int() | bool() | None:
            return obj
        case type():
            return f"<{obj.__name__}>"
        case _:
            return f"<{obj.__class__.__name__}>"


@contextmanager
def patch_pipeline():
    """Patch pipeline functions to capture internal stages"""
    captured = defaultdict(list)

    def capture(target, processor):
        key = f"{target.__module__}.{target.__name__}"

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)
            captured[key].append(processor(result))
            return result

        return wrapper

    # Save originals
    orig_parse = sql.parse
    orig_ingest = code.Tree.ingest_file
    orig_variations = variations.get_variations

    # Patch with capturing wrappers
    sql.parse = capture(sql.parse, lambda r: simplify(r))
    code.Tree.ingest_file = capture(
        code.Tree.ingest_file,
        lambda r: simplify(r, terminal=(sql.Node, sql.Tree, code.Column, code.Table, code.Location, code.Range)),
    )
    variations.get_variations = capture(
        variations.get_variations,
        lambda r: simplify(
            r, terminal=(sql.Node, sql.Tree, code.Tree, code.Query, code.Column, code.Table, code.Location, code.Range)
        ),
    )

    try:
        yield captured
    finally:
        # Restore originals
        sql.parse = orig_parse
        code.Tree.ingest_file = orig_ingest
        variations.get_variations = orig_variations


@contextmanager
def patch_server():
    """Patch server to capture responses and notifications"""
    responses = {}
    notifications = []
    orig_send_notification = server.lspserver.send_notification

    server.workspace = None
    server.workspace_folder = None
    server.lspserver.lsp._workspace = pygls.workspace.Workspace(None)
    server.lspserver.send_notification = lambda met, par: notifications.append({"method": met, "params": par})

    converter = server.lspserver.lsp._converter

    def handle(method, params, req_id):
        response = None
        match method:
            case "initialize":
                response = server.initialize(converter.structure(params, lsp.InitializeParams))
            case "textDocument/didOpen":
                server.did_open(converter.structure(params, lsp.DidOpenTextDocumentParams))

        if response and req_id:
            responses[req_id] = response

    try:
        yield handle, responses, notifications
    finally:
        server.lspserver.send_notification = orig_send_notification


@pytest.mark.parametrize("session_name", [f.stem for f in sorted(SESSIONS_DIR.glob("*.ndjson"))])
def test_session(snapshot, session_name):
    """Test complete pipeline by replaying LSP session"""
    snapshot.snapshot_dir = SNAPSHOTS_DIR
    session_data = utils.load_ndjson(SESSIONS_DIR / f"{session_name}.ndjson")

    with patch_pipeline() as captured_internal, patch_server() as (handle, server_responses, server_notifications):
        for record in session_data:
            if record["direction"] == "client->server":
                msg = record["message"]
                handle(msg.get("method"), msg.get("params", {}), msg.get("id"))

    # Format snapshot
    md = utils.Markdown()
    md.h1(f"Session: {session_name}")

    md.h2("Internal Pipeline")
    for stage_name, values in captured_internal.items():
        for i, value in enumerate(values):
            md.h3(f"{stage_name} (call {i + 1})")
            md.code(value)

    md.h2("Client-Server Exchange")
    for record in session_data:
        if record["direction"] == "client->server":
            msg = record["message"]
            md.h3(f"client->server: {msg.get('method')}")
            md.code(simplify(msg))
            if msg.get("id") in server_responses:
                md.h4("server->client")
                md.code(simplify(server_responses[msg.get("id")]))

    if server_notifications:
        md.h2("Server Notifications")
        for notification in server_notifications:
            md.h3(notification["method"])
            md.code(simplify(notification["params"]))

    output = str(md)

    # Write snapshots
    (SNAPSHOTS_DIR / f"{session_name}.last.md").write_text(output)
    snapshot.assert_match(output, f"{session_name}.true.md")
