import json, re, sys
import tree_sitter
from src import sql
from deepdiff import DeepDiff
from pathlib import Path


"""
We will take input.sql file, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields). Then we'll compare it with benchmark that is stored
in the output.json
"""

INPUTS = Path("tests/input/code")
OUTPUT = Path("tests/sql/output.json")


def simplify(obj) -> dict | list | str:
    """Transform into standard JSON serialisable objects."""
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
    output = simplify(sql.parse_files(INPUTS))
    output_json = json.dumps(output, indent=2)
    output_mini = json_minify(output_json)
    OUTPUT.write_text(output_mini)


def test_parse_files():
    try:
        output_test = simplify(sql.parse_files(INPUTS))
    except Exception as e:
        assert False, "Parsing failed: {e}"

    output_true = json.load(OUTPUT.open("r"))
    diff = DeepDiff(output_test, output_true, ignore_order=True)
    assert not diff, f"Parsing incorrect:\n{diff}"


if __name__ == "__main__":
    if "--create-outputs" in sys.argv:
        prep_output()
        print("Outputs created.")
