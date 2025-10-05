"""
Server — LSP Communication Layer

Architecture:
- Pipeline: SQL parsing, Code AST abstraction, Workspace & logic analysis
- Server: LSP server (this module) - thin communication wrapper
- Frontend: VS Code extension (frontend-vscode) - owns all UI logic

This module provides:
- Workspace lifecycle management (initialize, file ingestion)
- Custom notifications to send variations data to frontend
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
workspace = None


def get_workspace(new: bool = False) -> src.workspace.Workspace:
    global workspace

    if new:
        workspace = src.workspace.Workspace()

    assert workspace is not None, "Workspace accessed before initialization"
    return workspace


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
    document = lspserver.workspace.get_text_document(params.text_document.uri)
    log.info(f"Opening file {document.uri}")

    get_workspace().ingest_file(path=get_path(document.uri), content=document.source)

    variations = get_workspace().find_variations(path=get_path(document.uri))
    log.info(f"Found {len(variations)} variations for {document.uri}")

    serialized = serialise(variations)
    log.info(f"Sending sql-refinery/variations notification with {len(serialized)} items")
    lspserver.send_notification("sql-refinery/variations", {"uri": document.uri, "variations": serialized})


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = lspserver.workspace.get_text_document(params.text_document.uri)
    log.info(f"Updating file {document.uri}")

    get_workspace().ingest_file(path=get_path(document.uri), content=document.source)

    variations = get_workspace().find_variations(path=get_path(document.uri))
    lspserver.send_notification("sql-refinery/variations", {"uri": document.uri, "variations": serialise(variations)})


@lspserver.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    log.info("Initializing LSP server")

    # Initialize workspace on first connect or reset on reconnect
    get_workspace(new=True)

    if params.workspace_folders:
        assert len(params.workspace_folders) == 1, log.error("Only one workspace folder is supported")  # type:ignore
        workspace_path = get_path(params.workspace_folders[0].uri)

        log.info(f"Loading workspace folder {workspace_path}")
        get_workspace().ingest_folder(workspace_path)


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
