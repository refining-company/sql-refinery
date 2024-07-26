from pathlib import Path
from typing import Tuple
import json
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

# TODO: write hacky code to make it work and output an example. this code will be 100% discarded. we'll use it to undestand
#       how to structure the actual solution.

### TODO Look into deepdiff.DeepHash for hashing node (hashes all of the dict so position in code will become an issue)


# mapping {column -> [ops, ...]}
# [column1->{op.signature:[op,freq]}, column2->, ...]
# you're now looking into editor_op[0]. it uses column3 and column4.
# you check mappping and retrieve only ops for column3 and column4.

# column map
#   {resolved_col1: {op_signature1: [Op1, Op2, Op3 ...],
#                    op_signature2: [Op1, Op2, Op3 ...],
#                    }
#
#   {resolved_col2: {op_signature1: [Op1, Op2, Op3 ...],
#                    op_signature2: [Op1, Op2, Op3 ...],
#
#   }
#

# Op1(column1, column 2) and Op2(column3)
# ALTERNATIVE 1: mapping {column1->[Op1, ...], column2->[Op1, ...], column3->[Op2, ...]} --- best option
# ALTERNATIVE 2: mapping {(column1, column2)->Op1, column3->Op2}

# OP b"date(date_month, 'start of year')"
# b'date_month' 0.9759036144578314
# b"date(date_month, 'start of year')" 1.0
# b'account_id' 0.963855421686747     <--- this does not make sense
# b'date_month' 0.963855421686747

# duble check the codebase is capturing things correctly

# HASH should be SIGNATURE
# hash should be something that is not dependent on where in the code it is, what aliases does it use, etc. but is should
# capture formula (e.g. CASE WHEN), all constants ("North-West") and all fully-resolved columns (dataset.table.column)
# Op1.signature ≈ Op2.signature = Op2 is an example of this forumula that is located in Op2.node (node has SQLParse tree, start, end, etc.)


@dataclass
class Suggestion:
    file: str
    start_point: Tuple[int, int]
    end_point: Tuple[int, int]
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

    # TODO refactor this to be cleaner
    @staticmethod
    def get_op_signature(op):
        # only gets the structure of the node not the identifiers of the leaf nodes since the column aliases are not resolved yet in the tree-sitter level
        def get_node_signature(node):
            node_signature = [node.type]
            [node_signature.append(get_node_signature(child)) for child in node.children]
            return ":".join(node_signature)

        column_strings = [":".join([str(col.dataset), str(col.table), str(col.column)]) for col in op.columns]
        columns_resolved = ":".join(column_strings)

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
                                codebase_op.node.text.decode("utf-8"),
                                score=similarity * freq,
                            )
                        )

        return suggestions

    def simplify(self, obj) -> dict | list | str:
        if isinstance(obj, Codebase | Query | Table | Op | Column):
            keys = list(obj.__dataclass_fields__.keys())
            return {
                ":".join(keys): [
                    self.simplify(getattr(obj, field_name))
                    for field_name, field_info in obj.__dataclass_fields__.items()
                ]
            }

        if isinstance(obj, tree_sitter.Tree):
            return {"root": [self.simplify(obj.root_node)]}

        if isinstance(obj, tree_sitter.Node):
            keys = [obj.grammar_name]
            if obj.type in ("identifier", "number", "string"):
                keys.append(obj.text.decode("utf-8"))
            return {":".join(keys): [self.simplify(child) for child in obj.children]}

        if isinstance(obj, dict):
            return {str(key): self.simplify(value) for key, value in obj.items()}

        if isinstance(obj, list):
            return [self.simplify(item) for item in obj]

        if isinstance(obj, bytes):
            return obj.decode("utf-8")

        try:
            return str(obj)
        except Exception as e:
            raise TypeError(f"Object of type {type(obj)} is not simplifiable: {e}")


if __name__ == "__main__":

    editor = load("src/editor")
    logic = Logic("tests/input/code")

    for query in editor.queries:
        for op in query.ops:
            print("\n")
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
