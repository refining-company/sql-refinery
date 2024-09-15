import json
from deepdiff import DeepDiff
from pathlib import Path
from src import code, utils, sql

"""
We will take every file in the input folder, parse it with codebase.load() function and 
turn the computational query treeinto a dictionary (by using only some of the fields) with 
the simplify_codebase() function. Then we'll compare it with benchmark that is stored
in the output.json
"""

GOLDEN_MASTER_FILE = Path(__file__).with_suffix(".json")


def test_codebase(paths: dict[str, Path]):
    global GOLDEN_MASTER_FILE

    try:
        output = code.simplify(code.load(paths["codebase"]))
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    master = json.load(GOLDEN_MASTER_FILE.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, "Test failed with error {}".format(diff)


def update_snapshots(paths: dict[str, Path]):
    global GOLDEN_MASTER_FILE

    output = code.simplify(code.load(paths["codebase"]))
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    GOLDEN_MASTER_FILE.write_text(output_mini)
