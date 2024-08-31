import json
import sys
import json
from deepdiff import DeepDiff
from pathlib import Path
from src import logic, utils

GOLDEN_MASTER_FILE = Path(__file__).with_suffix(".json")


def simplify_suggestions(obj):
    return {
        "Suggestion:{}:{}:{}".format(obj.score, obj.freq, obj.expression): [
            "File:{}:{}:{}, End:{}".format(file, start[0], start[1], end)
            for suggestion in obj[1:]
            for file, start, end in suggestion.file
        ]
    }


def simplify(obj) -> dict | list | str:
    if isinstance(obj, list) and all(isinstance(item, logic.Suggestion) for item in obj):
        codebase_suggestions = {}
        if len(obj) > 1:
            codebase_suggestions = {
                "Suggestion:{}:{}:{}".format(obj[1].score, obj[1].freq, obj[1].expression): [
                    "File:{}:{}:{}, End:{}".format(file, start[0], start[1], end)
                    for suggestion in obj[1:]
                    for file, start, end in suggestion.file
                ]
            }

        return {
            "input": {
                "\n".join(
                    "File:{}:{}:{}, End:{}".format(file, start[0], start[1], end) for file, start, end in obj[0].file
                ): obj[0].expression,
            },
            "suggestions": codebase_suggestions,
        }

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


def test_logic(paths: dict[str, Path]):
    try:
        logic_ = logic.Logic(paths["codebase"])
        output = logic_.analyse(paths["editor"])
        output = simplify(output)
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    master = json.load(GOLDEN_MASTER_FILE.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, "Test failed with error {}".format(diff)


def create_masters(paths: dict[str, Path]):
    global GOLDEN_MASTER_FILE

    logic_ = logic.Logic(paths["codebase"])
    output = logic_.analyse(paths["editor"])
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    GOLDEN_MASTER_FILE.write_text(output_mini)
