from pathlib import Path
import textwrap
import sys
import logging

import pygls.server
from lsprotocol.types import (
    TEXT_DOCUMENT_DID_OPEN,
    DidOpenTextDocumentParams,
    TextDocumentItem,
)

from src import session


# TODO take from package configs
pygls.server.logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
pygls.server.logger.addHandler(handler)

server = pygls.server.LanguageServer(name="sql-refinery-server", version="0.1-dev")


def main(codebase_path: str | Path, editor_path: str | Path):
    current_session = session.Session(codebase_path=codebase_path, editor_path=editor_path)
    suggestions = current_session.analyse_editor()

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


def did_open(ls: pygls.server.LanguageServer, params: DidOpenTextDocumentParams):
    text_document: TextDocumentItem = params.text_document
    print(f"Opened file: {text_document.uri}", file=sys.stderr)
    print(f"Server arguments: {sys.argv}", file=sys.stderr)
    if len(sys.argv) >= 2:
        main(sys.argv[1], sys.argv[2])


server.feature(TEXT_DOCUMENT_DID_OPEN)(did_open)

if __name__ == "__main__":
    print(f"Starting server", file=sys.stderr)
    server.start_io()
