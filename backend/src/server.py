"""
Server — LSP Server

Architecture:
- Pipeline: SQL parsing, Code AST abstraction, Workspace & logic analysis
- Server: LSP server (this module)
- Frontend: VS Code extension (frontend-vscode)

This module provides:
- A pygls-based LanguageServer
- Handlers for open/change, diagnostics and code-lens requests
- Translation from `Workspace` outputs into LSP types
"""

import sys
import argparse
import urllib.parse
from pathlib import Path

import pygls.server
import lsprotocol.types as lsp

import src.logger
import src.workspace

log = src.logger.get(__name__)

# TODO take from package configs
lspserver = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")
workspace = None


def get_workspace(new: bool = False) -> src.workspace.Workspace:
    global workspace

    if new:
        workspace = src.workspace.Workspace()

    assert workspace is not None, "Workspace accessed before initialization"
    return workspace


def analyse_document(uri: str) -> tuple[list[lsp.Diagnostic], list[lsp.CodeLens]]:
    """UI for find_inconsistencies"""
    inconsistencies = get_workspace().find_inconsistencies(path=get_path(uri))

    diagnostics = []
    code_lenses = []
    for inc in inconsistencies:
        # Create diagnostic
        range = lsp.Range(lsp.Position(*inc.this._node.start_point), lsp.Position(*inc.this._node.end_point))
        diagnostic = lsp.Diagnostic(
            range=range,
            message=f"Alternative expressions found in the codebase",
            code="Inconsistency",
            severity=lsp.DiagnosticSeverity.Information,
        )
        diagnostics.append(diagnostic)

        # Create code lens
        title = f"Alternatives found: {len(inc.others)}"
        other_locations = []
        for other in inc.others:
            location_uri = other._file.as_uri()
            location_range = lsp.Range(lsp.Position(*other._node.start_point), lsp.Position(*other._node.end_point))
            other_locations.append({"uri": location_uri, "position": location_range.start, "range": location_range})

        code_lens = lsp.CodeLens(
            range=range,
            command=lsp.Command(
                title=title,
                command="sqlRefinery.peekLocations",
                arguments=[uri, range.end, other_locations, "peek"],
            ),
        )
        code_lenses.append(code_lens)

    return diagnostics, code_lenses


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    document = lspserver.workspace.get_text_document(params.text_document.uri)
    log.info(f"Opening file {document.uri}")

    get_workspace().ingest_file(path=get_path(document.uri), content=document.source)

    diagnostics, _ = analyse_document(document.uri)
    lspserver.publish_diagnostics(document.uri, diagnostics)


@lspserver.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = lspserver.workspace.get_text_document(params.text_document.uri)
    log.info(f"Updating file {document.uri}")
    log.warning(f"File {document.uri} changed. Change handling is not implemented yet.")


@lspserver.feature(lsp.TEXT_DOCUMENT_CODE_LENS)
def code_lens_provider(params: lsp.CodeLensParams):
    document = lspserver.workspace.get_text_document(params.text_document.uri)
    log.info(f"Providing code lenses for file {document.uri}")

    _, code_lenses = analyse_document(document.uri)
    return code_lenses


@lspserver.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    log.info("Initializing LSP server")

    # Initialize workspace on first connect or reset on reconnect
    get_workspace(new=True)

    if params.workspace_folders:
        assert len(params.workspace_folders) == 1, log.error("Only one workspace folder is supported")
        workspace_path = get_path(params.workspace_folders[0].uri)

        log.info(f"Loading workspace folder {workspace_path}")
        get_workspace().ingest_folder(workspace_path)


def start(start_debug: bool = False, start_server: bool = False):
    if start_debug:
        log.info("Starting custom debugger")
        import src._debug

    if start_server:
        log.info(f"Starting LSP server with params {sys.argv}")
        lspserver.start_io()


def get_path(uri: str) -> Path:
    path = urllib.parse.urlparse(uri).path
    path = urllib.parse.unquote(path)
    path = Path(path)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-debug", action="store_true", help="Start custom debugger")
    parser.add_argument("--start-server", action="store_true", help="Start language server")
    args = parser.parse_args()

    start(**vars(args))
