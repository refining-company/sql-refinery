"""
Session-Based Testing

Tests complete pipeline (SQL → parse → AST → variations → LSP) by replaying
LSP sessions by directly calling LSP handlers (no threads/IO).

Architecture:
- Direct handler calls: Calls server.initialize(), server.did_open(), etc. synchronously
- Patching: Intercepts pipeline functions to capture internal stages
- Snapshot: Saves internal pipeline + LSP protocol in markdown format
"""

import dataclasses
import re
from collections import defaultdict
from collections.abc import Callable
from functools import wraps
from pathlib import Path

import pytest

import tests.utils as utils
from src import code, logger, server, sql, variations

log = logger.get(__name__)


# ============================================================================
# Utility Functions (from test_pipeline.py)
# ============================================================================


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
            children = [child for child in children if child]
            children = sum([child if isinstance(child, list) else [child] for child in children], [])

            if node_type:
                key = "{} ({} at {}:{}) = {}".format(
                    node_type,
                    obj.grammar_name,
                    obj.start_point.row + 1,
                    obj.start_point.column + 1,
                    re.sub(r"\s+", " ", simplify(obj.text, terminal))[:20],
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
            return simplify_paths(obj)
        case bytes():
            return obj.decode("utf-8")
        case float():
            return round(obj, 2)
        case str() | int() | bool() | None:
            return obj
        case type():
            return f"<{obj.__name__}>"
        case _:
            return f"<{obj.__class__.__name__}>"


def get_capturer() -> tuple[Callable, dict[str, list]]:
    """Create function capturer for snapshot testing"""
    captured = defaultdict(list)

    def capture(target, processor) -> tuple[Callable, Callable]:
        key = f"{target.__module__}.{target.__name__}"

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)
            captured[key].append(processor(result))
            return result

        return target, wrapper  # Return original first, wrapper second (for unpacking)

    return capture, captured


def simplify_paths(obj):
    """Replace absolute paths with . for portability"""
    match obj:
        case dict():
            return {k: simplify_paths(v) for k, v in obj.items()}
        case list():
            return [simplify_paths(item) for item in obj]
        case str():
            return obj.replace(str(Path.cwd()), ".")
        case _:
            return obj


# ============================================================================
# Test Functions
# ============================================================================


def get_sessions():
    """Auto-discover session files from tests/sessions/*.ndjson"""
    sessions_dir = Path(__file__).parent / "sessions"
    return [f.stem for f in sorted(sessions_dir.glob("*.ndjson"))]


@pytest.mark.parametrize("session_name", get_sessions())
def test_session(snapshot, session_name):
    """Test complete pipeline by replaying LSP session"""

    # Setup paths
    sessions_dir = Path(__file__).parent / "sessions"
    snapshot_dir = Path(__file__).parent / "snapshots"
    session_path = sessions_dir / f"{session_name}.ndjson"

    # Configure snapshot directory
    snapshot.snapshot_dir = snapshot_dir

    log.info(f"Testing session: {session_name}")

    # Load session
    session_data = utils.load_ndjson(session_path)

    # Patch to capture internal pipeline
    capture, captured_internal = get_capturer()
    _sql_parse, sql.parse = capture(
        sql.parse,
        lambda result: simplify(result),
    )
    _ingest_file, code.Tree.ingest_file = capture(
        code.Tree.ingest_file,
        lambda result: simplify(
            result, terminal=(sql.Node, sql.Tree, code.Column, code.Table, code.Location, code.Range)
        ),
    )
    _get_variations, variations.get_variations = capture(
        variations.get_variations,
        lambda result: simplify(
            result,
            terminal=(sql.Node, sql.Tree, code.Tree, code.Query, code.Column, code.Table, code.Location, code.Range),
        ),
    )

    # Track server responses
    server_responses = []

    try:
        # Reset server global state
        server.workspace = None
        server.workspace_folder = None

        # Create mock LSP workspace for document tracking
        from pygls.workspace import Workspace as LspWorkspace

        server.lspserver.lsp._workspace = LspWorkspace(None)

        # Replay session by calling LSP handlers directly (no threads/IO!)
        import lsprotocol.types as lsp

        # Get cattrs converter for proper param conversion (camelCase -> snake_case)
        converter = server.lspserver.lsp._converter

        for record in session_data:
            direction = record["direction"]
            message = record["message"]

            if direction == "client->server":
                method = message.get("method")
                params = message.get("params", {})
                msg_id = message.get("id")

                log.debug(f"Calling handler: {method}")

                # Call handlers directly - they're just Python functions!
                # Use cattrs to convert JSON params to LSP types
                if method == "initialize":
                    init_params = converter.structure(params, lsp.InitializeParams)
                    result = server.initialize(init_params)
                    if msg_id is not None:
                        server_responses.append({"request_id": msg_id, "method": method, "response": result})

                elif method == "initialized":
                    # Notification, no action needed
                    pass

                elif method == "textDocument/didOpen":
                    did_open_params = converter.structure(params, lsp.DidOpenTextDocumentParams)
                    server.did_open(did_open_params)

                elif method == "textDocument/codeLens":
                    # TODO: codeLens handler doesn't exist in server yet
                    # Skip for now
                    if msg_id is not None:
                        server_responses.append({"request_id": msg_id, "method": method, "response": []})

                elif method == "shutdown":
                    if msg_id is not None:
                        server_responses.append({"request_id": msg_id, "method": method, "response": None})

                elif method == "exit":
                    # Notification, no action needed
                    pass

    finally:
        # Restore functions
        sql.parse = _sql_parse
        code.Tree.ingest_file = _ingest_file
        variations.get_variations = _get_variations

    # Format snapshot
    md_lines = [f"# Session: {session_name}\n"]

    # Section 1: Internal Pipeline
    md_lines.append("## Internal Pipeline\n")
    for stage_name, values in captured_internal.items():
        for i, value in enumerate(values):
            md_lines.append(f"### {stage_name} (call {i+1})\n")
            md_lines.append("```json")
            md_lines.append(utils.pformat(value))
            md_lines.append("```\n")

    # Section 2: LSP Protocol (from session)
    md_lines.append("## LSP Protocol\n")
    for record in session_data:
        direction = record["direction"]
        message = record["message"]
        method = message.get("method", f"response-{message.get('id')}")

        md_lines.append(f"### {direction}: {method}\n")
        md_lines.append("```json")
        md_lines.append(utils.pformat(simplify_paths(message)))
        md_lines.append("```\n")

    # Section 3: Server Responses (captured from test)
    if server_responses:
        md_lines.append("## Server Responses (Captured)\n")
        for resp in server_responses:
            md_lines.append(f"### Response to {resp['method']} (id={resp['request_id']})\n")
            md_lines.append("```json")
            if "response" in resp:
                md_lines.append(utils.pformat(simplify_paths(resp["response"])))
            else:
                md_lines.append(utils.pformat({"error": resp.get("error", "Unknown error")}))
            md_lines.append("```\n")

    output = "\n".join(md_lines)

    # Write snapshots
    (snapshot_dir / f"{session_name}.last.md").write_text(output)
    snapshot.assert_match(output, f"{session_name}.true.md")
