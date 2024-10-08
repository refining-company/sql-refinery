from src import code
from src import logic


class Session:
    queries_codebase: code.Tree
    queries_editor: code.Tree

    logic_codebase: logic.Map
    logic_editor: logic.Map

    def __init__(self, codebase_path: str, editor_path: str):
        self.queries_codebase = code.parse(codebase_path)
        self.queries_editor = code.parse(editor_path)

        self.logic_codebase = logic.parse(self.queries_codebase)
        self.logic_editor = logic.parse(self.queries_editor)

    def analyse_editor(self) -> list[logic.Alternative]:
        suggestions = logic.compare(self.logic_editor, self.logic_codebase)
        return suggestions
