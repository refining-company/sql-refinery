"""
Server — LSP Communication Layer

Architecture:
- Pipeline: SQL parsing, Code AST abstraction, Workspace & logic analysis
- Server: LSP server (this module) - thin I/O wrapper
- Frontend: VS Code extension (frontend-vscode) - owns all UI logic

This module provides:
- Workspace lifecycle management (singleton per session)
- Collect all files (workspace folder + open documents)
- Rebuild workspace on every file operation
- Send computed results to frontend via custom notifications (sql-refinery/{key})
- Serialization of Python dataclasses to JSON
"""

import argparse
import dataclasses
import sys
import urllib.parse
from pathlib import Path

import lsprotocol.types as lsp
import pygls.server

import src.logger
import src.workspace

log = src.logger.get(__name__)

lspserver = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")

# Workspace singleton - created on initialize, persists for session
workspace: src.workspace.Workspace | None = None

# Workspace folder path - set on initialize
workspace_folder: Path | None = None


def collect_all_files() -> dict[Path, str]:
    """Collect all SQL files from workspace folder + open documents

    Combines:
    - Codebase files from disk (workspace_folder/**/*.sql)
    - Open documents from LSP (may override disk with in-memory edits)

    Returns dict: Path -> file content
    """
    files: dict[Path, str] = {}

    # Codebase files from workspace folder on disk
    if workspace_folder:
        for file_path in workspace_folder.glob("**/*.sql"):
            files[file_path] = file_path.read_text()

    # Open documents from LSP workspace (overrides disk files with edits)
    for uri in lspserver.workspace.text_documents:
        document = lspserver.workspace.get_text_document(uri)
        files[get_path(uri)] = document.source

    return files


def serialise(obj):
    """Recursively serialise objects to JSON-compatible format"""
    match obj:
        # Handle dataclass objects
        case _ if dataclasses.is_dataclass(obj):
            data = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
            return {key: serialise(value) for key, value in data.items()}

        # Handle Path objects
        case Path():
            return str(obj)

        # Handle collections
        case list() | frozenset() | set():
            return [serialise(item) for item in obj]
        case dict():
            return {key: serialise(value) for key, value in obj.items()}

        # Handle primitives
        case _:
            return obj


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    """Handle file open: rebuild workspace and send all computed data"""
    path = get_path(params.text_document.uri)
    log.info(f"File opened: {path}")

    # Rebuild entire workspace from all files
    workspace.rebuild(collect_all_files())

    # Get computed output and send each data type to frontend
    output = workspace.get_output(path)
    for key, data in output.items():
        lspserver.send_notification(f"sql-refinery/{key}", {"uri": params.text_document.uri, key: serialise(data)})


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    """Handle file change: rebuild workspace and send all computed data"""
    path = get_path(params.text_document.uri)
    log.info(f"File changed: {path}")

    # Rebuild entire workspace from all files
    workspace.rebuild(collect_all_files())

    # Get computed output and send each data type to frontend
    output = workspace.get_output(path)
    for key, data in output.items():
        lspserver.send_notification(f"sql-refinery/{key}", {"uri": params.text_document.uri, key: serialise(data)})


@lspserver.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    """Initialize workspace singleton and store workspace folder path"""
    global workspace, workspace_folder

    log.info("Initializing LSP server")

    # Create workspace singleton for this session
    workspace = src.workspace.Workspace()

    # Store workspace folder path (codebase location)
    if params.workspace_folders:
        assert len(params.workspace_folders) == 1, "Only one workspace folder is supported"
        workspace_folder = get_path(params.workspace_folders[0].uri)
        log.info(f"Workspace folder: {workspace_folder}")


def start(start_debug: bool = False, start_server: bool = False, start_recording: bool = False):
    if start_debug:
        log.info("Starting custom debugger")
        import src._debug

        src._debug.start()

    if start_recording:
        log.info("Starting LSP session recording")
        import tests.recorder

        tests.recorder.start()

    if start_server:
        log.info(f"Starting LSP server with params {sys.argv}")
        lspserver.start_io()


def get_path(uri: str) -> Path:
    path = urllib.parse.urlparse(uri).path
    path = urllib.parse.unquote(path)
    return Path(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-debug", action="store_true", help="Start custom debugger")
    parser.add_argument("--start-server", action="store_true", help="Start language server")
    parser.add_argument("--start-recording", action="store_true", help="Record LSP session to file")
    args = parser.parse_args()

    start(**vars(args))
