"""
Recording utilities for LSP protocol messages.
"""

import json
from collections.abc import Callable, Generator
from contextlib import contextmanager
from pathlib import Path

import pygls.protocol
from lsprotocol import converters

import src

log = src.logger.get(__name__)


recording_path: Path | None = None
original_methods = {}


def record_message(direction: str, message: dict):
    """Record a single LSP message."""
    if recording_path is None:
        return

    # TODO: should replace absolute paths with ${cwd} when recording
    record = {"direction": direction, "message": converters.get_converter().unstructure(message)}

    with recording_path.open("a") as f:
        f.write(json.dumps(record) + "\n")
        f.flush()


def start(output_path: Path = Path(__file__).parent.parent.parent / "logs" / "session.last.ndjson"):
    """Start recording LSP messages."""
    # TODO: should use patch_server from ./tests/

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


def mock_client_send(client_message: dict):
    """Send client message to server through protocol handler"""
    message = src.server.lspserver.lsp._deserialize_message(client_message["message"])
    src.server.lspserver.lsp._procedure_handler(message)


@contextmanager
def mock_client() -> Generator[Callable]:
    """Setup mock client environment"""
    orig_lspserver = src.server.lspserver
    src.server.lspserver = src.server.Server()

    try:
        yield mock_client_send
    finally:
        src.server.lspserver = orig_lspserver


def replay_session(session_data: list[dict]):
    """Replay LSP session using mock client"""
    with mock_client() as send:
        for record in session_data:
            if record["direction"] == "client->server":
                try:
                    send(record)
                except SystemExit:
                    pass
