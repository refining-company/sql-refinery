from pathlib import Path
import re
import Levenshtein
from dataclasses import dataclass
from src import codebase

"""
We take in the the whole codebase and construct a computational query tree, we then create a mapping between columns and 
expressions that use that column, afterwards when we input an expression from the editor we search which operations in the 
codebase use the same column, then measure how similar the texts of the expressions are and based on the similarity and the 
frequency we suggest an expression from the codebase.  
"""

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
    file: list[tuple[str, tuple[int, int], tuple[int, int]]]
    expression: str
    freq: int = 0
    score: int = None

    def __str__(self):
        files_str = "\n    ".join(
            "File:{}:{}:{}, End:{}".format(file, start[0], start[1], end) for file, start, end in self.file
        )
        return (
            f"Files:\n    {files_str}\n"
            f"Expression: {self.expression}\n"
            f"Frequency: {self.freq}\n"
            f"Score: {self.score}\n"
        )


class Logic:

    def __init__(self, codebase_path):
        self.codebase = codebase.load(codebase_path)
        self.column_op_map = {}
        self.map_column_uses()

    def map_column_uses(self) -> dict[codebase.Column, dict[str, codebase.Op]]:
        queries = []
        [
            queries.extend([query] + [source for source in query.sources if isinstance(source, codebase.Query)])
            for query in self.codebase.queries
        ]
        for query in queries:
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
        op_expression = self.resolve_columns(op)
        for col in op.columns:
            col_ops = self.column_op_map[(col.dataset, col.table, col.column)]
            for codebase_ops in col_ops.values():
                codebase_op_expression = self.resolve_columns(codebase_ops[0])
                similarity = Levenshtein.ratio(op_expression, codebase_op_expression)
                if 0.7 < similarity < 1:
                    locations = [
                        (
                            str(c_op.file),
                            (c_op.node.start_point.row + 1, c_op.node.start_point.column + 1),
                            (c_op.node.end_point.row + 1, c_op.node.end_point.column + 1),
                        )
                        for c_op in codebase_ops
                    ]
                    suggestions.append(
                        Suggestion(
                            locations,
                            codebase_op_expression,
                            freq=len(codebase_ops),
                            score=similarity,
                        )
                    )
        suggestions.sort(key=lambda suggestion: (suggestion.score is not None, suggestion.score), reverse=True)
        return suggestions

    # BUG the expression "SUM(ar.revenue) AS revenue, COUNT(DISTINCT ar.account_id) AS accounts" is processed wrong
    ## issue is probably that the alias has the same name as the column name we are resolving
    @staticmethod
    def resolve_columns(op: codebase.Op):
        expression = op.node.text.decode("utf-8")
        op_columns = op.columns
        expression_parts = re.split(r"(\s+|[\n()])", expression)
        resolved_columns = {
            str(column.column.decode("utf-8")): (column.dataset, column.table, column.column) for column in op_columns
        }

        def resolve_word(word):
            for column, parts in resolved_columns.items():
                if word.endswith(column):
                    return ".".join(str(part.decode("utf-8")) if part else "" for part in parts).strip(".")
            return word

        resolved_expression = [resolve_word(word) for word in expression_parts if word]
        return "".join(resolved_expression)


if __name__ == "__main__":
    editor = codebase.load("src/editor")
    logic = Logic("tests/input/code")

    for query in editor.queries:
        for op in query.ops:
            print("\n")
            print("\n")

            suggestions = logic.get_similar_op(op)
            print(
                Suggestion(
                    [
                        (
                            str(op.file),
                            (op.node.start_point.row + 1, op.node.start_point.column + 1),
                            (op.node.end_point.row + 1, op.node.end_point.column + 1),
                        )
                    ],
                    logic.resolve_columns(op),
                )
            )
            for suggestion in suggestions:
                print(suggestion)
