"""Language server"""

import sys
import logging
import argparse
import urllib.parse
from pathlib import Path


import pygls.server
import lsprotocol.types as lsp

import src


pygls.server.logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
pygls.server.logger.addHandler(handler)

# TODO take from package configs
server = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")
session = src.workspace.Workspace()


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
    print(f"Opening file {document.uri}", file=sys.stderr)
    diagnostics = analyse(document.source, uri=params.text_document.uri)
    server.publish_diagnostics(document.uri, diagnostics)


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    print(f"Refreshing file ", file=sys.stderr)
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
    print("Initializing LSP server", file=sys.stderr)

    if params.workspace_folders:
        assert len(params.workspace_folders) == 1, "Only one workspace folder is supported"
        workspace_uri = params.workspace_folders[0].uri
        workspace_path = urllib.parse.urlparse(workspace_uri).path
        workspace_path = urllib.parse.unquote(workspace_path)

        print(f"Loading workspace folder {workspace_path}", file=sys.stderr)
        session.load_codebase(workspace_path)


def main(start_debug: bool = False, start_server: bool = False):
    if start_debug:
        print(f"Starting custom debugger", file=sys.stderr)
        import src._debug

    if start_server:
        print(f"Starting LSP server with params {sys.argv}", file=sys.stderr)
        server.start_io()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-debug", action="store_true", help="Start custom debugger")
    parser.add_argument("--start-server", action="store_true", help="Start language server")
    args = parser.parse_args()

    main(**vars(args))
