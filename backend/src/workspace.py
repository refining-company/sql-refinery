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

from __future__ import annotations

from pathlib import Path

import src

log = src.logger.get(__name__)


class Workspace:
    layer_folder: Path | None
    layer_files: dict[Path, str]
    layer_sql: dict[Path, src.sql.Tree]
    layer_code: src.code.Tree | None
    layer_model: src.model.Semantics | None
    layer_variations: dict[Path, list[src.variations.ExpressionVariations]]

    def __init__(self):
        self.layer_folder = None
        self.layer_files = {}
        self.layer_sql = {}
        self.layer_code = None
        self.layer_model = None
        self.layer_variations = {}

    def set_folder(self, folder: Path | None) -> None:
        self.layer_folder = folder
        self.layer_files = {}

        if self.layer_folder:
            log.info(f"Workspace folder: {self.layer_folder}")
            for file_path in self.layer_folder.glob("**/*.sql"):
                self.layer_files[file_path] = file_path.read_text()

        self._rebuild()

    def update_file(self, path: Path, content: str) -> None:
        if self.layer_files.get(path) != content:
            self.layer_files[path] = content
            self._rebuild()

    def _rebuild(self) -> None:
        log.info(f"Rebuilding workspace with {len(self.layer_files)} files")

        self.layer_sql = src.sql.build(self.layer_files)
        self.layer_code = src.code.build(self.layer_sql)
        self.layer_model = src.model.build(self.layer_code)
        self.layer_variations = src.variations.build(self.layer_model)

        log.info(f"Computed variations for {[p.stem for p in self.layer_variations.keys()]}")

    def get_output(self, path: Path) -> dict:
        return {"variations": self.layer_variations.get(path, [])}
