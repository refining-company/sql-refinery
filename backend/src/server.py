import sys
import logging
from pathlib import Path

import pygls.server
import lsprotocol.types as lsp

import src
import src._debug


pygls.server.logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
pygls.server.logger.addHandler(handler)

# TODO take from package configs
server = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")
session = src.session.Session()


def analyse(document: str, uri: str = None) -> list[lsp.Diagnostic]:
    inconsistencies = session.find_inconsistencies(contents=document, uri=uri)

    diagnostics = []
    for inc in inconsistencies:
        range = lsp.Range(lsp.Position(*inc.this.node.start_point), lsp.Position(*inc.this.node.end_point))
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
    print(f"Opened file: {document.uri}", file=sys.stderr)
    diagnostics = analyse(document.source, uri=params.text_document.uri)
    server.publish_diagnostics(document.uri, diagnostics)


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    print(f"Changed file", file=sys.stderr)
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
        range = lsp.Range(lsp.Position(*inc.this.node.start_point), lsp.Position(*inc.this.node.end_point))
        other_locations = []
        for other in inc.others:
            location_uri = (session.path_codebase / other.file).resolve().as_uri()
            location_range = lsp.Range(lsp.Position(*other.node.start_point), lsp.Position(*other.node.end_point))
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


if __name__ == "__main__":
    session.load_codebase(sys.argv[1])

    if "--standalone" in sys.argv:
        print(f"Standalone debugging", file=sys.stderr)
        analyse(Path(sys.argv[2]).read_text())
    else:
        print(f"Starting server with params {sys.argv}", file=sys.stderr)
        server.start_io()
