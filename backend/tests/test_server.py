"""
Pytest harness for the in-process LSP server scenario.
"""

from functools import wraps
from itertools import chain
from pathlib import Path

import pytest
import lsprotocol.types as lsp
import pygls.workspace
import pygls.server

import src.server
from src import logger

log = logger.get(__name__)


def scenario():
    """Perform LSP server testing steps and yield results."""
    dir_root = Path(__file__).parent
    dir_inputs = dir_root / "inputs"
    file_editor = dir_inputs / "editor.sql"
    codebase_dir = dir_inputs / "codebase"

    # Step 0: initialize
    init_req = lsp.InitializeParams(
        capabilities=lsp.ClientCapabilities(),
        workspace_folders=[lsp.WorkspaceFolder(name=codebase_dir.name, uri=codebase_dir.as_uri())],
    )
    init_resp = src.server.lspserver.lsp.lsp_initialize(init_req)
    yield "Initialise", (init_req, init_resp)

    # Step 1: open document - capture diagnostics
    diag_resp = []
    _publish_diagnostics = src.server.lspserver.publish_diagnostics
    src.server.lspserver.publish_diagnostics = _intercept(lambda uri, diagnostics: diagnostics, diag_resp)
    try:
        open_req = lsp.DidOpenTextDocumentParams(
            text_document=lsp.TextDocumentItem(
                uri=file_editor.as_uri(), language_id="sql", version=1, text=file_editor.read_text()
            )
        )
        src.server.did_open(open_req)
    finally:
        src.server.lspserver.publish_diagnostics = _publish_diagnostics

    yield "Open document", (open_req, list(chain.from_iterable(diag_resp)))

    # Step 2: get-code-lenses
    lens_req = lsp.CodeLensParams(text_document=lsp.TextDocumentIdentifier(file_editor.as_uri()))
    yield "Get code lenses", (lens_req, src.server.code_lens_provider(lens_req))

    # Step 3: get document content
    doc = src.server.lspserver.workspace.get_text_document(file_editor.as_uri())
    yield "Get final document", doc


def simplify(obj, lspserver: pygls.server.LanguageServer):
    match obj:
        # Copmlex request-response pairs

        case [lsp.InitializeParams(workspace_folders=folders), lsp.InitializeResult()]:
            folder_names = [f.name for f in folders or []]
            return f"Initialize with workspace folders: `{', '.join(folder_names)}`"

        case [lsp.DidOpenTextDocumentParams(text_document=doc_id), list() as diagnostics]:
            doc_uri = simplify(doc_id.uri, lspserver)
            result = [f"Document opened: `{simplify(doc_id.uri, lspserver)}`"]

            result += ["Found " + str(len(diagnostics)) + " diagnostics:"]
            doc_id = lspserver.workspace.get_text_document(doc_id.uri)
            for diag in diagnostics:
                result += [f"- `{doc_uri}:{simplify(diag.range, lspserver)}` {diag.message} "]
                result += ["  ```sql"]
                result += ["".join(doc_id.lines[diag.range.start.line : diag.range.end.line + 1]) + "  ```\n"]

            return "\n".join(result)

        case [lsp.CodeLensParams(text_document=doc_id), list() as codelenses]:
            doc_uri = simplify(doc_id.uri, lspserver)
            result = [f"Code lens requested for: `{doc_uri}`"]
            result += [f"Found {len(codelenses)} code lenses:"]

            doc_id = lspserver.workspace.get_text_document(doc_id.uri)
            for lens in codelenses:
                result += [f"- `{doc_uri}:{simplify(lens.range, lspserver)}` {lens.command.title}"]
                result += ["  ```sql"]
                result += ["".join(doc_id.lines[lens.range.start.line : lens.range.end.line + 1]) + "  ```\n"]

                for loc in lens.command.arguments[2]:
                    doc_alt = lspserver.workspace.get_text_document(loc["uri"])

                    result += [f"  - `{simplify(loc["uri"], lspserver)}:{simplify(loc["range"], lspserver)}`"]
                    result += []
                    result += ["    ```sql"]
                    result += [
                        "".join(doc_alt.lines[loc["range"].start.line : loc["range"].end.line + 1]) + "    ```\n"
                    ]

            return "\n".join(result)

        # Atomic cases

        case str() if obj.startswith("file://"):
            return Path(obj.replace("file://", "")).name

        case pygls.workspace.TextDocument() as doc_id:
            return f"`{simplify(doc_id.uri, lspserver)}`\n```sql\n{doc_id.source}\n```"

        case lsp.Range(start=start, end=end):
            return f"{start.line}:{start.character}-{end.line}:{end.character}"

        case _ if not obj:
            return ""

        case _:
            return str(obj)


def _intercept(target, captures: list):
    """Creates a decorator that intercepts calls to the target function."""

    @wraps(target)
    def wrapper(*args, **kwargs):
        result = target(*args, **kwargs)
        captures.append(result)
        return result

    return wrapper


@pytest.fixture(scope="module")
def captured_outputs():
    """Run scenario steps and convert them to snapshot format."""
    output = ["# Testing Server"]

    for idx, (name, result) in enumerate(scenario()):
        output += [f"## STEP {idx}: {name}"]
        output += [simplify(result, src.server.lspserver)]
        output += ["\n"]

    return "\n".join(output)


def test_server(snapshot, captured_outputs):
    snapshot.snapshot_dir = Path(__file__).parent / "snapshots"
    (snapshot.snapshot_dir / "test_server.last.md").write_text(captured_outputs)
    snapshot.assert_match(captured_outputs, "test_server.true.md")
