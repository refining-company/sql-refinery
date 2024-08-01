import json
import sys
import json
import dataclasses
import hashlib
from deepdiff import DeepDiff
from pathlib import Path
from src import codebase, utils, sql


"""
We will take every file in the input folder, parse it with codebase.load() function and 
turn the computational query treeinto a dictionary (by using only some of the fields) with 
the simplify_codebase() function. Then we'll compare it with benchmark that is stored
in the output.json
"""

INPUT_DIR = Path("tests/input/code")
OUTPUT = Path("tests/codebase/outputs.json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, codebase.Codebase):
        return {
            "files": [
                {"file:{}:{}".format(str(file), utils.node_preview(tree.root_node)): []}
                for file, tree in obj.files.items()
            ],
            "queries": [simplify(query) for query in obj.queries],
        }

    if isinstance(obj, codebase.Query):
        query = {
            "File:{}:{}:{} Expression:{}".format(
                obj.file, obj.node.start_point.row, obj.node.start_point.column, utils.node_preview(obj.node)
            ): {
                "columns": list(set([simplify(column) for op in obj.ops for column in op.columns])),
                "ops": [simplify(op) for op in obj.ops],
            }
        }
        return query

    if isinstance(obj, codebase.Table):
        return {"Table:{}:{}:{}:{}".format(obj.dataset, obj.table, obj.alias, utils.node_preview(obj.node)): []}

    if isinstance(obj, codebase.Op):
        op = {
            "File:{}:{}:{} Expression:{}:{}".format(
                obj.file,
                obj.node.start_point.row,
                obj.node.start_point.column,
                utils.node_preview(obj.node),
                hashlib.sha256(json.dumps(simplify(obj.node)).encode("utf-8")).hexdigest(),
            ): [],
            "columns": [simplify(column) for column in obj.columns],
        }
        return op

    if isinstance(obj, codebase.Column):
        return "{}:{}:{}".format(obj.dataset, obj.table, obj.column)

    if isinstance(obj, sql.Tree):
        return {"root": [simplify(obj.root_node)]}

    if isinstance(obj, sql.Node):
        keys = [obj.grammar_name]
        if obj.type in ("identifier", "number", "string"):
            return {":".join(keys): obj.text.decode("utf-8")}
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


def prep_output():
    output = simplify(codebase.load(INPUT_DIR))
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    OUTPUT.write_text(output_mini)


def test_codebase():
    try:
        output_test = simplify(codebase.load(INPUT_DIR))
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    output_true = json.load(OUTPUT.open("r"))
    diff = DeepDiff(output_test, output_true)
    assert not diff, "Test failed with error {}".format(diff)


if __name__ == "__main__":
    if "--create-outputs" in sys.argv:
        prep_output()
        print("Outputs created.")
