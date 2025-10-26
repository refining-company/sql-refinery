"""
Server — LSP Communication Layer

Architecture:
- Pipeline: SQL parsing, Code AST abstraction, Workspace & logic analysis
- Server: LSP server (this module) - thin I/O wrapper
- Frontend: VS Code extension (frontend-vscode) - owns all UI logic

This module provides:
- Workspace lifecycle management (single instance per server)
- Collect all files (workspace folder + open documents)
- Update workspace on file operations
- Send computed results to frontend via custom notifications (sql-refinery/{key})
- Serialization of Python dataclasses to JSON
"""

import argparse
from pathlib import Path

import lsprotocol.types as lsp
import pygls.server

import src.logger
import src.utils
import src.workspace

log = src.logger.get(__name__)

workspace = src.workspace.Workspace()
lspserver = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    path = src.utils.uri_to_path(params.text_document.uri)
    log.info(f"File opened: {path}")

    workspace.update_file(path, params.text_document.text)

    output = workspace.get_output(path)
    for key, data in output.items():
        # TODO: Filter data before sending to reduce payload size
        # - Remove detailed syntactic column locations from model.Column.code arrays
        # - Frontend only needs semantic column info and first syntactic occurrence
        lspserver.send_notification(
            f"sql-refinery/{key}", {"uri": params.text_document.uri, key: src.utils.serialise(data)}
        )


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    path = src.utils.uri_to_path(params.text_document.uri)
    log.info(f"File changed: {path}")

    content = lspserver.workspace.get_text_document(params.text_document.uri).source
    workspace.update_file(path, content)

    output = workspace.get_output(path)
    for key, data in output.items():
        lspserver.send_notification(
            f"sql-refinery/{key}", {"uri": params.text_document.uri, key: src.utils.serialise(data)}
        )


@lspserver.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    log.info("Initializing LSP server")

    if params.workspace_folders:
        assert len(params.workspace_folders) == 1, "Only one workspace folder is supported"
        folder = src.utils.uri_to_path(params.workspace_folders[0].uri)
        workspace.set_folder(folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Start debugger")
    parser.add_argument("--record", action="store_true", help="Record LSP session")
    parser.add_argument("--replay", help="Replay session from file")
    args = parser.parse_args()

    if args.debug:
        log.info("Starting debugger")
        import src._debugger

        src._debugger.start()

    if args.record:
        log.info("Recording LSP session")
        import src._recorder

        src._recorder.start()

    if args.replay:
        log.info(f"Replaying session: {args.replay}")
        import src._recorder

        session_data = src.utils.load_ndjson(Path(args.replay))
        with src._recorder.mock_client() as (exchange, replay_func):  # type: ignore[has-type]
            for msg in session_data:
                if msg["direction"] == "client->server":
                    replay_func(msg)
        log.info(f"Replayed {len(exchange)} messages")
    else:
        log.info("Starting LSP server")
        lspserver.start_io()
