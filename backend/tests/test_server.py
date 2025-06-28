"""
Pytest harness for the in-process LSP server scenario.
"""

import asyncio
from pathlib import Path

import pytest
from pygls.client import JsonRPCClient

import tests.utils as utils
from src import logger

log = logger.get(__name__)


def simplify(obj):
    """Recursively replace absolute paths with relative paths in data structure."""
    match obj:
        case dict():
            return {k: simplify(v) for k, v in obj.items()}
        case list():
            return [simplify(item) for item in obj]
        case str() if str(Path(__file__).parent.parent) in obj:
            return obj.replace(str(Path(__file__).parent.parent), "${workspaceFolder}")
        case _:
            return obj


@pytest.mark.asyncio()
@pytest.mark.parametrize("session_file", ["0_init.ndjson", "1_code_lens.ndjson"])
async def test_server(snapshot, session_file):
    """Test server by replaying recorded session and verifying server's recording."""
    snapshot.snapshot_dir = Path(__file__).parent / "snapshots"
    session_path = Path(__file__).parent / "sessions" / session_file
    recording_path = Path(__file__).parent.parent / "session.last.ndjson"

    # Clear any existing recording
    recording_path.unlink(missing_ok=True)

    # Simulate a client and replay messages from the session file
    client = JsonRPCClient()
    await client.start_io("poetry", "run", "python", "-m", "src.server", "--start-server", "--start-recording")

    # TODO: should replace ${workspaceFolder} back to absolute paths when replaying
    for record in utils.load_ndjson(session_path):
        if record["direction"] == "client->server":
            msg = record["message"]

            if "id" in msg:
                result_future = asyncio.get_running_loop().create_future()

                client.protocol.send_request(
                    msg["method"],
                    msg.get("params", {}),
                    msg_id=msg["id"],
                    callback=lambda result, future=result_future: future.set_result(result),
                )
                result = await result_future
            else:
                client.protocol.notify(msg["method"], msg.get("params", {}))

    await client.stop()

    # Read the recording and format it for snapshot comparison
    result = ["# Testing Server\n"]
    for record in utils.load_ndjson(recording_path):
        result.append(f"## {record['direction']}")
        result.append("```json")
        result.append(utils.pformat(simplify(record["message"])))
        result.append("```\n")
    captured_outputs = "\n".join(result)

    # Clean up the recording file
    recording_path.unlink(missing_ok=True)

    # Compare snapshots
    test_name = f"test_server_{Path(session_file).stem}"
    (snapshot.snapshot_dir / f"{test_name}.last.md").write_text(captured_outputs)
    snapshot.assert_match(captured_outputs, f"{test_name}.true.md")
