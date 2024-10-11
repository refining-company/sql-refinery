import textwrap
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


def main(codebase_path: str, document: str):
    print(f"Analysing codebase {codebase_path} and document '{document[:100]}'", file=sys.stderr)

    current_session = session.Session(codebase_path=codebase_path)
    suggestions = current_session.analyse_document(contents=document)

    # debug output
    for suggestion in suggestions:
        print(
            "{file}:{start_row}:{start_col}-{end_row}:{end_col}\n"
            "{op}\n\n"
            "Alternatives freq={freq} sim={score}\n"
            "{alts}\n\n=======================\n".format(
                file=suggestion.this.file,
                start_row=suggestion.this.node.start_point.row + 1,
                start_col=suggestion.this.node.start_point.column + 1,
                end_row=suggestion.this.node.end_point.row + 1,
                end_col=suggestion.this.node.end_point.column + 1,
                op=suggestion.this.node.text.decode("utf-8"),
                freq=suggestion.reliability,
                score=suggestion.similarity,
                alts=textwrap.indent("\n\n".join(n.node.text.decode("utf-8") for n in suggestion.others), prefix="\t"),
            ),
            file=sys.stderr,
        )


@server.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: lsp.DidOpenTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    print(f"Opened file: {document.uri}", file=sys.stderr)
    main(sys.argv[1], document.source)


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(params: lsp.DidChangeTextDocumentParams) -> None:
    document = server.workspace.get_text_document(params.text_document.uri)
    print(f"Changed file", file=sys.stderr)
    main(sys.argv[1], document.source)


# def did_open(ls: pygls.server.LanguageServer, params: DidOpenTextDocumentParams):
#     text_document: TextDocumentItem = params.text_document
#     print(f"Opened file: {text_document.uri}", file=sys.stderr)
#     print(f"Server arguments: {sys.argv}", file=sys.stderr)
#     if len(sys.argv) >= 2:
#         main(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    if "--standalone" in sys.argv:
        print(f"Standalone debugging", file=sys.stderr)
        main(sys.argv[1], Path(sys.argv[2]).read_text())
    else:
        print(f"Starting server with params {sys.argv}", file=sys.stderr)
        server.start_io()
