import json
from deepdiff import DeepDiff
from pathlib import Path
from src import sql, utils

"""
We will take every file in the input folder, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields)with the simplify() function. Then we'll compare it 
with benchmark that is stored in the output.json
"""

GOLDEN_MASTER_FILE = Path(__file__).with_suffix(".json")


def simplify(obj) -> dict | list | str:
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


def test_parse_files(paths: dict[str, Path]):
    try:
        output = simplify(sql.parse_files(paths["codebase"]))
    except Exception as e:
        assert False, "Parsing failed: {e}"

    master = json.load(GOLDEN_MASTER_FILE.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, f"Parsing incorrect:\n{diff}"


def update_snapshots(paths: dict[str, Path]):
    global GOLDEN_MASTER_FILE

    output = simplify(sql.parse_files(paths["codebase"]))
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    GOLDEN_MASTER_FILE.write_text(output_mini)
