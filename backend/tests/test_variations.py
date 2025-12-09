"""
Variations Testing

Tests variations feature by replaying LSP sessions and capturing workspace snapshots.
"""

import pytest

import src
import tests.utils as utils

SESSIONS_DIR = src.ROOT_DIR / "backend" / "tests" / "sessions"
SNAPSHOTS_DIR = src.ROOT_DIR / "backend" / "tests" / "snapshots"


def capture_variations(ws: src.workspace.Workspace) -> dict[str, str]:
    """Capture variations as formatted markdown"""
    md = src.utils.Markdown()
    for file_path, file_variations in sorted(ws.layer_variations.items(), key=str):
        md.h1(src.utils.trunk_path(str(file_path)))

        for expr_variations in file_variations:
            this = expr_variations.this
            this_sql = src.utils.compact_str(this.sql)
            md.h2(f"Expression at {this.location}: {len(expr_variations.others)} variations")
            md.text(f"`{this_sql}`")

            for i, variation in enumerate(expr_variations.others):
                md.text(
                    f"Variation {i+1}: similarity {variation.similarity:.2f}, "
                    + f"frequency {variation.group.frequency} "
                    + f"({", ".join(map(str, sorted(variation.group.locations, key=str)))})"
                    + "\n"
                    + f"`{src.utils.compact_str(variation.group.sql)}`"
                )

    return {"output": str(md)}


def format_variations(captures: list[dict[str, str]]) -> dict[str, str]:
    """Take last variation snapshot as output"""
    if captures:
        return captures[-1]
    return {"output": ""}


@pytest.mark.parametrize("session_name", [f.stem for f in sorted(SESSIONS_DIR.glob("variations*.ndjson"))])
def test_variations(snapshot, session_name):
    """Test variations with workspace snapshots and markdown output"""
    session_dir = SNAPSHOTS_DIR / session_name
    trace_dir = session_dir / "trace"
    snapshot.snapshot_dir = session_dir

    # Replay session
    src.server.lspserver = src.server.Server()
    session_data = src.utils.load_ndjson(SESSIONS_DIR / f"{session_name}.ndjson")
    with (
        src._recorder.listen_server(utils.capture_server) as exchange_snapshots,
        src._recorder.listen_workspace(utils.capture_workspace) as workspace_snapshots,
        src._recorder.listen_workspace(capture_variations) as variations_snapshots,
    ):
        src._recorder.replay_session(session_data)

    # Format and write snapshots
    exchange_output = utils.format_server(exchange_snapshots)
    utils.write_snapshots(exchange_output, trace_dir, "last.json")

    workspace_output = utils.format_workspace(workspace_snapshots)
    utils.write_snapshots(workspace_output, trace_dir, "last.json")

    variations_output = format_variations(variations_snapshots)
    utils.write_snapshots(variations_output, session_dir, "last.md")

    # Compare .last against .true
    for prefix in variations_output.keys():
        last_file = session_dir / f"{prefix}.last.md"
        true_file = session_dir / f"{prefix}.true.md"
        snapshot.assert_match(last_file.read_text(), true_file)
