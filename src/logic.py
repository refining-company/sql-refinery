from pathlib import Path
import json
from deepdiff import DeepDiff
from sql import Tree, Node
from codebase import Codebase, Column, Op, Table, Column, Query, load


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

### Important!! Op dataclass needs to be hashable in order to use it in a dict to get the frequencies of the operation


class QueryTreeJSONEncoder(json.JSONEncoder):

    def __init__(self, **kwargs):
        super(QueryTreeJSONEncoder, self).__init__(**kwargs)

    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode()
        elif isinstance(obj, Codebase):
            return self.encode_codebase(obj)
        elif isinstance(obj, Query):
            return self.encode_query(obj)
        elif isinstance(obj, Op):
            return self.encode_op(obj)
        elif isinstance(obj, Table):
            return self.encode_table(obj)
        elif isinstance(obj, Column):
            return self.encode_column(obj)
        elif isinstance(obj, Node):
            return self.encode_node(obj)
        elif isinstance(obj, Tree):
            return self.encode_tree(obj)
        elif isinstance(obj, Path):
            return self.encode_path(obj)
        elif obj is None:
            return "None"
        else:
            return super().default(obj)

    def encode_codebase(self, codebase: Codebase):
        encoded_dict = {}

        for path, tree in codebase.files.items():
            encoded_dict[str(path)] = self.encode_tree(tree)

        encoded_codebase = {"files": encoded_dict, "queries": [self.encode_query(query) for query in codebase.queries]}
        return encoded_codebase

    def encode_query(self, query: Query):
        encoded_query = {
            "node": self.encode_node(query.node),
            "sources": [self.default(obj) for obj in query.sources],
            "ops": [self.encode_op(op) for op in query.ops],
            "alias": self.default(query.alias),
        }
        return encoded_query

    def encode_table(self, table: Table):
        encoded_table = {
            "node": self.encode_node(table.node),
            "dataset": self.default(table.dataset),
            "table": self.default(table.table),
            "alias": self.default(table.alias),
        }

        return encoded_table

    def encode_op(self, op: Op):
        encoded_op = {
            "node": self.encode_node(op.node),
            "columns": [self.encode_column(column) for column in op.columns],
            "alias": self.default(op.alias),
        }
        return encoded_op

    def encode_column(self, column: Column):
        encoded_column = {
            "node": [self.encode_node(node) for node in column.nodes],
            "dataset": self.default(column.dataset),
            "table": self.default(column.table),
            "column": self.default(column.column),
        }
        return encoded_column

    def encode_node(self, node: Node):
        encoded_node = {
            "type": node.type,
            "children": [self.encode_node(child) for child in node.children],
        }
        if node.type in ["identifier", "number", "string"]:
            encoded_node["text"] = node.text.decode("utf-8")
        return encoded_node

    def encode_tree(self, tree: Tree):
        encoded_tree = {"root": self.encode_node(tree.root_node)}
        return encoded_tree


encoder = QueryTreeJSONEncoder()


def count_keys_and_values(d):
    num_keys = 0
    num_values = 0

    def traverse_dict(d):
        nonlocal num_keys, num_values
        if isinstance(d, dict):
            num_keys += len(d)
            for key, value in d.items():
                traverse_dict(value)
        elif isinstance(d, list):
            num_values += len(d)
            for item in d:
                traverse_dict(item)
        else:
            num_values += 1

    traverse_dict(d)
    return num_keys + num_values


def map_column_uses(codebase: Codebase) -> dict[Column, Op]:

    column_map = {}

    for query in codebase.queries:
        for op in query.ops:
            for column in op.columns:

                col_resolved = (column.dataset, column.table, column.column)
                column_map.setdefault(col_resolved, {})
                column_map[col_resolved].setdefault(op, [op, 0])
                column_map[col_resolved][op][1] += 1
    return column_map


if __name__ == "__main__":

    codebase = load("tests/input/code")
    editor = load("src/editor")

    column_op_mapping = map_column_uses(codebase)

    for query in editor.queries:
        for editor_op in query.ops:
            for col in editor_op.columns:
                ops = column_op_mapping[(col.dataset, col.table, col.column)]
                op_score = {}

                for op_signature, op_freq in ops.items():
                    editor_op_dict = encoder.default(editor_op)
                    codebase_op_dict = encoder.default(ops[op_signature][0])

                    differences = DeepDiff(editor_op_dict, codebase_op_dict)
                    num_differences = len(differences)
                    num_elements_op = count_keys_and_values(editor_op_dict)

                    similarity = (num_elements_op - num_differences) / num_elements_op
                    if 0.7 < similarity < 0.95:
                        op_score[op_signature] = similarity * op_freq[1]
                try:
                    best_op = max(op_score, key=op_score.get)
                    print(ops[best_op])
                    print()
                    print()

                except ValueError as e:
                    print("Error:", e)

    print("breakpoint")
