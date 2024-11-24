"""Workspace manages the code online and offline analysis
"""

from pathlib import Path
from src import code
from src import logic


class Workspace:
    path_codebase: Path
    queries_codebase: code.Tree
    queries_editor: code.Tree

    _inconsistencies: dict[str, list[logic.Alternative]]

    def __init__(self):
        self._inconsistencies = {}

    def load_codebase(self, path: str):
        self.path_codebase = Path(path).resolve()
        assert self.path_codebase.is_dir(), f"Path to codebase '{path}' is not a directory"
        self.queries_codebase = code.from_dir(self.path_codebase)

    def find_inconsistencies(self, uri: str, contents: str) -> list[logic.Alternative]:
        self.queries_editor = code.ingest(code.Tree(), Path(uri).name, contents)
        self._inconsistencies[uri] = logic.compare(self.queries_editor, self.queries_codebase)

        return self._inconsistencies[uri]
