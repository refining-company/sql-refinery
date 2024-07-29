from pathlib import Path
import json
import re
import tree_sitter
import Levenshtein
from dataclasses import dataclass
from src import sql, codebase, utils

# Algorithm:
# [x] Load and parse codebase
# [x] Capture all column identifiers and their respective expressions
# [x] Resolve all column identifiers to include table name derrived from surrounding code
# [ ] Creat `editor.sql` file that will be part of a codebase
# [ ] Create data model (data classes) for `logic.py`
# [ ] Find all expressions in the SELECT clause and create a map dict{Column dataclass: [Op dataclass, ...]}
# [ ] In the current document go expression by expression from those that are in `editor.sql`
# [ ] Match each against other expressions in the codebase map using Levenstein distance of the SQL string
# [ ] For those that are similar but not exactly equal (e.g. > .7 and <0.99)
# [ ] Suggest alternatives ordered by how close they are and how frequently they've been used


@dataclass
class Suggestion:
    file: str
    start_point: tuple[int, int]
    end_point: tuple[int, int]
    expression: str
    score: int = None


class Logic:

    def __init__(self, codebase_path):
        self.codebase = codebase.load(codebase_path)
        self.column_op_map = {}
        self.map_column_uses()

    def map_column_uses(self) -> dict[codebase.Column, dict[str, codebase.Op]]:
        for query in self.codebase.queries:
            for op in query.ops:
                for column in op.columns:
                    col_resolved = (column.dataset, column.table, column.column)
                    self.column_op_map.setdefault(col_resolved, {})
                    self.column_op_map[col_resolved].setdefault(self.get_op_signature(op), []).append(op)

    @staticmethod
    def get_op_signature(op):
        def get_node_signature(node):
            return ":".join([node.type] + [get_node_signature(child) for child in node.children])

        columns_resolved = ":".join(
            [":".join([str(col.dataset), str(col.table), str(col.column)]) for col in op.columns]
        )
        return ":".join([get_node_signature(op.node), columns_resolved])

    def get_similar_op(self, op: codebase.Op):
        suggestions = []
        for col in op.columns:
            col_ops = self.column_op_map[(col.dataset, col.table, col.column)]
            for _, codebase_ops in col_ops.items():
                freq = len(codebase_ops)
                for codebase_op in codebase_ops:
                    op_expression = op.node.text.decode("utf-8")
                    codebase_op_expression = codebase_op.node.text.decode("utf-8")
                    similarity = Levenshtein.ratio(op_expression, codebase_op_expression)
                    if 0.7 < similarity < 1:
                        suggestions.append(
                            Suggestion(
                                codebase_op.file,
                                (codebase_op.node.start_point.row, op.node.start_point.column),
                                (codebase_op.node.end_point.row, op.node.end_point.column),
                                self.resolve_columns(codebase_op.node.text.decode("utf-8"), codebase_op.columns),
                                score=similarity * freq,
                            )
                        )

        return suggestions

    # BUG the expression "SUM(ar.revenue) AS revenue, COUNT(DISTINCT ar.account_id) AS accounts" is processed wrong
    @staticmethod
    def resolve_columns(expression: str, op_columns):
        words = [part for part in re.split(r"(\s+|[\n()])", expression) if part]
        resolved_expression = []
        resolved_columns = {
            str(column.column.decode("utf-8")): (column.dataset, column.table, column.column) for column in op_columns
        }
        for word in words:
            for column in resolved_columns.keys():
                if word.endswith(column):
                    word = ".".join(
                        [
                            (
                                ""
                                if resolved_columns[column][i] is None
                                else str(resolved_columns[column][i].decode("utf-8"))
                            )
                            for i in range(3)
                        ]
                    )
                    resolved_expression.append(word.strip("."))
                else:
                    resolved_expression.append(word)

        return " ".join(resolved_expression)


if __name__ == "__main__":

    editor = load("src/editor")
    logic = Logic("tests/input/code")

    for query in editor.queries:
        for op in query.ops:
            print("\n")
            suggestions = logic.get_similar_op(op)
            utils.print_dataclass(
                Suggestion(
                    op.file,
                    (op.node.start_point.row, op.node.start_point.column),
                    (op.node.end_point.row, op.node.end_point.column),
                    op.node.text.decode("utf-8"),
                )
            )
            print("\n")
            for suggestion in suggestions:
                utils.print_dataclass(suggestion)
                print("\n")
