import sys
import logging
from pathlib import Path

import pygls.server
import lsprotocol.types as lsp

from src import session


# TODO take from package configs
pygls.server.logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
pygls.server.logger.addHandler(handler)

server = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")


def main(codebase_path: str, document: str) -> list[lsp.Diagnostic]:
    print(f"Analysing codebase {codebase_path} and document '{document[:100]}'", file=sys.stderr)

    current_session = session.Session(codebase_path=codebase_path)
    suggestions = current_session.analyse_document(contents=document)

    # debug output
    diagnostics = []
    for suggestion in suggestions:
        diagnostic = lsp.Diagnostic(
            range=lsp.Range(
                start=lsp.Position(
                    line=suggestion.this.node.start_point.row,
                    character=suggestion.this.node.start_point.column,
                ),
                end=lsp.Position(
                    line=suggestion.this.node.end_point.row,
                    character=suggestion.this.node.end_point.column,
                ),
            ),
            message="Potential logical conflict with codebase",
            severity=lsp.DiagnosticSeverity.Warning,
            code="Logic conflict",
            source="SQL Refinery",
        )
        diagnostics.append(diagnostic)
    return diagnostics


@server.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    print(f"Opened file: {document.uri}", file=sys.stderr)
    diagnostics = main(sys.argv[1], document.source)
    server.publish_diagnostics(document.uri, diagnostics)


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    print(f"Changed file", file=sys.stderr)
    diagnostics = main(sys.argv[1], document.source)
    server.publish_diagnostics(document.uri, diagnostics)


if __name__ == "__main__":
    if "--standalone" in sys.argv:
        print(f"Standalone debugging", file=sys.stderr)
        main(sys.argv[1], Path(sys.argv[2]).read_text())
    else:
        print(f"Starting server with params {sys.argv}", file=sys.stderr)
        server.start_io()
