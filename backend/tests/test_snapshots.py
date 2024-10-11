from pathlib import Path
import re
import inspect
from collections import defaultdict
from functools import wraps, partial

from src import sql
from src import code
from src import logic
from src import server
from tests import utils


def capture_snapshots(init):
    captured = defaultdict(list)

    def _intercept(target: callable, simplify: callable) -> callable:
        """
        Wrapper that intercepts outputs of `target` function and translate into simple text representation
        using `simplify` to convert into basic types
        and `utils.pformat` to convert into compact JSON
        """

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)

            module = inspect.getmodule(target)
            key = f"{module.__name__}.{target.__name__}"
            simplified_result = utils.pformat(simplify(result))
            captured[key].append(simplified_result)

            return result

        return wrapper

    # patching functions of interest and running the pipeline
    sql.parse = _intercept(
        sql.parse,
        simplify=simplify,
    )
    code.parse = _intercept(
        code.parse,
        simplify=partial(simplify, terminal=(sql.Node, sql.Tree)),
    )
    logic.parse = _intercept(
        logic.parse,
        simplify=partial(simplify, terminal=(sql.Node, sql.Tree, code.Tree, code.Query)),
    )
    logic.compare = _intercept(
        logic.compare,
        simplify=partial(simplify, terminal=(sql.Node, sql.Tree, code.Tree, code.Query)),
    )

    # run the pipeline
    server.main(**init)

    captured = {f"{k}.{i}": v[i] for k, v in captured.items() for i in range(len(v))}
    return captured


def update_snapshots(config: dict[str, Path]):
    print("Generating snapshots...")
    captured_snapshots = capture_snapshots(config["init"])
    print("\t", "Generated")

    print("Deleting old files...")
    for file in config["true_snapshots"].glob("**/*"):
        print("\t", f"Deleted {file.name}")
        file.unlink()

    print("Writing new files...")
    for key, snapshot in captured_snapshots.items():
        snapshot_file = config["true_snapshots"] / f"{key}.json"
        snapshot_file.write_text(snapshot)
        print("\t", f"Wrote {snapshot_file.name}")

    print("Snapshots updated.")


def test_snapshots(config: dict[str, Path]):
    captured_snapshots = capture_snapshots(config["init"])

    true_snapshot_files = list(config["true_snapshots"].glob("**/*"))
    true_snapshots = {file.stem: file.read_text() for file in true_snapshot_files}

    files = true_snapshots.keys() | captured_snapshots.keys()

    for file in files:
        assert file in true_snapshots, f"Unrecognised snapshot captured: {file} is not found in true snapshots"
        assert file in captured_snapshots, f"Snapshot was not provided: {file} is not found in captured snapshots"
        assert true_snapshots[file] == captured_snapshots[file], f"Snapshots {file} are different"


def simplify(obj, terminal=()) -> dict | list | str:
    # TODO: move some complexity into __repr__ and __str__ of the dataclasses

    # If the object is an instance of a terminal class, return its class name or identifier
    if isinstance(obj, terminal):
        if isinstance(obj, sql.Node):
            return simplify(obj.text, terminal)

        return f"<{obj.__class__.__name__}>"

    # Custom expansion logic for specific classes
    if isinstance(obj, logic.Map):
        return {
            "tree": simplify(obj.tree, terminal),
            "all_queries": simplify(obj.all_queries, terminal),
            "all_expressions": simplify(obj.all_expressions, terminal),
        }

    if isinstance(obj, logic.Alternative):
        return {
            "this": simplify(obj.this, terminal),
            "others": simplify(obj.others, terminal),
            "reliability": obj.reliability,
            "similarity": round(obj.similarity, 2),
        }

    if isinstance(obj, code.Tree):
        return {
            "files": simplify(obj.files, terminal),
            "queries": simplify(obj.queries, terminal),
        }

    if isinstance(obj, code.Query):
        return {
            f"Query at {obj.file}:{obj.node.start_point.row + 1}:{obj.node.start_point.column + 1}": {
                "expressions": simplify(obj.expressions, terminal),
                "sources": simplify(obj.sources, terminal),
                "alias": obj.alias,
            }
        }

    if isinstance(obj, code.Expression):
        return {
            f"Expression at {obj.file}:{obj.node.start_point.row + 1}:{obj.node.start_point.column + 1} = {str(obj)}": {
                "columns": simplify(obj.columns, terminal),
                "alias": obj.alias,
            }
        }

    if isinstance(obj, code.Column):
        return {str(obj): simplify(obj.nodes, terminal)}

    if isinstance(obj, code.Table):
        return {str(obj): simplify(obj.node, terminal)}

    if isinstance(obj, sql.Tree):
        return [simplify(obj.root_node)]

    if isinstance(obj, sql.Node):
        node_type = sql.get_type(obj, meta=True, helper=False, original=False)

        children = simplify(obj.children, terminal)  # simplify recursively
        children = [child for child in children if child]  # filter out empty values
        children = sum([child if isinstance(child, list) else [child] for child in children], [])  # flatten the list

        if node_type:
            key = "{} ({} at {}:{}) = {}".format(
                node_type,
                obj.grammar_name,
                obj.start_point.row + 1,
                obj.start_point.column + 1,
                re.sub(r"\s+", " ", simplify(obj.text, terminal))[:20],
            )
            return {key: children}
        else:
            return children

    # Handle built-in types
    if isinstance(obj, dict):
        return {str(simplify(key, terminal)): simplify(value, terminal) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item, terminal) for item in obj]

    if isinstance(obj, tuple):
        return tuple(simplify(item, terminal) for item in obj)

    if isinstance(obj, Path):
        return str(obj)

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj

    # Fallback for other types
    return f"<{obj.__class__.__name__}>"
