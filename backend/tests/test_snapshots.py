from pathlib import Path
import re
import inspect
from collections import defaultdict
from functools import wraps

from src import sql
from src import utils
from src import server


def capture_snapshots(init):
    captured = defaultdict(list)

    def _capture_snapshot(fn: callable, fn_simplify: callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)

            module = inspect.getmodule(fn)
            key = f"{module.__name__}.{fn.__name__}"
            simplified_result = utils.pformat(fn_simplify(result))
            captured[key].append(simplified_result)

            return result

        return wrapper

    # patching functions of interest and running the pipeline
    sql.parse = _capture_snapshot(fn=sql.parse, fn_simplify=simplify)
    server.main(**init)

    captured = {f"{k}.{i}": v[i] for k, v in captured.items() for i in range(len(v))}
    return captured


def update_snapshots(paths: dict[str, Path]):
    captured_snapshots = capture_snapshots(paths["init"])

    for file in paths["true_snapshots"].glob("**/*"):
        file.unlink()

    for key, snapshot in captured_snapshots.items():
        snapshot_file = paths["true_snapshots"] / f"{key}.json"
        snapshot_file.write_text(snapshot)


def test_snapshots(paths: dict[str, Path]):
    captured_snapshots = capture_snapshots(paths["init"])

    true_snapshot_files = list(paths["true_snapshots"].glob("**/*"))
    true_snapshots = {file.stem: file.read_text() for file in true_snapshot_files}

    files = true_snapshots.keys() | captured_snapshots.keys()

    for file in files:
        assert file in true_snapshots, f"Unrecognised snapshot captured: {file} is not found in true snapshots"
        assert file in captured_snapshots, f"Snapshot was not provided: {file} is not found in captured snapshots"
        assert true_snapshots[file] == captured_snapshots[file], f"Snapshots are different"


def simplify(obj) -> dict | list | str:
    if isinstance(obj, sql.Tree):
        return [simplify(obj.root_node)]

    if isinstance(obj, sql.Node):
        node_type = sql.get_type(obj, meta=True, helper=False, original=False)

        children = simplify(obj.children)  # simplify recursively
        children = [child for child in children if child]  # filter out empty values
        children = sum([child if isinstance(child, list) else [child] for child in children], [])  # flatten the list

        if node_type:
            key = "{} ({} at {}:{}) = {}".format(
                node_type,
                obj.grammar_name,
                obj.start_point.row + 1,
                obj.start_point.column + 1,
                re.sub(r"\s+", " ", simplify(obj.text))[:20],
            )
            return {key: children}
        else:
            return children

    if isinstance(obj, dict):
        return {str(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    raise TypeError(f"Object of type {type(obj)} is not simplifiable")
