import pytest
from pathlib import Path


def get_paths(root: Path = None) -> dict[str, Path]:
    root = root or Path(__file__).parent
    inputs_dir = root / ".submodules" / "playground"
    editor_file = inputs_dir / "code" / "editor.sql"
    codebase_dir = inputs_dir / "code" / "codebase"

    return {"inputs": inputs_dir, "editor": editor_file, "codebase": codebase_dir}


@pytest.fixture(scope="session")
def paths(pytestconfig: pytest.Config) -> dict[str, Path]:
    return get_paths(pytestconfig.rootdir)
