from pathlib import Path
from src import code, utils, sql

"""
We will take every file in the input folder, parse it with codebase.load() function and 
turn the computational query treeinto a dictionary (by using only some of the fields) with 
the simplify_codebase() function. Then we'll compare it with benchmark that is stored
in the output.json
"""

TRUE_SNAPSHOT = Path(__file__).with_suffix(".json")


def simplify(obj) -> dict | list | str:
    if isinstance(obj, code.Tree):
        return {
            "files": simplify(obj.files),
            "queries": simplify(obj.queries),
        }

    if isinstance(obj, code.Query):
        query = {
            "Query at {}:{}:{}".format(obj.file, obj.node.start_point.row + 1, obj.node.start_point.column + 1): {
                "ops": simplify(obj.expressions),
                "sources": simplify(obj.sources),
                "alias": obj.alias,
            }
        }
        return query

    if isinstance(obj, code.Expression):
        op = {
            "Op at {}:{}:{} = {}".format(
                obj.file,
                obj.node.start_point.row + 1,
                obj.node.start_point.column + 1,
                str(obj),
            ): {
                "columns": simplify(obj.columns),
                "alias": obj.alias,
            }
        }
        return op

    if isinstance(obj, sql.Node):
        return simplify(obj.text)

    if isinstance(obj, code.Column):
        return {str(obj): simplify(obj.nodes)}

    if isinstance(obj, code.Table):
        return {str(obj): simplify(obj.node)}

    if isinstance(obj, dict):
        return {str(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    return f"<{obj.__class__.__name__}>"


def test_code(paths: dict[str, Path]):
    global TRUE_SNAPSHOT
    output = run(paths)
    assert output == TRUE_SNAPSHOT.read_text()


def run(inputs):
    result = code.parse(inputs["init"]["codebase_path"])
    return utils.pformat(simplify(result))


def update_snapshots(paths: dict[str, Path]):
    global TRUE_SNAPSHOT
    result = run(paths)
    TRUE_SNAPSHOT.write_text(result)
