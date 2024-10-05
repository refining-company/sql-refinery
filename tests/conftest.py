import pytest
from pathlib import Path
import difflib


def get_paths() -> dict[str, Path]:
    root = Path(__file__).parent
    inputs_dir = root / "inputs"
    editor_file = inputs_dir / "editor.sql"
    codebase_dir = inputs_dir / "codebase"

    return {"inputs": inputs_dir, "editor": editor_file, "codebase": codebase_dir}


@pytest.fixture(scope="session")
def paths() -> dict[str, Path]:
    return get_paths()


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, str) and isinstance(right, str) and op == "==" and (left + right).count("\n") >= 5:
        diff = list(difflib.unified_diff(left.splitlines(), right.splitlines(), lineterm="", n=0))
        return ["Strings are not equal:"] + diff
