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

    match obj:  # TODO: split match obj into nested and non-nested objects (terminal is relevant for nested only)
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
    always = (
        src.sql.Tree,
        src.sql.Node,
        src.code.Range,
        src.code.Location,
        src.code.Column,
        src.code.Table,
        src.code.Expression,
        src.model.Column,
        src.model.Expression,
        src.model.Table,
    )
    return {
        "workspace.layer_folder": src.utils.pformat(simplify(src.server.workspace.layer_folder)),
        "workspace.layer_files": src.utils.pformat(simplify(src.server.workspace.layer_files)),
        "workspace.layer_sql": src.utils.pformat(simplify(src.server.workspace.layer_sql)),
        "workspace.layer_code": src.utils.pformat(
            simplify(
                src.server.workspace.layer_code,
                terminal=always,
            )
        ),
        "workspace.layer_model": src.utils.pformat(
            simplify(
                src.server.workspace.layer_model,
                terminal=always,
            )
        ),
        "workspace.layer_variations": src.utils.pformat(
            simplify(
                src.server.workspace.layer_variations,
                terminal=(*always, src.variations.ExpressionVariation),
            )
        ),
        "workspace._index": src.utils.pformat(
            simplify(
                src.server.workspace._index,
                terminal=(
                    *always,
                    src.code.Query,
                    src.variations.ExpressionVariation,
                    src.variations.ExpressionVariations,
                ),
            )
        ),
        "workspace._map": src.utils.pformat(
            simplify(
                src.server.workspace._map,
                terminal=always,
            )
        ),
    }


def capture_variations():
    """Capture variations as formatted markdown"""
    md = src.utils.Markdown()
    for file_path, file_variations in sorted(src.server.workspace.layer_variations.items(), key=str):
        md.h1(src.utils.trunk_path(str(file_path)))

        for expr_variations in file_variations:
            this = expr_variations.this
            this_sql = src.utils.compact_str(this.sql)
            md.h2(f"Expression at {this.location}: {len(expr_variations.others)} variations")
            md.text(f"`{this_sql}`")

            for i, variation in enumerate(expr_variations.others):
                md.text(
                    f"Variation {i+1}: similarity {variation.similarity:.2f}, "
                    + f"frequency {variation.group.frequency} "
                    + f"({", ".join(map(str, sorted(variation.group.locations, key=str)))})"
                    + "\n"
                    + f"`{src.utils.compact_str(variation.group.sql)}`"
                )

    return {"output": str(md)}


def write_snapshots(snapshots: list[dict[str, str]], target_dir: Path, ext: str) -> dict[str, Path]:
    """Write list of snapshot dicts to {prefix}.{i}.{ext} files"""
    files = {}
    for i, snapshot_dict in enumerate(snapshots):
        for prefix, content in snapshot_dict.items():
            file = target_dir / f"{prefix}.{i}.{ext}"
            file.write_text(content)
            files[f"{prefix}.{i}"] = file
    return files


@pytest.mark.parametrize("session_name", [f.stem for f in sorted(SESSIONS_DIR.glob("variations*.ndjson"))])
def test_variations(snapshot, session_name):
    """Test variations with workspace snapshots and markdown output"""

    # Setup snapshot directory
    session_dir = SNAPSHOTS_DIR / session_name
    trace_dir = session_dir / "trace"
    snapshot.snapshot_dir = session_dir

    # Load session data
    session_data = src.utils.load_ndjson(SESSIONS_DIR / f"{session_name}.ndjson")
    with (
        patch_workspace(capture_workspace) as workspace_snapshots,
        patch_workspace(capture_variations) as variations_snapshots,
    ):
        # TODO: make a patcher for run_sessions as well to follow patch_workspace logic
        server_client = run_session(session_data)

    # Write server-client exchange
    server_client_simplified = {f"{i:03d}": simplify(item) for i, item in enumerate(server_client)}
    (trace_dir / "server_client.last.json").write_text(src.utils.pformat(server_client_simplified))

    # Write workspace trace
    write_snapshots(workspace_snapshots, trace_dir, "last.json")

    # Write .last variations markdown snapshots
    # TODO: do we need all intermediate snapshots?
    variation_files = write_snapshots(variations_snapshots, session_dir, "last.md")

    # Compare .last against .true using assert_match
    for prefix, last_file in variation_files.items():
        snapshot.assert_match(last_file.read_text(), session_dir / f"{prefix}.true.md")
