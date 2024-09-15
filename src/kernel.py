from src import code
from src import logic


class Session:
    queries_codebase: code.Tree
    queries_editor: code.Tree

    logic_codebase: logic.Map
    logic_editor: logic.Map

    def __init__(self, codebase_path: str, editor_path: str):
        self.queries_codebase = code.load(codebase_path)
        self.queries_editor = code.load(editor_path)

        self.logic_codebase = logic.Map(self.queries_codebase)
        self.logic_editor = logic.Map(self.queries_editor)

    def analyse_editor(self) -> list[logic.Alternative]:
        suggestions = self.logic_editor.compare(self.logic_codebase)
        return suggestions
