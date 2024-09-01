import json
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

GOLDEN_MASTER_FILE = Path(__file__).with_suffix(".json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, codebase.Codebase):
        return {
            "files": [{"File:{}".format(str(file)): []} for file in obj.files.keys()],
            "queries": [simplify(query) for query in obj.queries],
        }

    if isinstance(obj, codebase.Query):
        query = {
            "Query:{}:{}:{}".format(obj.file, obj.node.start_point.row + 1, obj.node.start_point.column + 1): {
                "ops": [simplify(op) for op in obj.ops]
            }
        }
        return query

    if isinstance(obj, codebase.Table):
        return {
            "Table:{}:{}:{}".format(
                simplify(obj.dataset),
                simplify(obj.table),
                simplify(obj.alias),
            ): []
        }

    if isinstance(obj, codebase.Op):
        op = {
            "Op:{}:{}:{}:{}".format(
                obj.file,
                obj.node.start_point.row + 1,
                obj.node.start_point.column + 1,
                hashlib.sha256(json.dumps(simplify(obj.node)).encode("utf-8")).hexdigest(),
            ): [],
            "columns": [simplify(column) for column in obj.columns],
        }
        return op

    if isinstance(obj, codebase.Column):
        return "Column:{}:{}:{}".format(
            simplify(obj.dataset),
            simplify(obj.table),
            simplify(obj.column),
        )

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


def test_codebase(paths: dict[str, Path]):
    global GOLDEN_MASTER_FILE

    try:
        output = simplify(codebase.load(paths["codebase"]))
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    master = json.load(GOLDEN_MASTER_FILE.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, "Test failed with error {}".format(diff)


def update_snapshots(paths: dict[str, Path]):
    global GOLDEN_MASTER_FILE

    output = simplify(codebase.load(paths["codebase"]))
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    GOLDEN_MASTER_FILE.write_text(output_mini)
