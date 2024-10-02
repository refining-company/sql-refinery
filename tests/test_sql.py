import json
from deepdiff import DeepDiff
from pathlib import Path
from src import sql, utils
import re

"""
We will take every file in the input folder, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields)with the simplify() function. Then we'll compare it 
with benchmark that is stored in the output.json
"""

TRUE_SNAPSHOT = Path(__file__).with_suffix(".json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, sql.Tree):
        return [simplify(obj.root_node)]

    if isinstance(obj, sql.Node):
        node_type = sql.get_type(obj, meta=True, helper=False, original=False)

        children = simplify(obj.children)  # simplify recursively
        children = [child for child in children if child]  # filter out empty values
        children = sum([child if isinstance(child, list) else [child] for child in children], [])  # flatten the list

        if node_type:
            key = "{} ({} at {}:{}) = {}".format(
                node_type,
                obj.grammar_name,
                obj.start_point.row + 1,
                obj.start_point.column + 1,
                re.sub(r"\s+", " ", simplify(obj.text))[:20],
            )
            return {key: children}
        else:
            return children

    if isinstance(obj, dict):
        return {str(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    raise TypeError(f"Object of type {type(obj)} is not simplifiable")


def test_parse_files(paths: dict[str, Path]):
    global TRUE_SNAPSHOT

    try:
        output = run(paths)
    except Exception as e:
        assert False, f"Parsing failed: {e}"

    master = json.load(TRUE_SNAPSHOT.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, f"Parsing incorrect:\n{diff}"


def run(inputs):
    files = inputs["inputs"].glob("**/*.sql")
    result = {file.relative_to(inputs["inputs"]): sql.parse(file.read_bytes()) for file in files}
    return simplify(result)


def update_snapshots(paths: dict[str, Path]):
    global TRUE_SNAPSHOT
    result = utils.prettify(run(paths))
    TRUE_SNAPSHOT.write_text(result)
