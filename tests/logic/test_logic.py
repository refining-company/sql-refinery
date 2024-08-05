import json
import sys
import json
import hashlib
from deepdiff import DeepDiff
from pathlib import Path
from src import logic, codebase, utils


EDITOR = Path("tests/logic/editor")
CODEBASE = Path("tests/logic/input/code")
OUTPUT = Path("tests/logic/outputs.json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, list) and all(isinstance(item, logic.Suggestion) for item in obj):
        return {
            "input": {
                "\n".join(
                    "File:{}:{}:{}, End:{}".format(file, start[0], start[1], end) for file, start, end in obj[0].file
                ): obj[0].expression,
            },
            "suggestions": [simplify(suggestion) for suggestion in obj[1:]],
        }

    if isinstance(obj, logic.Suggestion):
        return {
            "\n".join("File:{}:{}:{}, End:{}".format(file, start[0], start[1], end) for file, start, end in obj.file): [
                obj.expression,
                obj.freq,
                obj.score,
            ]
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


def process_editor():
    editor = codebase.load(EDITOR)
    log = logic.Logic(CODEBASE)
    output = []

    for query in editor.queries:
        for op in query.ops:
            suggestions = [
                logic.Suggestion(
                    [
                        (
                            str(op.file),
                            (op.node.start_point.row + 1, op.node.start_point.column + 1),
                            (op.node.end_point.row + 1, op.node.end_point.column + 1),
                        )
                    ],
                    log.resolve_columns(op),
                )
            ]
            similar_ops = log.get_similar_op(op)
            suggestions.extend(similar_ops)
            output.append(suggestions)
    return output


def prep_output():
    output = process_editor()
    output = simplify(output)
    output_json = json.dumps(output, indent=2)
    output_mini = utils.json_minify(output_json)
    OUTPUT.write_text(output_mini)


def test_codebase():
    try:
        output_test = process_editor()
        output_test = simplify(output_test)
    except Exception as _:
        assert False, "Parsing of Codebase: failed"

    output_true = json.load(OUTPUT.open("r"))
    diff = DeepDiff(output_test, output_true)
    assert not diff, "Test failed with error {}".format(diff)


if __name__ == "__main__":
    if "--create-outputs" in sys.argv:
        prep_output()
        print("Outputs created.")
