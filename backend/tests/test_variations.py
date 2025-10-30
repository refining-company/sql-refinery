"""
Variations Testing

Tests variations feature by replaying LSP sessions and capturing workspace snapshots.
"""

import dataclasses
from contextlib import contextmanager
from pathlib import Path

import attr
import pytest

import src
import src._recorder
import src.server

TEST_DIR = Path(__file__).parent
SESSIONS_DIR = TEST_DIR / "sessions"
SNAPSHOTS_DIR = TEST_DIR / "snapshots"


def simplify(obj, terminal=()) -> dict | list | tuple | str | int | float | bool | None:
    """Simplify complex objects for snapshot comparison"""
    # Check terminal first for dataclasses, LSP types, and tree-sitter
    if isinstance(obj, terminal):
        match obj:
            case _ if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
                return repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            case src.sql.Tree() | src.sql.Node():
                return f"{src.sql.to_repr(obj)} = {src.sql.to_str(obj)}"
            case Path():
                return src.utils.trunk_path(str(obj))
            case _:
                return str(obj)

    match obj:
        # Dataclasses
        case _ if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
            obj_key = repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            obj_dict = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
            return {obj_key: simplify(obj_dict, terminal)}

        # LSP types (attrs-based, convert to dict and recurse)
        case _ if attr.has(type(obj)):
            return simplify(attr.asdict(obj, recurse=False), terminal)

        # Tree-sitter objects
        case src.sql.Tree():
            return [simplify(obj.root_node, terminal)]

        case src.sql.Node():
            return src.sql.to_struct(obj)

        # Built-in nested types
        case dict():
            return {simplify(k, (type(k))): simplify(v, terminal) for k, v in sorted(obj.items(), key=str)}
        case list() | set() | frozenset():
            items = [simplify(item, terminal) for item in obj]
            return sorted([item for item in items if item != []], key=str)
        case tuple():
            return tuple(simplify(item, terminal) for item in obj)
        case Path():
            return simplify(str(obj), terminal)
        case bytes():
            return obj.decode("utf-8")
        case float():
            return round(obj, 2)
        case str():
            return src.utils.trunk_path(obj)
        case int() | bool() | None:
            return obj
        case type():
            return f"<{obj.__name__}>"
        case _:
            return str(obj)


@contextmanager
def patch_workspace(callback):
    """Patch Workspace._rebuild, capture callback return values"""
    captures = []
    original_rebuild = src.workspace.Workspace._rebuild
    src.workspace.Workspace._rebuild = src.utils.patch(original_rebuild, lambda: captures.append(callback()))

    try:
        yield captures
    finally:
        src.workspace.Workspace._rebuild = original_rebuild


def run_session(session_data: list[dict]) -> list:
    """Replay session and return server-client exchange"""
    with src._recorder.mock_client() as (server_client, replay):
        for record in session_data:
            if record["direction"] == "client->server":
                replay(record)

    return server_client


def capture_workspace():
    return {
        "layer_folder": simplify(src.server.workspace.layer_folder),
        "layer_files": simplify(src.server.workspace.layer_files),
        "layer_sql": simplify(src.server.workspace.layer_sql),
        "layer_code": simplify(
            src.server.workspace.layer_code,
            terminal=(src.code.Location, src.code.Range, src.code.Column, src.code.Table, src.code.Expression),
        ),
        "layer_model": simplify(
            src.server.workspace.layer_model,
            terminal=(src.model.Column, src.model.Table, src.model.Expression),
        ),
        "layer_variations": simplify(
            src.server.workspace.layer_variations,
            terminal=(
                src.code.Expression,
                src.model.Column,
                src.model.Expression,
                src.variations.ExpressionVariation,
            ),
        ),
        "_index": simplify(
            src.server.workspace._index,
            terminal=(
                src.code.Location,
                src.code.Range,
                src.code.Column,
                src.code.Table,
                src.code.Expression,
                src.code.Query,
                src.model.Column,
                src.model.Table,
                src.model.Expression,
                src.variations.ExpressionVariation,
                src.variations.ExpressionVariations,
                src.sql.Tree,
                src.sql.Node,
            ),
        ),
        "_map": simplify(
            src.server.workspace._map,
            terminal=(
                src.code.Column,
                src.code.Table,
                src.code.Expression,
                src.model.Column,
                src.model.Table,
                src.model.Expression,
            ),
        ),
    }


def capture_variations():
    return src.server.workspace.layer_variations.copy()


@pytest.mark.parametrize("session_name", [f.stem for f in sorted(SESSIONS_DIR.glob("variations*.ndjson"))])
def test_variations(snapshot, session_name):
    """Test variations with workspace snapshots and markdown output"""

    # Load session data
    session_data = src.utils.load_ndjson(SESSIONS_DIR / f"{session_name}.ndjson")

    # Patch class methods with both callbacks
    with (
        patch_workspace(capture_workspace) as workspace_snapshots,
        patch_workspace(capture_variations) as variations_snapshots,
    ):
        # TODO: make a patcher for run_sessions as well to follow patch_workspace logic
        server_client = run_session(session_data)

    # Setup snapshot directory
    session_dir = SNAPSHOTS_DIR / session_name
    session_dir.mkdir(exist_ok=True)
    snapshot.snapshot_dir = session_dir

    # Write server-client exchange
    server_client_simplified = {f"{i:03d}": simplify(item) for i, item in enumerate(server_client)}
    (session_dir / "server_client.last.json").write_text(src.utils.pformat(server_client_simplified))

    # Write workspace trace
    trace_dir = session_dir / "trace"
    trace_dir.mkdir(exist_ok=True)

    for i, ws_snapshot in enumerate(workspace_snapshots):
        for layer_name, layer_data in ws_snapshot.items():
            filename = f"workspace.{layer_name}.{i + 1}.last.json"
            (trace_dir / filename).write_text(src.utils.pformat(layer_data))

    # TODO: Format variations_snapshots as markdown
    # TODO: Write output.last.md and compare with output.true.md
