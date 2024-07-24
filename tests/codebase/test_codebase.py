import json
import sys
import pytest
from deepdiff import DeepDiff
from pathlib import Path
from src import codebase, utils


"""
We will take every file in the input folder, parse it with codebase.load() function and 
turn the computational query treeinto a dictionary (by using only some of the fields) with 
the simplify_codebase() function. Then we'll compare it with benchmark that is stored
in the output.json
"""

INPUT_DIR = Path("tests/input/code")
OUTPUT = Path("tests/codebase/outputs.json")


def prep_output():
    output = utils.simplify_codebase(codebase.load(INPUT_DIR))
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    OUTPUT.write_text(output_mini)


def test_codebase():
    try:
        output_test = utils.simplify_codebase(codebase.load(INPUT_DIR))
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    output_true = json.load(OUTPUT.open("r"))
    diff = DeepDiff(output_test, output_true)
    assert not diff, "Test failed with error {}".format(diff)


if __name__ == "__main__":
    if "--create-outputs" in sys.argv:
        prep_output()
        print("Outputs created.")
