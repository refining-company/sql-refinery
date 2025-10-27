"""
Recording utilities for LSP protocol messages.
"""

import json
from collections.abc import Callable, Generator
from contextlib import contextmanager
from pathlib import Path

import lsprotocol.types as lsp
import pygls.protocol
import pygls.workspace
from lsprotocol import converters

import src

log = src.logger.get(__name__)

recording_path: Path | None = None
original_methods = {}


def record_message(direction: str, message: dict):
    """Record a single LSP message."""
    if recording_path is None:
        return

    # TODO: should replace absolute paths with ${workspaceFolder} when recording
    record = {"direction": direction, "message": converters.get_converter().unstructure(message)}

    with recording_path.open("a") as f:
        f.write(json.dumps(record) + "\n")
        f.flush()


def start(output_path: Path = Path(__file__).parent.parent.parent / "logs" / "session.last.ndjson"):
    """Start recording LSP messages."""
    global recording_path, original_methods

    recording_path = output_path
    recording_path.write_text("")

    log.info(f"Recording LSP session to {recording_path}")

    original_methods = {
        "_send_data": pygls.protocol.LanguageServerProtocol._send_data,
        "_procedure_handler": pygls.protocol.LanguageServerProtocol._procedure_handler,
    }

    def patched_send_data(self, data):
        record_message("server->client", data)
        return original_methods["_send_data"](self, data)

    def patched_procedure_handler(self, message):
        record_message("client->server", message)
        return original_methods["_procedure_handler"](self, message)

    pygls.protocol.LanguageServerProtocol._send_data = patched_send_data  # type: ignore
    pygls.protocol.LanguageServerProtocol._procedure_handler = patched_procedure_handler  # type: ignore


@contextmanager
def mock_client() -> Generator[tuple[list, Callable]]:
    exchange: list = []

    src.server.workspace = src.workspace.Workspace()
    src.server.lspserver.lsp._workspace = pygls.workspace.Workspace(None)  # type: ignore

    orig_send_notification = src.server.lspserver.send_notification
    src.server.lspserver.send_notification = lambda method, params: exchange.append(  # type: ignore
        {"direction": "server->client", "type": "notification", "method": method, "params": params}
    )

    def replay(client_message: dict) -> None:
        converter = src.server.lspserver.lsp._converter

        msg = client_message["message"]
        method = msg.get("method")
        params = msg.get("params", {})

        exchange.append({"direction": "client->server", "method": method, "data": msg})

        response = None
        match method:
            case "initialize":
                response = src.server.initialize(converter.structure(params, lsp.InitializeParams))
            case "textDocument/didOpen":
                src.server.did_open(converter.structure(params, lsp.DidOpenTextDocumentParams))
            case "textDocument/formatting":
                response = src.server.format_document(converter.structure(params, lsp.DocumentFormattingParams))

        if response is not None:
            exchange.append({"direction": "server->client", "type": "response", "method": method, "data": response})

    try:
        yield exchange, replay
    finally:
        src.server.lspserver.send_notification = orig_send_notification  # type: ignore
