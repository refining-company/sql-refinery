import json
from deepdiff import DeepDiff
from pathlib import Path
from src import sql, utils

"""
We will take every file in the input folder, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields)with the simplify() function. Then we'll compare it 
with benchmark that is stored in the output.json
"""

TRUE_SNAPSHOT = Path(__file__).with_suffix(".json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, sql.Tree):
        return {"root": [simplify(obj.root_node)]}

    if isinstance(obj, sql.Node):
        keys = [obj.grammar_name]
        # TODO: Should capture only meta types that are used by code.py later and should do so recursively
        if sql.is_type(obj, {"identifier", "string", "number"}):
            return {":".join(keys): simplify(obj.text)}
        else:
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
        output = run(paths)
    except Exception as e:
        assert False, "Parsing failed: {e}"

    master = json.load(TRUE_SNAPSHOT.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, f"Parsing incorrect:\n{diff}"


def run(inputs):
    files = inputs["codebase"].glob("**/*.sql")
    result = {str(file): sql.parse(file.read_bytes()) for file in files}
    return simplify(result)


def update_snapshots(paths: dict[str, Path]):
    global TRUE_SNAPSHOT
    result = utils.prettify(run(paths))
    TRUE_SNAPSHOT.write_text(result)
