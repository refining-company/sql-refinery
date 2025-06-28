"""
Test Pipeline Architecture

This module implements a snapshot-based testing approach for SQL analysis:

1. Test Organization:
   - scenario() - Defines the business logic test cases with clear ownership of its state
   - Pytest fixtures for non-intrusive function interception
   - Snapshots are stored using pytest-snapshot, capturing the exact structure of important outputs

2. Key Design Principles:
   - Tests own their state management (scenario resets workspace)
   - Function interception through pytest fixtures isolates what's being tested
   - Complex objects are simplified to comparable structures
   - Separation between snapshot generation and verification
"""

import dataclasses
import re
from collections import defaultdict
from collections.abc import Callable
from functools import wraps
from pathlib import Path

import pytest

import tests.utils as utils
from src import code, logger, logic, server, sql

log = logger.get(__name__)


def scenario():
    """Business logic test scenario."""
    dir_root = Path(__file__).parent
    dir_inputs = dir_root / "inputs"
    dir_codebase = dir_inputs / "codebase"
    file_editor = dir_inputs / "editor.sql"

    log.info("Starting scenario...")
    workspace = server.get_workspace(new=True)  # Start with a fresh workspace
    workspace.ingest_folder(dir_codebase)
    workspace.ingest_file(path=file_editor, content=file_editor.read_text())
    workspace.find_variations(path=file_editor)
    log.info("Scenario finished.")


def simplify(obj, terminal=()) -> dict | list | tuple | str | int | float | bool | None:
    # Terminal class handling
    if isinstance(obj, terminal):
        match obj:
            case sql.Node():
                return simplify(obj.text, terminal)
            case logic.Variation() | code.Tree() | code.Query() | code.Expression() | code.Column() | code.Table():
                return repr(obj)
            case _:
                return f"<{obj.__class__.__name__}>"

    # Non-terminal class nandling
    else:
        match obj:
            # Custom data structures
            case logic.Variation() | code.Tree() | code.Query() | code.Expression() | code.Column() | code.Table():
                obj_dict = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
                return {f"{repr(obj)} = {str(obj)}": simplify(obj_dict, terminal)}

            # Tree-sitter objects
            case sql.Tree():
                return [simplify(obj.root_node)]

            case sql.Node():
                node_type = sql.get_type(obj, meta=True, helper=False, original=False)

                children = simplify(obj.children, terminal)  # simplify recursively
                children = [child for child in children if child]  # type:ignore  # filter out empty values
                children = sum(
                    [child if isinstance(child, list) else [child] for child in children], []
                )  # flatten the list

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
                return str(obj)
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
    """Capture function calls and their outputs for snapshot testing. Returns a decorator and a dictionary to store captured outputs."""
    captured = defaultdict(list)

    def capture(target, processor) -> tuple[Callable, Callable]:
        key = f"{target.__module__}.{target.__name__}"

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)
            captured[key].append(processor(result))
            return result

        return target, wrapper

    return capture, captured


@pytest.fixture(scope="module")
def captured_outputs():
    """Run scenario once and capture outputs for all tests."""

    # Patch functions to capture their outputs and simplify
    capture, captured = get_capturer()
    _sql_parse, sql.parse = capture(
        sql.parse,
        lambda result: simplify(result),
    )
    _ingest_file, code.Tree.ingest_file = capture(
        code.Tree.ingest_file,
        lambda result: simplify(result, terminal=(sql.Node, sql.Tree, code.Column, code.Table)),
    )
    _compare, logic.compare = capture(
        logic.compare,
        lambda result: simplify(result, terminal=(sql.Node, sql.Tree, code.Tree, code.Query, code.Column, code.Table)),
    )

    try:
        scenario()
    finally:
        # Restore original functions
        sql.parse = _sql_parse
        code.Tree.ingest_file = _ingest_file
        logic.compare = _compare

    md_lines = ["# Testing Pipeline\n"]
    for key, values in captured.items():
        for i, value in enumerate(values):
            md_lines.append(f"# STEP: {key} {i+1}\n")
            md_lines.append("```json")
            md_lines.append(utils.pformat(value))
            md_lines.append("```\n")

    return "\n".join(md_lines)


def test_pipeline(snapshot, captured_outputs):
    snapshot.snapshot_dir = Path(__file__).parent / "snapshots"
    (snapshot.snapshot_dir / "test_pipeline.last.md").write_text(captured_outputs)
    snapshot.assert_match(captured_outputs, "test_pipeline.true.md")
