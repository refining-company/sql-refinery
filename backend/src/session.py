from pathlib import Path
from src import code
from src import logic


class Session:
    path_codebase: Path
    queries_codebase: code.Tree
    queries_editor: code.Tree

    logic_codebase: logic.Map
    logic_editor: logic.Map

    def __init__(self): ...

    def load_codebase(self, codebase_path: str):
        self.path_codebase = Path(codebase_path).resolve()
        self.queries_codebase = code.parse(path=self.path_codebase)
        self.logic_codebase = logic.parse(self.queries_codebase)

    def analyse_document(self, contents: str) -> list[logic.Alternative]:
        self.queries_editor = code.parse(contents=contents)
        self.logic_editor = logic.parse(self.queries_editor)
        suggestions = logic.compare(self.logic_editor, self.logic_codebase)

        return suggestions
