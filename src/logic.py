from __future__ import annotations
from dataclasses import dataclass
import Levenshtein
from src import code

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
class Alternative:
    op: code.Op = None
    alt: list[code.Op] = None
    freq: int = None
    score: int = None


class Map:
    tree: code.Tree = None
    all_queries: list[code.Query] = None
    columns_to_ops: list[code.Query] = None

    def __init__(self, tree: code.Tree):
        self.tree = tree
        self.all_queries = self.get_all_queries(tree.queries)
        self.columns_to_ops = self.map_columns_to_ops(self.all_queries)

    def get_all_queries(self, queries: list[code.Query]) -> list[code.Query]:
        nested_queries = []
        for query in queries:
            nested_queries += self.get_all_queries([s for s in query.sources if isinstance(s, code.Query)])
        return queries + nested_queries

    def map_columns_to_ops(self, queries: list[code.Query]) -> dict[tuple[str, str, str], dict[str, list[code.Op]]]:
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

    def find_alternatives(self, op: code.Op, threshold=0.7) -> list[Alternative]:
        suggestions = []
        op_str = str(op)
        for col in op.columns:
            col_ops = self.columns_to_ops[(col.dataset, col.table, col.column)]
            for alt_op_str, alt_op_ops in col_ops.items():
                similarity = Levenshtein.ratio(op_str, alt_op_str)
                if threshold < similarity < 1:
                    suggestions.append(Alternative(freq=len(alt_op_ops), score=similarity, op=op, alt=alt_op_ops))

        suggestions.sort(key=lambda suggestion: (suggestion.freq, suggestion.score), reverse=True)
        return suggestions

    def compare(self, other: Map) -> list[Alternative]:
        output = []
        for query in self.all_queries:
            for op in query.ops:
                output += other.find_alternatives(op)

        return output
