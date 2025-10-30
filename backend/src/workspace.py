"""Pipeline orchestration and caching"""

from __future__ import annotations

from pathlib import Path

import src

log = src.logger.get(__name__)


class Workspace:
    """Pipeline orchestrator managing files, layers, indexes, and maps"""

    layer_folder: Path | None
    layer_files: dict[Path, str]
    layer_sql: dict[Path, src.sql.Tree]
    layer_code: src.code.Code | None
    layer_model: src.model.Model | None
    layer_variations: dict[Path, list[src.variations.ExpressionVariations]]

    _index: dict[type, list]
    _map: dict[tuple, dict]

    # ============================================================================
    # Pipeline Management
    # ============================================================================

    def __init__(self):
        self.layer_folder = None
        self.layer_files = {}
        self._reset()

    def _reset(self):
        self.layer_sql = {}
        self.layer_code = None
        self.layer_model = None
        self.layer_variations = {}
        self._index = {}
        self._map = {}

    def _rebuild(self) -> None:
        log.info(f"Rebuilding workspace with {len(self.layer_files)} files")

        self._reset()

        self.layer_sql = src.sql.build(self)
        self.layer_code = src.code.build(self)
        self.layer_model = src.model.build(self)
        self.layer_variations = src.variations.build(self)

        log.info(f"Computed variations for {[p.stem for p in self.layer_variations.keys()]}")

    # ============================================================================
    # Index & Mapping
    # ============================================================================

    def new[T](self, obj: T) -> T:
        """Register object in type index and return it"""
        obj_type = type(obj)
        if obj_type not in self._index:
            self._index[obj_type] = []

        if obj not in self._index[obj_type]:
            self._index[obj_type].append(obj)

        return obj

    def get[T](self, type_: type[T]) -> list[T]:
        """Get all indexed objects of given type"""
        return self._index[type_]

    def map[Fro, To](self, fro: type[Fro], to: type[To], by: str | tuple[str, ...]) -> dict[Fro, To]:
        """Build lazy map from fro → to via field path (cached)

        Args:
            fro: Source type
            to: Target type
            by: Field name or tuple of field names for multi-hop traversal

        Example:
            ws.map(sql.Node, model.Column, by=("_node", "_code"))
        """
        by = (by,) if isinstance(by, str) else by
        key = (fro, to, by)

        if key in self._map:
            return self._map[key]

        current_pairs = [(obj, obj) for obj in self.get(to)]

        for field in reversed(by):
            next_pairs = []
            for obj, original_to in current_pairs:
                if hasattr(obj, field):
                    val = getattr(obj, field)
                    for item in val if isinstance(val, list | tuple) else [val]:
                        next_pairs.append((item, original_to))
            current_pairs = next_pairs

        result: dict = {}
        for obj, original_to in current_pairs:
            if obj in result:
                raise NotImplementedError(f"One-to-many mapping: {obj} → {result[obj]} and {original_to}")
            result[obj] = original_to

        self._map[key] = result
        return result

    # ============================================================================
    # External APIs
    # ============================================================================

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

    def get_output(self, path: Path) -> dict:
        return {"variations": self.layer_variations.get(path, [])}
