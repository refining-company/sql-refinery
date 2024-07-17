import json
import sys
import pytest
from deepdiff import DeepDiff
from pathlib import Path
from src import sql
from tree_sitter import Node, Tree

"""
We will take input.sql file, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields). Then we'll compare it with benchmark that is stored
in the output.json
"""

INPUT_DIR = Path("tests/input/code")
OUTPUT_DIR = Path("tests/sql/output")


class TreeSitterJSONEncoder(json.JSONEncoder):

    def __init__(self, **kwargs):
        super(TreeSitterJSONEncoder, self).__init__(**kwargs)

    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode()
        elif isinstance(obj, Node):
            return self.encode_node(obj)
        elif isinstance(obj, Tree):
            return self.encode_tree(obj)
        else:
            return super().default(obj)

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


def prep_output():

    for file, tree in sql.parse_files(INPUT_DIR).items():
        output_json = json.dumps(tree, cls=TreeSitterJSONEncoder, indent=2)
        output_file = Path(OUTPUT_DIR) / (file.stem + ".json")
        output_file.write_text(output_json)


ENCODER = TreeSitterJSONEncoder()


def test_parser():
    for file, tree in sql.parse_files(INPUT_DIR).items():
        try:
            input_dict = ENCODER.default(tree)
        except Exception as _:
            assert False, "Parsing of {}: failed ".format(file)

        output_file = Path(OUTPUT_DIR) / (file.stem + ".json")
        target_dict = json.load(output_file.open("r"))
        diff = DeepDiff(input_dict, target_dict)
        assert not diff, "Test {}: failed with error {}".format(file, diff)


if __name__ == "__main__":

    if "--create-outputs" in sys.argv:
        prep_output()
    test_parser()
