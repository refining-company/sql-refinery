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
    op: codebase.Op = None
    freq: int = None
    score: int = None
    alt: list[codebase.Op] = None


class Logic:
    def __init__(self, codebase_path):
        self.codebase = codebase.load(codebase_path)
        self.all_queries = flatten_queries(self.codebase.queries)
        self.map_column_ops = map_columns_to_ops(self.all_queries)
        ...

    def get_similar_ops(self, op: codebase.Op, threshold=0.7) -> list[Suggestion]:
        suggestions = []
        op_str = str(op)
        for col in op.columns:
            col_ops = self.map_column_ops[(col.dataset, col.table, col.column)]
            for alt_op_str, alt_op_ops in col_ops.items():
                similarity = Levenshtein.ratio(op_str, alt_op_str)
                if threshold < similarity < 1:
                    suggestions.append(Suggestion(freq=len(alt_op_ops), score=similarity, op=op, alt=alt_op_ops))

        suggestions.sort(key=lambda suggestion: (suggestion.freq, suggestion.score), reverse=True)
        return suggestions

    def compare_codebases(self, editor_path) -> list[Suggestion]:
        editor = codebase.load(editor_path)
        output = []
        for query in editor.queries:
            for op in query.ops:
                output += self.get_similar_ops(op)
        return output


def flatten_queries(queries: list[codebase.Query]) -> list[codebase.Query]:
    nested_queries = []
    for query in queries:
        nested_queries += flatten_queries([s for s in query.sources if isinstance(s, codebase.Query)])
    return queries + nested_queries


def map_columns_to_ops(queries: list[codebase.Query]) -> dict[tuple[str, str, str], dict[str, list[codebase.Op]]]:
    column_op_map = {}
    for query in queries:
        for op in query.ops:
            op_id = str(op)
            for column in op.columns:
                col_id = (column.dataset, column.table, column.column)
                column_op_map.setdefault(col_id, {})
                column_op_map[col_id].setdefault(op_id, [])
                column_op_map[col_id][op_id].append(op)

    return column_op_map
