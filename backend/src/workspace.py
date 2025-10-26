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

    # Indexes (type-based lookups) - unified index for all layers
    index: dict[type, list]

    def __init__(self):
        self.layer_folder = None
        self.layer_files = {}
        self._reset()

    def _reset(self):
        """Reset all computed layers, indexes, and maps"""
        self.layer_sql = {}
        self.layer_code = None
        self.layer_model = None
        self.layer_variations = {}
        self.index = {}
        self._map_cache = {}

    def new(self, obj):
        """Index an object and return it"""
        obj_type = type(obj)
        if obj_type not in self.index:
            self.index[obj_type] = []

        # Only add if not already in index (prevent duplicates)
        if obj not in self.index[obj_type]:
            self.index[obj_type].append(obj)

        return obj

    def map(self, fro: type, to: type) -> dict:
        """Get or build lazy map from fro → to via _code field"""
        key = (fro, to)

        if key not in self._map_cache:
            mapping = {}
            for to_obj in self.index[to]:
                if hasattr(to_obj, "_code"):
                    for fro_obj in to_obj._code:
                        if isinstance(fro_obj, fro):
                            mapping[fro_obj] = to_obj
            self._map_cache[key] = mapping

        return self._map_cache[key]

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

        self._reset()

        self.layer_sql = src.sql.build(self)
        self.layer_code = src.code.build(self)
        self.layer_model = src.model.build(self)
        self.layer_variations = src.variations.build(self)

        log.info(f"Computed variations for {[p.stem for p in self.layer_variations.keys()]}")

    def get_output(self, path: Path) -> dict:
        return {"variations": self.layer_variations.get(path, [])}
