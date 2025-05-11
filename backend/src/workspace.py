"""
Pipeline — Workspace & Logic Analysis

Architecture:
- Pipeline: SQL parsing, Code AST abstraction, Workspace & Logic Analysis (this module)
- Server: LSP server (server.py)
- Frontend: VS Code extension (frontend-vscode)

This module provides:
- `Workspace` to ingest SQL files/folders into a code tree
- Entry point for finding cross-file inconsistencies via `logic.compare`
"""

from pathlib import Path
from src import logic
from src import code
from src import logger

log = logger.get(__name__)


class Workspace:
    tree: code.Tree

    def __init__(self):
        self.tree = code.Tree()

    def ingest_folder(self, path: Path):
        assert path, f"Path to codebase '{path}' is not a directory"

        for file in path.glob("**/*.sql"):
            self.ingest_file(file, file.read_text())

        log.info(f"Injested folder {path}")

    def ingest_file(self, path: Path, content: str):
        self.tree.ingest_file(path=path, content=content)
        log.info(f"Ingested file {path}")

    def find_inconsistencies(self, path: Path) -> list[logic.Alternative]:
        log.info(f"Finding inconsistencies for file {path}")
        return logic.compare(path, self.tree)
