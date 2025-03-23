"""Workspace manages the code online and offline analysis"""

import sys
from pathlib import Path
from src import code
from src import logic


class Workspace:
    path_codebase: Path
    tree: code.Tree
    _inconsistencies: dict[str, list[logic.Alternative]]

    def __init__(self):
        self._inconsistencies = {}
        self.tree = code.Tree()

    def load_codebase(self, path: str):
        self.path_codebase = Path(path).resolve()
        assert self.path_codebase.is_dir(), f"Path to codebase '{path}' is not a directory"
        self.tree = code.from_dir(self.path_codebase)

        print(f"Loaded codebase from {path}", file=sys.stderr)

    def find_inconsistencies(self, uri: str, content: str) -> list[logic.Alternative]:
        editor_file = Path(uri).name
        self.tree.ingest(name=editor_file, content=content)
        self._inconsistencies[uri] = logic.compare(editor_file, self.tree)
        return self._inconsistencies[uri]
