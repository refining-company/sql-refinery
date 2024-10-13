from pathlib import Path
from src import code
from src import logic


class Workspace:
    path_codebase: Path
    queries_codebase: code.Tree
    queries_editor: code.Tree

    logic_codebase: logic.Map
    logic_editor: logic.Map

    _inconsistencies: dict[str, list[logic.Alternative]]

    def __init__(self):
        self._inconsistencies = {}

    def load_codebase(self, codebase_path: str):
        self.path_codebase = Path(codebase_path).resolve()
        self.queries_codebase = code.parse(path=self.path_codebase)
        self.logic_codebase = logic.parse(self.queries_codebase)

    def find_inconsistencies(self, contents: str, uri: str) -> list[logic.Alternative]:
        self.queries_editor = code.parse(contents=contents)
        self.logic_editor = logic.parse(self.queries_editor)
        self._inconsistencies[uri] = logic.compare(self.logic_editor, self.logic_codebase)

        return self._inconsistencies[uri]
