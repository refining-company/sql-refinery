import sys
import pytest
import json
import re
from deepdiff import DeepDiff
from pathlib import Path
from src import codebase
import tree_sitter


INPUT_DIR = Path("tests/input/code")
OUTPUT = Path("tests/codebase/outputs.json")


def simplify(obj) -> dict | list | str:

    if isinstance(obj, codebase.Codebase | codebase.Query | codebase.Table | codebase.Op | codebase.Column):
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


def json_minify(string: str) -> str:
    """Minify JSON string."""
    string = re.sub(r"\{\s+(.*)\s+\}", r"{ \1 }", string)  # small one-item objects
    string = re.sub(r"(\n[ \t]*)\{\s+", r"\1{ ", string)  # hanging {
    string = re.sub(r"\s+(?=[\}\]])", " ", string)  # combine closing brackets on one line

    return string


def prep_output():

    output = simplify(codebase.load(INPUT_DIR))
    output_json = json.dumps(output, indent=2)
    output_mini = json_minify(output_json)
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
