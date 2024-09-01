import pytest
from pathlib import Path


def get_paths() -> dict[str, Path]:
    root = Path(__file__).parent
    inputs_dir = root / "inputs"
    editor_file = inputs_dir / "editor.sql"
    codebase_dir = inputs_dir / "codebase"

    return {"inputs": inputs_dir, "editor": editor_file, "codebase": codebase_dir}


@pytest.fixture(scope="session")
def paths() -> dict[str, Path]:
    return get_paths()
