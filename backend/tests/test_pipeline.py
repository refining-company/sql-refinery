"""
Test Pipeline Architecture

This module implements a snapshot-based testing approach for SQL analysis:

1. Test Organization:
   - scenario() - Defines the business logic test cases with clear ownership of its state
   - capture_snapshots() - Non-intrusive harness that intercepts function outputs
   - Snapshots are stored as JSON files capturing the exact structure of important outputs

2. Key Design Principles:
   - Tests own their state management (scenario resets workspace)
   - Function interception through monkey patching isolates what's being tested
   - Complex objects are simplified to comparable structures
   - Separation between snapshot generation and verification
"""

import re
import pytest
from pathlib import Path
from collections import defaultdict
from functools import wraps, partial
import dataclasses

from src import sql
from src import code
from src import logic
from src import server
from src import logger
import tests.utils as utils

log = logger.get(__name__)


def simplify(obj, terminal=()) -> dict | list | tuple | str | int | float | bool | None:
    # If the object is an instance of a terminal class
    if isinstance(obj, terminal):
        if isinstance(obj, sql.Node):
            return simplify(obj.text, terminal)
        if isinstance(obj, (logic.Alternative, code.Tree, code.Query, code.Expression, code.Column, code.Table)):
            return repr(obj)

        return f"<{obj.__class__.__name__}>"

    # Custom expansion logic for custom data structures
    if isinstance(obj, (logic.Alternative, code.Tree, code.Query, code.Expression, code.Column, code.Table)):
        obj_dict = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
        return {f"{repr(obj)} = {str(obj)}": simplify(obj_dict, terminal)}

    # Custom expansion logic for tree-sitter objects
    if isinstance(obj, sql.Tree):
        return [simplify(obj.root_node)]

    if isinstance(obj, sql.Node):
        node_type = sql.get_type(obj, meta=True, helper=False, original=False)

        children = simplify(obj.children, terminal)  # simplify recursively
        children = [child for child in children if child]  # filter out empty values # type: ignore
        children = sum([child if isinstance(child, list) else [child] for child in children], [])  # flatten the list

        if node_type:
            key = "{} ({} at {}:{}) = {}".format(
                node_type,
                obj.grammar_name,
                obj.start_point.row + 1,
                obj.start_point.column + 1,
                re.sub(r"\s+", " ", simplify(obj.text, terminal))[:20],  # type: ignore
            )
            return {key: children}
        else:
            return children

    # Handle built-in types
    if isinstance(obj, dict):
        return {str(simplify(key, terminal)): simplify(value, terminal) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item, terminal) for item in obj]

    if isinstance(obj, tuple):
        return tuple(simplify(item, terminal) for item in obj)

    if isinstance(obj, (set, frozenset)):
        return tuple(sorted((simplify(item, terminal) for item in obj), key=str))

    if isinstance(obj, Path):
        return str(obj)

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    if isinstance(obj, float):
        return round(obj, 2)

    if isinstance(obj, (str, int, bool, type(None))):
        return obj

    if isinstance(obj, type):
        return f"<{obj.__name__}>"

    # Fallback for other types
    return f"<{obj.__class__.__name__}>"


def scenario():
    """Business logic test sequence with full ownership of state management."""
    tests_root_dir = Path(__file__).parent
    inputs_dir = tests_root_dir / "inputs"
    codebase_dir = inputs_dir / "codebase"
    editor_file_path = inputs_dir / "editor.sql"

    log.info("Starting scenario execution...")
    workspace = server.get_workspace(new=True)  # Start with a fresh workspace
    workspace.ingest_folder(codebase_dir)
    workspace.ingest_file(path=editor_file_path, content=editor_file_path.read_text())
    workspace.find_inconsistencies(path=editor_file_path)
    log.info("Scenario execution finished.")


def capture_snapshots() -> dict:
    """Patches target functions, runs the scenario, and captures their outputs."""
    captured = defaultdict(list)

    def _intercept(target: callable, fn: callable) -> callable:  # type: ignore
        """
        Wrapper that intercepts outputs of `target` function and translate into simple text representation
        using `fn` to convert into basic types and `utils.pformat` to convert into compact JSON
        """

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)
            key = f"{target.__module__}.{target.__name__}"
            simplified_result = utils.pformat(fn(result))
            captured[key].append(simplified_result)
            return result

        return wrapper

    _sql_parse = sql.parse
    _ingest_file = code.Tree.ingest_file
    _logic_compare = logic.compare

    try:
        sql.parse = _intercept(sql.parse, fn=simplify)
        code.Tree.ingest_file = _intercept(
            code.Tree.ingest_file,
            fn=partial(simplify, terminal=(sql.Node, sql.Tree, code.Column, code.Table)),
        )
        logic.compare = _intercept(
            logic.compare,
            fn=partial(simplify, terminal=(sql.Node, sql.Tree, code.Tree, code.Query, code.Column, code.Table)),
        )

        scenario()  # The scenario handles its own workspace setup
    finally:
        sql.parse = _sql_parse
        code.Tree.ingest_file = _ingest_file
        logic.compare = _logic_compare

    return {f"{k}.{i}": v[i] for k, v in captured.items() for i in range(len(v))}


def update_snapshots():
    """Generates and updates snapshots based on the current scenario execution."""
    log.info("Generating snapshots...")
    captured_snapshots = capture_snapshots()
    log.info("\tGenerated")

    snapshot_dir = Path(__file__).parent / "snapshots"
    log.info("Deleting old files...")
    if snapshot_dir.exists():
        for file_path in snapshot_dir.glob("**/*"):
            if file_path.is_file():
                log.info(f"\tDeleted {file_path.name}")
                file_path.unlink()
    else:
        snapshot_dir.mkdir(parents=True, exist_ok=True)

    log.info("Writing new files...")
    for key, snapshot_data in captured_snapshots.items():
        snapshot_file = snapshot_dir / f"{key}.json"
        snapshot_file.write_text(snapshot_data)
        log.info(f"\tWrote {snapshot_file.name}")

    log.info("Snapshots updated.")


def get_test_params():
    """Prepares parameters for the pytest test_pipeline function by capturing current outputs."""
    captured_data = capture_snapshots()

    snapshot_dir = Path(__file__).parent / "snapshots"
    correct_data = {file.stem: file.read_text() for file in snapshot_dir.glob("**/*.json") if file.is_file()}

    params = [pytest.param(key, captured_data, correct_data, id=key) for key in list(correct_data.keys())]
    params.append(pytest.param(None, captured_data, correct_data, id="check_new_or_missing_snapshots"))

    return params


@pytest.mark.parametrize("name,captured,correct", get_test_params())
def test_pipeline(name: str, captured: dict, correct: dict):
    """Compares captured snapshots against correct ones, or checks for new or missing snapshots"""
    if name:  # This is for an existing snapshot
        assert name in captured, f"Snapshot '{name}' was not captured (expected based on existing snapshot files)"
        assert correct[name] == captured[name], f"Snapshots '{name}' are different"
    else:  # This is for missing or new snapshots
        extra_keys = set(captured.keys()) - set(correct.keys())
        assert not extra_keys, f"Unexpected snapshots captured: {extra_keys}"

        missing_keys = set(correct.keys()) - set(captured.keys())
        assert not missing_keys, f"Missing snapshots that were captured earlier: {missing_keys}"


if __name__ == "__main__":
    update_snapshots()
