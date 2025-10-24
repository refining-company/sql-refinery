"""
Session-Based Testing

Tests complete pipeline (SQL → parse → AST → variations → LSP) by replaying
LSP sessions through direct handler calls (no threads/IO).
"""

import dataclasses
from collections import defaultdict
from contextlib import contextmanager
from functools import wraps
from pathlib import Path

import pytest

import src
import src._recorder

TEST_DIR = Path(__file__).parent
SESSIONS_DIR = TEST_DIR / "sessions"
SNAPSHOTS_DIR = TEST_DIR / "snapshots"


def simplify(obj, terminal=(), terminal_hidden=False) -> dict | list | tuple | str | int | float | bool | None:
    """Simplify complex objects for snapshot comparison

    Args:
        terminal: Classes to stop recursion and show repr() + str()
        terminal_hidden: If True, show str() for "_" fields instead of recursing
    """
    # Terminal class handling - stop recursion here (ignored if terminal_hidden=True)
    if not terminal_hidden and isinstance(obj, terminal):
        match obj:
            case src.sql.Node():
                return simplify(obj.text, terminal, terminal_hidden)
            case _ if dataclasses.is_dataclass(obj):
                return repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            case _:
                return f"<{obj.__class__.__name__}>"

    # Non-terminal class handling - recurse into structure
    match obj:
        # Dataclasses
        case _ if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
            if terminal_hidden:
                # Include "_" fields but show only str() for them
                obj_dict = {}
                for f in dataclasses.fields(obj):
                    value = getattr(obj, f.name)
                    if f.name.startswith("_"):
                        # Show str() representation for "_" fields
                        obj_dict[f.name] = str(value) if "__str__" in type(value).__dict__ else repr(value)
                    else:
                        # Recurse normally for non-"_" fields
                        obj_dict[f.name] = simplify(value, terminal, terminal_hidden)
            else:
                # Normal mode: skip "_" fields entirely
                obj_dict = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
                obj_dict = simplify(obj_dict, terminal, terminal_hidden)

            obj_key = repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            return {obj_key: obj_dict}

        # Tree-sitter objects
        case src.sql.Tree():
            return [simplify(obj.root_node, terminal, terminal_hidden)]
        case src.sql.Node():
            return src.sql.to_struc(obj)

        # Built-in types
        case dict():
            return {
                str(simplify(key, terminal, terminal_hidden)): simplify(value, terminal, terminal_hidden)
                for key, value in obj.items()
            }
        case list() | set() | frozenset():
            return sorted([simplify(item, terminal, terminal_hidden) for item in obj], key=str)
        case tuple():
            return tuple(simplify(item, terminal, terminal_hidden) for item in obj)
        case Path():
            return simplify(str(obj), terminal, terminal_hidden)
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
            return f"<{obj.__class__.__name__}>"


@contextmanager
def patch_pipeline():
    """Patch pipeline functions to capture internal stages"""
    pipeline = defaultdict(list)

    def capture(target, processor):
        key = f"{target.__module__}.{target.__name__}"

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)
            pipeline[key].append(processor(result))
            return result

        return wrapper

    # Save originals
    orig_sql_build = src.sql.build
    orig_code_build = src.code.build
    orig_model_build = src.model.build
    orig_variations_build = src.variations.build

    # Patch with capturing wrappers
    src.sql.build = capture(src.sql.build, lambda r: simplify(r))
    src.code.build = capture(
        src.code.build,
        lambda r: simplify(
            r, terminal=(src.sql.Node, src.sql.Tree, src.code.Column, src.code.Table, src.code.Location, src.code.Range)
        ),
    )
    src.model.build = capture(
        src.model.build,
        lambda r: simplify(r, terminal_hidden=True),
    )
    src.variations.build = capture(
        src.variations.build,
        lambda r: simplify(
            r,
            terminal=(
                src.sql.Node,
                src.sql.Tree,
                src.code.Tree,
                src.code.Query,
                src.code.Expression,
                src.code.Column,
                src.code.Table,
                src.code.Location,
                src.code.Range,
                src.model.Column,
            ),
        ),
    )

    try:
        yield pipeline
    finally:
        # Restore originals
        src.sql.build = orig_sql_build
        src.code.build = orig_code_build
        src.model.build = orig_model_build
        src.variations.build = orig_variations_build


@pytest.mark.parametrize("session_name", [f.stem for f in sorted(SESSIONS_DIR.glob("*.ndjson"))])
def test_session(snapshot, session_name):
    """Test complete pipeline by replaying LSP session"""
    # Set snapshot directory to session-specific folder
    session_dir = SNAPSHOTS_DIR / session_name
    session_dir.mkdir(exist_ok=True)
    snapshot.snapshot_dir = session_dir

    # Replay session
    session_data = src.utils.load_ndjson(SESSIONS_DIR / f"{session_name}.ndjson")
    with patch_pipeline() as pipeline, src._recorder.mock_client() as (exchange, replay):
        for record in session_data:
            if record["direction"] == "client->server":
                replay(record)

    # Write .last snapshots
    for stage_name, values in pipeline.items():
        for i, value in enumerate(values):
            (session_dir / f"{stage_name}.{i + 1}.last.json").write_text(src.utils.pformat(value))

    (session_dir / "exchange.last.json").write_text(src.utils.pformat(simplify(exchange)))

    # Compare .last against .true using assert_match
    for last_file in sorted(session_dir.glob("*.last.json")):
        true_filename = last_file.name.replace(".last.", ".true.")
        snapshot.assert_match(last_file.read_text(), true_filename)
