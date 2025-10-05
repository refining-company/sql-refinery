"""
Pipeline — Workspace & Logic Analysis

Architecture:
- Pipeline: SQL parsing, Code AST abstraction, Workspace & Logic Analysis (this module)
- Server: LSP server (server.py) - thin I/O wrapper
- Frontend: VS Code extension (frontend-vscode)

This module provides:
- `Workspace` singleton as process manager and data hub
- Rebuilds analysis from scratch on every file operation
- Caches all computed results in `output` for server to send
"""

from pathlib import Path

from src import code, logger, variations

log = logger.get(__name__)


class Workspace:
    """Process manager and data hub for SQL analysis

    Maintains:
    - files: Current file set (Path -> content)
    - tree: Parsed SQL code tree
    - output: All computed results ready to send to frontend
    """

    files: dict[Path, str]
    tree: code.Tree
    output: dict[str, dict]

    def __init__(self):
        self.files = {}
        self.tree = code.Tree()
        self.output = {"variations": {}}

    def rebuild(self, files: dict[Path, str]) -> None:
        """Rebuild entire workspace from all files

        Clears all state, re-ingests all files, and recomputes all analysis.
        This is stateless per-operation - guarantees consistent results.
        """
        log.info(f"Rebuilding workspace with {len(files)} files")

        # Store files for future reference
        self.files = files

        # Clear analysis state
        self.tree = code.Tree()
        self.output["variations"].clear()

        # Ingest all files into tree
        for path, content in files.items():
            self.tree.ingest_file(path=path, content=content)

        # Compute variations for ALL files
        for path in files.keys():
            vars = variations.get_variations(path, self.tree)
            self.output["variations"][path] = vars
            log.info(f"Computed {len(vars)} variations for {path}")

    def get_output(self, path: Path) -> dict:
        """Get cached output data for a specific file

        Returns dict with all data types ready to send to frontend.
        Server just serializes and sends this.
        """
        return {"variations": self.output["variations"].get(path, [])}
