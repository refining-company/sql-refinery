import re
import inspect
import pytest
from pathlib import Path
from collections import defaultdict
from functools import wraps, partial

from src import sql
from src import code
from src import logic
from src import server
import tests.utils as utils
import tests.conftest as conftest


def simplify(obj, terminal=()) -> dict | list | str | int | float | bool | None:
    # TODO: move some complexity into __repr__ and __str__ of the dataclasses

    # If the object is an instance of a terminal class, return its class name or identifier
    if isinstance(obj, terminal):
        if isinstance(obj, sql.Node):
            return simplify(obj.text, terminal)

        return f"<{obj.__class__.__name__}>"

    # Custom expansion logic for specific classes
    if isinstance(obj, logic.Alternative):
        return {
            "this": simplify(obj.this, terminal),
            "others": simplify(obj.others, terminal),
            "reliability": simplify(obj.reliability, terminal),
            "similarity": simplify(obj.similarity, terminal),
        }

    if isinstance(obj, code.Tree):
        return {
            "files": simplify(obj.files, terminal),
            "queries": simplify(obj.queries, terminal),
        }

    if isinstance(obj, code.Query):
        return {
            repr(obj): {
                "expressions": simplify(obj.expressions, terminal),
                "sources": simplify(obj.sources, terminal),
                "alias": obj.alias,
            }
        }

    if isinstance(obj, code.Expression):
        return {
            f"{repr(obj)} = {str(obj)}": {
                "columns": simplify(obj.columns, terminal),
                "alias": obj.alias,
            }
        }

    if isinstance(obj, code.Column):
        return {repr(obj): simplify(obj.nodes, terminal)}

    if isinstance(obj, code.Table):
        return {repr(obj): simplify(obj.node, terminal)}

    if isinstance(obj, sql.Tree):
        return [simplify(obj.root_node)]

    if isinstance(obj, sql.Node):
        node_type = sql.get_type(obj, meta=True, helper=False, original=False)

        children = simplify(obj.children, terminal)  # simplify recursively
        children = [child for child in children if child]  # filter out empty values # type: ignore
        children = sum([child if isinstance(child, list) else [child] for child in children], [])  # flatten the list

        if node_type:
            key = "{} ({} at {}:{}) = {}".format(
                node_type,
                obj.grammar_name,
                obj.start_point.row + 1,
                obj.start_point.column + 1,
                re.sub(r"\s+", " ", simplify(obj.text, terminal))[:20],  # type: ignore
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
        return tuple(simplify(item, terminal) for item in obj)  # type: ignore

    if isinstance(obj, Path):
        return str(obj)

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    if isinstance(obj, float):
        return round(obj, 2)

    if isinstance(obj, (str, int, bool, type(None))):
        return obj

    # Fallback for other types
    return f"<{obj.__class__.__name__}>"


def capture_snapshots(init):
    captured = defaultdict(list)

    def _intercept(target: callable, simplify: callable) -> callable:  # type: ignore
        """
        Wrapper that intercepts outputs of `target` function and translate into simple text representation
        using `simplify` to convert into basic types
        and `utils.pformat` to convert into compact JSON
        """

        @wraps(target)
        def wrapper(*args, **kwargs):
            result = target(*args, **kwargs)

            module = inspect.getmodule(target)
            key = f"{module.__name__}.{target.__name__}"  # type: ignore
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
    logic.compare = _intercept(
        logic.compare,
        simplify=partial(simplify, terminal=(sql.Node, sql.Tree, code.Tree, code.Query)),
    )

    # run the pipeline
    server.main(**init["server:main"])

    captured = {f"{k}.{i}": v[i] for k, v in captured.items() for i in range(len(v))}
    return captured


def update_snapshots(config: dict):
    print("Generating snapshots...")
    captured_snapshots = capture_snapshots(config)
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


def read_snapshots(path: Path):
    return {file.stem: file.read_text() for file in path.glob("**/*")}


def get_test_params():
    config = conftest.get_paths()
    captured = capture_snapshots(config)
    correct = read_snapshots(config["true_snapshots"])

    params = [pytest.param(key, captured, correct, id=key) for key in list(correct.keys())]
    params += [pytest.param(None, captured, correct, id="Unexpected")]

    return params


@pytest.mark.parametrize("name,captured,correct", get_test_params())
def test_pipeline(name: str, captured: dict, correct: dict):
    if name:
        assert name in captured, f"Snapshot '{name}' was not captured"
        assert correct[name] == captured[name], f"Snapshots '{name}' are different"
    else:
        extra_snapshots = set(captured) - set(correct)
        assert not extra_snapshots, f"Unexpected snapshots captured: {extra_snapshots}"
