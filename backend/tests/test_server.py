"""
Pytest harness for the in-process LSP server scenario.

This module implements a snapshot-based testing approach for LSP server:

1. scenario() - Defines simulated user actions as (request, response) steps
2. capture_snapshots() - Captures each step into JSON snapshots under snapshots_server
3. Test harness parametrizes over those snapshots for regression testing
"""

from pathlib import Path
import dataclasses
import pytest
import lsprotocol.types as lsp
import src.server
import attrs

import tests.utils as utils
from src import logger

log = logger.get(__name__)


def simplify(obj: object) -> dict | list | tuple | str | int | float | bool | None:
    """
    Convert complex LSP objects to simple JSON-serializable structures.
    Handles attrs-based LSP objects properly.
    """
    # Handle basic types directly
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj

    # Handle special types
    if isinstance(obj, Path):
        return str(obj)

    # Handle attrs objects (LSP types use attrs)
    if attrs.has(obj.__class__):
        return simplify(attrs.asdict(obj))

    # Handle dataclasses as fallback
    if dataclasses.is_dataclass(obj):
        return simplify(dataclasses.asdict(obj))  # type: ignore

    # Handle collections
    if isinstance(obj, dict):
        return {str(k): simplify(v) for k, v in obj.items()}

    if isinstance(obj, (list, tuple)):
        return [simplify(item) for item in obj]

    if isinstance(obj, (set, frozenset)):
        return sorted([simplify(item) for item in obj], key=str)

    # Last resort: return class name
    return f"<{obj.__class__.__name__}>"


# Main test scenario
def scenario():
    """
    Perform initialize, open, analyse-document steps, yielding (desc, req, resp) tuples.
    """
    dir_root = Path(__file__).parent
    dir_inputs = dir_root / "inputs"
    dir_codebase = dir_inputs / "codebase"
    file_editor = dir_inputs / "editor.sql"

    # Step 0: initialize
    init_req = lsp.InitializeParams(
        capabilities=lsp.ClientCapabilities(),
        workspace_folders=[lsp.WorkspaceFolder(name=dir_codebase.name, uri=dir_codebase.as_uri())],
    )
    src.server.lspserver.lsp.lsp_initialize(init_req)  # This would trigger lspserver.initialize()
    yield "initialize", init_req, None

    # Step 1: open document
    open_req = lsp.DidOpenTextDocumentParams(
        text_document=lsp.TextDocumentItem(
            uri=file_editor.as_uri(), language_id="sql", version=1, text=file_editor.read_text()
        )
    )
    src.server.did_open(open_req)
    yield "did_open", open_req, None

    # Step 2: get-code-lenses
    lens_req = lsp.CodeLensParams(text_document=lsp.TextDocumentIdentifier(file_editor.as_uri()))
    lens_resp = src.server.code_lens_provider(lens_req)
    yield "code_lens_provider", lens_req, lens_resp

    # Step 3: final-sql (from server workspace)
    doc = src.server.lspserver.workspace.get_text_document(file_editor.as_uri())
    final_sql = getattr(doc, "source", None)
    yield "get_text_document", None, final_sql


# Snapshot lifecycle functions


def capture_snapshots() -> dict:
    """
    Run scenario steps, capture request/response for each step as JSON strings.
    """
    captured = {}
    for idx, (desc, req, resp) in enumerate(scenario()):
        key = f"{idx}.{desc}"
        snapshot = {"request": simplify(req), "response": simplify(resp)}
        captured[key] = utils.pformat(snapshot)
    return captured


def update_snapshots():
    """
    Generates and updates snapshots based on the current scenario execution.
    """
    log.info("Generating snapshots...")
    captured_snapshots = capture_snapshots()
    log.info("\tGenerated")

    snap_dir = Path(__file__).parent / "snapshots_server"
    log.info("Deleting old files...")
    if snap_dir.exists():
        for file_path in snap_dir.glob("*.json"):
            log.info(f"\tDeleted {file_path.name}")
            file_path.unlink()
    else:
        snap_dir.mkdir(parents=True, exist_ok=True)

    log.info("Writing new files...")
    for key, snapshot_data in captured_snapshots.items():
        snapshot_file = snap_dir / f"{key}.json"
        snapshot_file.write_text(snapshot_data)
        log.info(f"\tWrote {snapshot_file.name}")

    log.info("Snapshots updated.")


# Pytest harness


def get_test_params():
    """
    Prepares parameters for pytest by capturing current snapshots and loading golden files.
    """
    captured = capture_snapshots()
    snap_dir = Path(__file__).parent / "snapshots_server"
    correct = {file.stem: file.read_text() for file in snap_dir.glob("*.json")}

    params = [pytest.param(name, captured, correct, id=name) for name in correct]
    params.append(pytest.param(None, captured, correct, id="#new_or_missing"))
    return params


@pytest.mark.parametrize("name,captured,correct", get_test_params())
def test_server(name, captured, correct):
    """
    Compares captured snapshots against correct ones, or checks for new/missing snapshots.
    """
    if name:
        assert name in captured, f"Snapshot '{name}' was not captured"
        assert correct[name] == captured[name], f"Snapshots '{name}' are different"
    else:
        extra_keys = set(captured.keys()) - set(correct.keys())
        assert not extra_keys, f"Unexpected snapshots captured: {extra_keys}"

        missing_keys = set(correct.keys()) - set(captured.keys())
        assert not missing_keys, f"Missing snapshots that were captured earlier: {missing_keys}"


# Create new golden snapshots from CLI
if __name__ == "__main__":
    update_snapshots()
