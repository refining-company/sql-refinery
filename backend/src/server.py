"""LSP Server"""

import sys
import argparse
import urllib.parse

import pygls.server
import lsprotocol.types as lsp

from src import logger
from src import workspace

log = logger.get(__name__)

# TODO take from package configs
server = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")
session = workspace.Workspace()


def analyse(document: str, uri: str) -> list[lsp.Diagnostic]:
    inconsistencies = session.find_inconsistencies(content=document, uri=uri)

    diagnostics = []
    for inc in inconsistencies:
        range = lsp.Range(lsp.Position(*inc.this._node.start_point), lsp.Position(*inc.this._node.end_point))
        diagnostic = lsp.Diagnostic(
            range=range,
            message=f"Alternative expressions found in the codebase",
            code="Inconsistency",
            severity=lsp.DiagnosticSeverity.Information,
        )
        diagnostics.append(diagnostic)

    return diagnostics


@server.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    log.info(f"Opening file {document.uri}")
    diagnostics = analyse(document.source, uri=params.text_document.uri)
    server.publish_diagnostics(document.uri, diagnostics)


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    log.info("Refreshing file")
    diagnostics = analyse(document.source, uri=params.text_document.uri)
    server.publish_diagnostics(document.uri, diagnostics)


@server.feature(lsp.TEXT_DOCUMENT_CODE_LENS)
def code_lens_provider(params: lsp.CodeLensParams):
    document_uri = params.text_document.uri
    code_lenses = []

    # Retrieve diagnostics for the document
    inconsistencies = session._inconsistencies.get(document_uri, [])
    for inc in inconsistencies:
        title = f"Alternatives found: {len(inc.others)}"
        range = lsp.Range(lsp.Position(*inc.this._node.start_point), lsp.Position(*inc.this._node.end_point))
        other_locations = []
        for other in inc.others:
            location_uri = (session.path_codebase / other._file).resolve().as_uri()
            location_range = lsp.Range(lsp.Position(*other._node.start_point), lsp.Position(*other._node.end_point))
            other_locations.append({"uri": location_uri, "position": location_range.start})

        # Create the CodeLens entry
        code_lens = lsp.CodeLens(
            range=range,
            command=lsp.Command(
                title=title,
                command="sqlRefinery.peekLocations",
                arguments=[document_uri, range.end, other_locations, "peek"],
            ),
        )
        code_lenses.append(code_lens)
    return code_lenses


@server.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    log.info("Initializing LSP server")

    if params.workspace_folders:
        assert len(params.workspace_folders) == 1, log.error("Only one workspace folder is supported")
        workspace_uri = params.workspace_folders[0].uri
        workspace_path = urllib.parse.urlparse(workspace_uri).path
        workspace_path = urllib.parse.unquote(workspace_path)

        log.info(f"Loading workspace folder {workspace_path}")
        session.load_codebase(workspace_path)


def main(start_debug: bool = False, start_server: bool = False):
    if start_debug:
        log.info("Starting custom debugger")
        import src._debug

    if start_server:
        log.info(f"Starting LSP server with params {sys.argv}")
        server.start_io()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-debug", action="store_true", help="Start custom debugger")
    parser.add_argument("--start-server", action="store_true", help="Start language server")
    args = parser.parse_args()

    main(**vars(args))
