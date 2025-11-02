"""
Formatting Testing

Tests formatting feature by replaying LSP sessions and capturing before/after snapshots.
"""

from pathlib import Path

import pytest
from lsprotocol import converters

import src
import src._recorder
import tests.utils as utils

TEST_DIR = Path(__file__).parent
SESSIONS_DIR = TEST_DIR / "sessions"
SNAPSHOTS_DIR = TEST_DIR / "snapshots"


def capture_formatting(data, direction: str) -> dict | None:
    """Extract key fields from LSP messages"""
    data_dict = converters.get_converter().unstructure(data)
    method = data_dict.get("method")

    # 1. textDocument/didOpen: extract uri and text
    if method == "textDocument/didOpen":
        uri = data_dict["params"]["textDocument"]["uri"]
        text = data_dict["params"]["textDocument"]["text"]
        return {"method": "open", "uri": uri, "id": None, "text": text}

    # 2. textDocument/formatting: extract request id and uri
    elif method == "textDocument/formatting":
        request_id = data_dict["id"]
        uri = data_dict["params"]["textDocument"]["uri"]
        return {"method": "request", "uri": uri, "id": request_id, "text": None}

    # 3. Server response: extract response id and formatted text
    elif direction == "server->client":
        response_id = data_dict["id"]
        try:
            new_text = data_dict["result"][0]["newText"]
            return {"method": "response", "uri": "", "id": response_id, "text": new_text}
        except (KeyError, IndexError, TypeError):
            pass

    return None


def format_formatting(captures: list[dict]) -> dict[str, str]:
    """Level 3: Walk backwards, chain response → request → didOpen"""
    sequences: list[dict] = []
    relevant = list(reversed([c for c in captures if c is not None]))

    for capture in relevant:
        if capture.get("method") != "response":
            continue

        # Found response - search for matching textDocument/formatting request
        req_id = capture.get("id")
        text_after = capture.get("text")
        request = next((c for c in relevant if c.get("method") == "request" and c.get("id") == req_id), None)
        if not request:
            continue

        # Found request - search for matching textDocument/didOpen
        uri = request.get("uri", "")
        open_msg = next((c for c in relevant if c.get("method") == "open" and c.get("uri") == uri), None)
        if not open_msg:
            continue

        text_before = open_msg.get("text")
        filename = src.utils.uri_to_path(uri).name

        sequences.append({"filename": filename, "before": text_before, "after": text_after})

    # Convert into one markdown file
    md = src.utils.Markdown()
    for sequence in sorted(sequences, key=str):
        md.h1(sequence["filename"])
        md.h2("Before")
        md.code(sequence["before"], "sql")
        md.h2("After")
        md.code(sequence["after"], "sql")

    return {"output": str(md)}


@pytest.mark.parametrize("session_name", [f.stem for f in sorted(SESSIONS_DIR.glob("formatting*.ndjson"))])
def test_formatting(snapshot, session_name):
    """Test formatting with before/after markdown output and trace snapshots"""
    session_dir = SNAPSHOTS_DIR / session_name
    trace_dir = session_dir / "trace"
    snapshot.snapshot_dir = session_dir

    # Replay session
    session_data = src.utils.load_ndjson(SESSIONS_DIR / f"{session_name}.ndjson")
    with (
        utils.listen_server(utils.capture_server) as exchange_snapshots,
        utils.listen_server(capture_formatting) as formatting_captures,
        utils.listen_workspace(utils.capture_workspace) as workspace_snapshots,
    ):
        src._recorder.replay_session(session_data)

    # Format and write snapshots
    exchange_output = utils.format_server(exchange_snapshots)
    utils.write_snapshots(exchange_output, trace_dir, "last.json")

    workspace_output = utils.format_workspace(workspace_snapshots)
    utils.write_snapshots(workspace_output, trace_dir, "last.json")

    formatting_output = format_formatting(formatting_captures)
    utils.write_snapshots(formatting_output, session_dir, "last.md")

    # Compare .last against .true
    for prefix in formatting_output.keys():
        last_file = session_dir / f"{prefix}.last.md"
        true_file = session_dir / f"{prefix}.true.md"
        snapshot.assert_match(last_file.read_text(), true_file)
