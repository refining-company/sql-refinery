"""
Pytest harness for the in-process LSP server scenario.
"""

import sys
from pathlib import Path

import lsprotocol.types as lsp
import pytest
import pytest_lsp
from pytest_lsp import ClientServerConfig, LanguageClient

from src import logger

log = logger.get(__name__)


@pytest_lsp.fixture(config=ClientServerConfig(server_command=[sys.executable, "-m", "src.server", "--start-server"]))
async def client(lsp_client: LanguageClient):
    yield lsp_client
    await lsp_client.shutdown_session()


async def scenario(client: LanguageClient):
    """Perform LSP server testing steps and yield results."""
    # Set up folder structure
    path_inputs = Path(__file__).parent / "inputs"
    path_editor = path_inputs / "editor.sql"
    path_codebase = path_inputs / "codebase"

    # Client opens up workspace and file
    workspace_folders = [lsp.WorkspaceFolder(name=path_codebase.name, uri=path_codebase.as_uri())]
    editor_doc = lsp.TextDocumentItem(path_editor.as_uri(), "sql", 1, path_editor.read_text())

    # Step 0: initialize session
    init_params = lsp.InitializeParams(capabilities=lsp.ClientCapabilities(), workspace_folders=workspace_folders)
    init_result = await client.initialize_session(init_params)
    yield "Initialise", (init_params, init_result)

    # Step 1: open document and wait for diagnostics
    diag_future = client.wait_for_notification("textDocument/publishDiagnostics")
    open_params = lsp.DidOpenTextDocumentParams(text_document=editor_doc)
    client.text_document_did_open(open_params)
    diagnostics = getattr(await diag_future, "diagnostics", [])
    yield "Open document", (open_params, diagnostics)

    # Step 2: get-code-lenses
    lens_params = lsp.CodeLensParams(text_document=lsp.TextDocumentIdentifier(editor_doc.uri))
    lens_result = await client.text_document_code_lens_async(lens_params)
    yield "Get code lenses", (lens_params, lens_result, editor_doc)

    # Step 3: get document content
    yield "Get final document", editor_doc


def simplify(obj):
    match obj:
        # Complex request-response pairs

        case [lsp.InitializeParams(workspace_folders=folders), lsp.InitializeResult()]:
            folder_names = [f.name for f in folders or []]
            return f"Initialize with workspace folders: `{', '.join(folder_names)}`"

        case [lsp.DidOpenTextDocumentParams(text_document=doc_id), list() as diagnostics]:
            doc_uri = simplify(doc_id.uri)
            result = [f"Document opened: `{doc_uri}`"]

            result += ["Found " + str(len(diagnostics)) + " diagnostics:"]
            for diag in diagnostics:
                result += [f"- `{doc_uri}:{simplify(diag.range)}` {diag.message} "]
                result += ["  ```sql"]
                result += [simplify((doc_id, diag.range))]
                result += ["  ```\n"]

            return "\n".join(result)

        case [lsp.CodeLensParams(text_document=doc_id), list() as codelenses, lsp.TextDocumentItem() as doc_item]:
            doc_uri = simplify(doc_id.uri)
            result = [f"Code lens requested for: `{doc_uri}`"]

            result += [f"Found {len(codelenses)} code lenses:"]
            for lens in codelenses:
                result += [f"- `{doc_uri}:{simplify(lens.range)}` {lens.command.title}"]
                result += ["  ```sql"]
                result += [simplify((doc_item, lens.range))]
                result += ["  ```\n"]

            return "\n".join(result)

        # Atomic cases

        case str() if obj.startswith("file://"):
            return Path(obj.replace("file://", "")).name

        case lsp.TextDocumentItem(uri=uri, text=text):
            return f"`{simplify(uri)}`\n```sql\n{text}\n```"

        case (lsp.TextDocumentItem() as doc, lsp.Range() as range):
            lines = doc.text.splitlines()
            return "\n".join(lines[range.start.line : range.end.line + 1])

        case lsp.Range(start=start, end=end):
            return f"{start.line}:{start.character}-{end.line}:{end.character}"

        case _ if not obj:
            return ""

        case _:
            return str(obj)


@pytest.mark.asyncio()
async def test_server(client: LanguageClient, snapshot):
    snapshot.snapshot_dir = Path(__file__).parent / "snapshots"
    result = ["# Testing Server"]

    idx = 0
    async for name, step_result in scenario(client):
        result += [f"## STEP {idx}: {name}"]
        result += [simplify(step_result)]
        result += ["\n"]
        idx += 1

    captured_outputs = "\n".join(result)
    (snapshot.snapshot_dir / "test_server.last.md").write_text(captured_outputs)
    snapshot.assert_match(captured_outputs, "test_server.true.md")
