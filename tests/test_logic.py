import json
from deepdiff import DeepDiff
from pathlib import Path
from src import session, utils, logic
from tests import test_code

TRUE_SNAPSHOT = Path(__file__).with_suffix(".json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, logic.Map):
        return {
            "tree": simplify(obj.tree),
            "all_queries": simplify(obj.all_queries),
            "all_ops": test_code.simplify(
                obj.all_ops
            ),  # BUG: all_ops has frozen set that doesn't have guaranteed order when converted to string
        }

    if isinstance(obj, logic.Alternative):
        return {
            "op": test_code.simplify(obj.op),
            "alt": test_code.simplify(obj.alt),
            "reliability": obj.reliability,
            "similarity": round(obj.similarity, 2),
        }

    if isinstance(obj, dict):
        return {simplify(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    if isinstance(obj, str):
        return obj

    return f"<{obj.__class__.__name__}>"


def test_logic(paths: dict[str, Path]):
    global TRUE_SNAPSHOT

    try:
        output = run(paths)
    except Exception as e:
        assert False, f"Parsing failed: {e}"

    master = json.load(TRUE_SNAPSHOT.open("r"))
    diff = DeepDiff(output, master)
    assert not diff, f"Parsing incorrect:\n{diff}"


def run(inputs):
    obj_session = session.Session(codebase_path=inputs["codebase"], editor_path=inputs["editor"])
    result = {
        "logic_codebase": obj_session.logic_codebase,
        "logic_editor": obj_session.logic_editor,
        "analyse_editor": obj_session.analyse_editor(),
    }
    return simplify(result)


def update_snapshots(paths: dict[str, Path]):
    global TRUE_SNAPSHOT
    result = utils.prettify(run(paths))
    TRUE_SNAPSHOT.write_text(result)
