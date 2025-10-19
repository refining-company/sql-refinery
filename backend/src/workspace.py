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

import src

log = src.logger.get(__name__)


class Workspace:
    folder: Path | None
    files: dict[Path, str]
    output: dict[str, dict]

    def __init__(self):
        self.folder = None
        self.files = {}
        self.output = {"variations": {}}

    def set_folder(self, folder: Path | None) -> None:
        self.folder = folder
        self.files = {}

        if self.folder:
            log.info(f"Workspace folder: {self.folder}")
            for file_path in self.folder.glob("**/*.sql"):
                self.files[file_path] = file_path.read_text()

        self._rebuild()

    def update_file(self, path: Path, content: str) -> None:
        if self.files.get(path) != content:
            self.files[path] = content
            self._rebuild()

    def _rebuild(self) -> None:
        log.info(f"Rebuilding workspace with {len(self.files)} files")

        # Build pipeline: files -> sql.Tree -> code.Tree -> model.Semantics -> variations
        parse_trees = src.sql.build(self.files)
        tree = src.code.build(parse_trees)
        semantics = src.model.build(tree)
        self.output["variations"] = src.variations.build(semantics)

        log.info(f"Computed variations for {[p.stem for p in self.output['variations'].keys()]}")

    def get_output(self, path: Path) -> dict:
        return {"variations": self.output["variations"].get(path, [])}
