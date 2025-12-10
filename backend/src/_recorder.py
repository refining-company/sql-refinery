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


@contextmanager
def listen_server(callback: Callable) -> Generator[list]:
    """Listen to protocol to intercept all client-server communication"""
    captures: list = []

    # Patch
    orig_send_data = pygls.protocol.LanguageServerProtocol._send_data
    orig_procedure_handler = pygls.protocol.LanguageServerProtocol._procedure_handler

    pygls.protocol.LanguageServerProtocol._send_data = src.utils.listen(  # type: ignore
        orig_send_data,
        lambda args, *_: callback(args[1], "server->client"),
        captures,
    )
    pygls.protocol.LanguageServerProtocol._procedure_handler = src.utils.listen(  # type: ignore
        orig_procedure_handler,
        lambda args, *_: callback(args[1], "client->server"),
        captures,
    )

    try:
        yield captures
    finally:
        # Restore
        pygls.protocol.LanguageServerProtocol._send_data = orig_send_data  # type: ignore
        pygls.protocol.LanguageServerProtocol._procedure_handler = orig_procedure_handler  # type: ignore


@contextmanager
def listen_workspace(callback: Callable) -> Generator[list]:
    """Listen to Workspace._rebuild, capture callback return values"""
    captures: list = []

    # Patch
    original_rebuild = src.workspace.Workspace._rebuild
    src.workspace.Workspace._rebuild = src.utils.listen(  # type: ignore
        original_rebuild,
        lambda args, *_: callback(args[0]),
        captures,
    )

    try:
        yield captures
    finally:
        # Restore
        src.workspace.Workspace._rebuild = original_rebuild  # type: ignore


def simplify_server(obj):
    """Simplify LSP message by replacing paths with {cwd} and file contents with {contents}"""
    match obj:
        case dict():
            result = {k: simplify_server(v) for k, v in sorted(obj.items(), key=str)}
            if result.get("params", {}).get("textDocument", {}).get("text"):
                result["params"]["textDocument"]["text"] = "{contents}"
            return result
        case list():
            return sorted([simplify_server(item) for item in obj], key=str)
        case str():
            return src.utils.trunk_path(obj)
        case _:
            return obj


def restore_server(obj):
    """Restore LSP message by replacing {cwd} with paths and {contents} with file contents"""
    match obj:
        case dict():
            result = {k: restore_server(v) for k, v in obj.items()}
            text_doc = result.get("params", {}).get("textDocument", {})
            if text_doc.get("text") == "{contents}" and "uri" in text_doc:
                text_doc["text"] = src.utils.uri_to_path(src.utils.restore_path(text_doc["uri"])).read_text()
            return result
        case list():
            return [restore_server(item) for item in obj]
        case str():
            return src.utils.restore_path(obj)
        case _:
            return obj


def record_session(output_path: Path = src.ROOT_DIR / "logs" / "session.last.ndjson"):
    """Intercept and record client-server communications to logs/session.last.ndjson"""
    output_path.write_text("")

    def capture_to_file(data, direction: str):
        unstructured = converters.get_converter().unstructure(data)
        simplified = simplify_server(unstructured)
        record = {"direction": direction, "message": simplified}
        output_path.open("a").write(json.dumps(record) + "\n")
        return None

    listener = listen_server(capture_to_file)
    listener.__enter__()
    # Intentionally not calling __exit__() - patches remain active for server's lifetime


@contextmanager
def mock_client() -> Generator[Callable]:
    """Setup mock client environment"""
    orig_lspserver = src.server.lspserver
    src.server.lspserver = src.server.Server()

    def send(message: dict):
        """Send client message to server through protocol handler"""
        deserialized = src.server.lspserver.lsp._deserialize_message(message)
        src.server.lspserver.lsp._procedure_handler(deserialized)

    try:
        yield send
    finally:
        src.server.lspserver = orig_lspserver


def replay_session(session_data: list[dict]):
    """Replay LSP session using mock client"""
    with mock_client() as send:
        for record in session_data:
            if record["direction"] == "client->server":
                try:
                    send(restore_server(record["message"]))
                except SystemExit:
                    pass
