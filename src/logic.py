from pathlib import Path
import json
import tree_sitter
from deepdiff import DeepDiff
from src.sql import Tree, Node
from src.codebase import Codebase, Column, Op, Table, Column, Query, load

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


def get_op_signature(op):

    # only gets the structure of the node not the identifiers of the leaf nodes since the column aliases re not resolved in the tree-sitter level
    def get_node_signature(node):
        node_signature = [node.type]
        [node_signature.append(get_node_signature(child)) for child in node.children]
        return ":".join(node_signature)

    column_strings = [":".join([str(col.dataset), str(col.table), str(col.column)]) for col in op.columns]
    columns_resolved = ":".join(column_strings)

    return ":".join([get_node_signature(op.node), columns_resolved])


def map_column_uses(codebase: Codebase) -> dict[Column, Op]:
    column_map = {}

    for query in codebase.queries:
        for op in query.ops:
            for column in op.columns:

                col_resolved = (column.dataset, column.table, column.column)
                column_map.setdefault(col_resolved, {})
                column_map[col_resolved].setdefault(get_op_signature(op), [op, 0])
                column_map[col_resolved][get_op_signature(op)][1] += 1
    return column_map


codebase = load("tests/input/code")
COLUMN_OP_MAPPING = map_column_uses(codebase)


def simplify(obj) -> dict | list | str:
    if isinstance(obj, Codebase | Query | Table | Op | Column):
        keys = list(obj.__dataclass_fields__.keys())
        return {
            ":".join(keys): [
                simplify(getattr(obj, field_name)) for field_name, field_info in obj.__dataclass_fields__.items()
            ]
        }

    if isinstance(obj, tree_sitter.Tree):
        return {"root": [simplify(obj.root_node)]}

    if isinstance(obj, tree_sitter.Node):
        keys = [obj.grammar_name]
        if obj.type in ("identifier", "number", "string"):
            keys.append(obj.text.decode("utf-8"))
        return {":".join(keys): [simplify(child) for child in obj.children]}

    if isinstance(obj, dict):
        return {str(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    try:
        return str(obj)
    except Exception as e:
        raise TypeError(f"Object of type {type(obj)} is not simplifiable: {e}")


def count_keys_values(d):
    def count_recursive(d):
        keys_count = 0
        values_count = 0
        if isinstance(d, dict):
            for key, value in d.items():
                keys_count += 1
                values_count += 1
                if isinstance(value, dict):
                    sub_keys, sub_values = count_recursive(value)
                    keys_count += sub_keys
                    values_count += sub_values
                elif isinstance(value, list):
                    values_count += len(value)
        return keys_count + values_count

    return count_recursive(d)


# mapping {column -> [ops, ...]}
# [column1->{op.signature:[op,freq]}, column2->, ...]
# you're now looking into editor_op[0]. it uses column3 and column4.
# you check mappping and retrieve only ops for column3 and column4.


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


def get_similar_op(op: Op):
    print("OP", op.node.text[:].decode())
    print("\n")
    for col in op.columns:
        codebase_ops = COLUMN_OP_MAPPING[(col.dataset, col.table, col.column)]
        op_score = {}

        for op_signature, (codebase_op, freq) in codebase_ops.items():
            op_dict = simplify(op)
            codebase_op_dict = simplify(codebase_op)
            differences = DeepDiff(op_dict, codebase_op_dict)
            num_tok = count_keys_values(op_dict)
            similarity = 1 - (len(differences) / num_tok)
            if similarity != 1:
                op_score[op_signature] = (codebase_op, similarity * freq)

        try:
            for op_signature, (codebase_op, score) in op_score.items():

                print(codebase_op.node.text[:].decode("utf-8") + "\n")
                print("Score: {}\n".format(score))
                print("\n")
                print("\n")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":

    editor = load("src/editor")

    for query in editor.queries:
        print("QUERY", query.node.text[:100])
        for op in query.ops:
            get_similar_op(op)

    print("breakpoint")
