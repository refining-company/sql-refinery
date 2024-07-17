import sys
import pytest
import json
from deepdiff import DeepDiff
from pathlib import Path
from src import codebase
from src.codebase import Codebase, Query, Op, Table, Column
from tree_sitter import Node, Tree


INPUT_DIR = "tests/input/code"
OUTPUT_DIR = "tests/codebase/output"


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
            # "children": [self.encode_node(child) for child in node.children],
        }
        if node.type in ["identifier", "number", "string"]:
            encoded_node["text"] = node.text.decode("utf-8")
        return encoded_node

    def encode_tree(self, tree: Tree):
        encoded_tree = {"root": self.encode_node(tree.root_node)}
        return encoded_tree


def prep_output():

    codebase_tree = codebase.load(Path(INPUT_DIR))
    output_json = json.dumps(codebase_tree, cls=QueryTreeJSONEncoder, indent=2)
    output_file = Path(OUTPUT_DIR + "/codebase.json")
    output_file.write_text(output_json)


ENCODER = QueryTreeJSONEncoder()


def test_codebase():

    try:
        codebase_tree = codebase.load(Path(INPUT_DIR))
        input_dict = ENCODER.default(codebase_tree)
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    output_file = Path(OUTPUT_DIR + "/codebase.json")
    target_dict = json.load(output_file.open("r"))
    diff = DeepDiff(input_dict, target_dict)
    assert not diff, "Test failed with error {}".format(diff)


if __name__ == "__main__":
    if "--create-outputs" in sys.argv:
        prep_output()
    pytest.main()
