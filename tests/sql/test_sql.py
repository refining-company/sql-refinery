import json
import sys
from deepdiff import DeepDiff
from pathlib import Path
from src import sql, utils

"""
We will take every file in the input folder, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields)with the simplify() function. Then we'll compare it 
with benchmark that is stored in the output.json
"""

INPUTS = Path("tests/input/code")
OUTPUT = Path("tests/sql/output.json")


def prep_output():
    output = utils.simplify(sql.parse_files(INPUTS))
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    OUTPUT.write_text(output_mini)


def test_parse_files():
    try:
        output_test = utils.simplify(sql.parse_files(INPUTS))
    except Exception as e:
        assert False, "Parsing failed: {e}"

    output_true = json.load(OUTPUT.open("r"))
    diff = DeepDiff(output_test, output_true)
    assert not diff, f"Parsing incorrect:\n{diff}"


if __name__ == "__main__":
    if "--create-outputs" in sys.argv:
        prep_output()
        print("Outputs created.")
