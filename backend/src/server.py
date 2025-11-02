"""LSP server - thin I/O wrapper"""

import argparse
from pathlib import Path

import lsprotocol.types as lsp
import pygls.server

import src.logger
import src.sql
import src.utils
import src.workspace

log = src.logger.get(__name__)


class Server(pygls.server.LanguageServer):
    """SQL Refinery Language Server with encapsulated state"""

    NAME = "sql-refinery-server"
    VERSION = "0.1-dev"

    def __init__(self):
        super().__init__(self.NAME, self.VERSION)
        self.sql_workspace = src.workspace.Workspace()
        self._register_features()

    def _register_features(self):
        """Register all LSP feature handlers"""

        @self.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
        def _(params: lsp.DidOpenTextDocumentParams):
            return self.did_open(params)

        @self.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
        def _(params: lsp.DidChangeTextDocumentParams):
            return self.did_change(params)

        @self.feature(lsp.TEXT_DOCUMENT_FORMATTING)
        def _(params: lsp.DocumentFormattingParams):
            return self.format_document(params)

        @self.feature(lsp.INITIALIZE)
        def _(params: lsp.InitializeParams):
            return self.initialize(params)

    # ============================================================================
    # LSP Handler Methods
    # ============================================================================

    def did_open(self, params: lsp.DidOpenTextDocumentParams) -> None:
        """Handle textDocument/didOpen"""
        path = src.utils.uri_to_path(params.text_document.uri)
        log.info(f"File opened: {path}")

        self.sql_workspace.update_file(path, params.text_document.text)

        output = self.sql_workspace.get_output(path)
        for key, data in output.items():
            self.send_notification(
                f"sql-refinery/{key}", {"uri": params.text_document.uri, key: src.utils.serialise(data)}
            )

    def did_change(self, params: lsp.DidChangeTextDocumentParams) -> None:
        """Handle textDocument/didChange"""
        path = src.utils.uri_to_path(params.text_document.uri)
        log.info(f"File changed: {path}")

        content = self.sql_workspace.get_text_document(params.text_document.uri).source
        self.sql_workspace.update_file(path, content)

        output = self.sql_workspace.get_output(path)
        for key, data in output.items():
            self.send_notification(
                f"sql-refinery/{key}", {"uri": params.text_document.uri, key: src.utils.serialise(data)}
            )

    def format_document(self, params: lsp.DocumentFormattingParams) -> list[lsp.TextEdit]:
        """Handle textDocument/formatting"""
        path = src.utils.uri_to_path(params.text_document.uri)
        log.info(f"Formatting document: {path}")

        content = self.sql_workspace.layer_files[path]
        formatted = src.sql.format(content)
        return [
            lsp.TextEdit(
                range=lsp.Range(
                    start=lsp.Position(line=0, character=0),
                    end=lsp.Position(line=len(content.splitlines()), character=0),
                ),
                new_text=formatted,
            )
        ]

    def initialize(self, params: lsp.InitializeParams) -> None:
        """Handle initialize"""
        log.info("Initializing LSP server")

        if params.workspace_folders:
            assert len(params.workspace_folders) == 1, "Only one workspace folder is supported"
            folder = src.utils.uri_to_path(params.workspace_folders[0].uri)
            self.sql_workspace.set_folder(folder)


# ============================================================================
# CLI Entry Point
# ============================================================================

# Module-level instance for CLI and imports
lspserver = Server()


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
        # TODO: should use _recorder:replay_session()
        with src._recorder.mock_client() as (exchange, replay_func):  # type: ignore[has-type]
            for msg in session_data:
                if msg["direction"] == "client->server":
                    replay_func(msg)
        log.info(f"Replayed {len(exchange)} messages")
    else:
        log.info("Starting LSP server")
        lspserver.start_io()
