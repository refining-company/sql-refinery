from src import code
from src import logic


class Session:
    queries_codebase: code.Tree
    queries_editor: code.Tree

    logic_codebase: logic.Map
    logic_editor: logic.Map

    def __init__(self, codebase_path: str):
        self.queries_codebase = code.parse(path=codebase_path)
        self.logic_codebase = logic.parse(self.queries_codebase)

    def analyse_document(self, contents: str) -> list[logic.Alternative]:
        self.queries_editor = code.parse(contents=contents)
        self.logic_editor = logic.parse(self.queries_editor)
        suggestions = logic.compare(self.logic_editor, self.logic_codebase)

        return suggestions
