"""
Shared Test Utilities

Common functions for LSP session testing and snapshot management.
"""

import dataclasses
from pathlib import Path

import attr
from lsprotocol import converters

import src


def simplify_workspace(obj, terminal=()) -> dict | list | tuple | str | int | float | bool | None:
    """Simplify complex objects for workspace snapshot comparison"""
    # Check terminal first for dataclasses, LSP types, and tree-sitter
    if isinstance(obj, terminal):
        match obj:
            case _ if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
                return repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            case src.sql.Tree() | src.sql.Node():
                return f"{src.sql.to_repr(obj)} = {src.sql.to_str(obj)}"
            case Path():
                return src.utils.trunk_path(str(obj))
            case _:
                return str(obj)

    match obj:
        # Dataclasses
        case _ if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
            obj_key = repr(obj) + (f" = {str(obj)}" if "__str__" in type(obj).__dict__ else "")
            obj_dict = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
            return {obj_key: simplify_workspace(obj_dict, terminal)}

        # LSP types (attrs-based, convert to dict and recurse)
        case _ if attr.has(type(obj)):
            return simplify_workspace(attr.asdict(obj, recurse=False), terminal)

        # Tree-sitter objects
        case src.sql.Tree():
            return [simplify_workspace(obj.root_node, terminal)]

        case src.sql.Node():
            return src.sql.to_struct(obj)

        # Built-in nested types
        case dict():
            return {
                simplify_workspace(k, (type(k))): simplify_workspace(v, terminal)
                for k, v in sorted(obj.items(), key=str)
            }
        case list() | set() | frozenset():
            items = [simplify_workspace(item, terminal) for item in obj]
            return sorted([item for item in items if item != []], key=str)
        case tuple():
            return tuple(simplify_workspace(item, terminal) for item in obj)
        case Path():
            return simplify_workspace(str(obj), terminal)
        case bytes():
            return obj.decode("utf-8")
        case float():
            return round(obj, 2)
        case str():
            return src.utils.trunk_path(obj)
        case int() | bool() | None:
            return obj
        case type():
            return f"<{obj.__name__}>"
        case _:
            return str(obj)


def capture_server(data, direction: str) -> dict:
    """Capture LSP message with direction"""
    data_dict = converters.get_converter().unstructure(data)
    return {"direction": direction, "data": data_dict}


def capture_workspace(ws: src.workspace.Workspace) -> dict[str, str]:
    always = (
        src.sql.Tree,
        src.sql.Node,
        src.code.Range,
        src.code.Location,
        src.code.Column,
        src.code.Table,
        src.code.Expression,
        src.model.Column,
        src.model.Expression,
        src.model.Table,
    )
    return {
        "workspace.layer_folder": src.utils.pformat(simplify_workspace(ws.layer_folder)),
        "workspace.layer_files": src.utils.pformat(simplify_workspace(ws.layer_files)),
        "workspace.layer_sql": src.utils.pformat(simplify_workspace(ws.layer_sql)),
        "workspace.layer_code": src.utils.pformat(simplify_workspace(ws.layer_code, terminal=always)),
        "workspace.layer_model": src.utils.pformat(simplify_workspace(ws.layer_model, terminal=always)),
        "workspace.layer_variations": src.utils.pformat(
            simplify_workspace(ws.layer_variations, terminal=(*always, src.variations.ExpressionVariation))
        ),
        "workspace._index": src.utils.pformat(
            simplify_workspace(
                ws._index,
                terminal=(
                    *always,
                    src.code.Query,
                    src.variations.ExpressionVariation,
                    src.variations.ExpressionVariations,
                ),
            )
        ),
        "workspace._map": src.utils.pformat(simplify_workspace(ws._map, terminal=always)),
    }


def format_workspace(captures: list[dict[str, str]]) -> dict[str, str]:
    """Level 1: Flatten list of capture dicts into indexed flat dict"""
    return {f"{prefix}.{i}": content for i, capture in enumerate(captures) for prefix, content in capture.items()}


def format_server(captures: list[dict[str, str]]) -> dict[str, str]:
    """Level 2: Aggregate all exchange captures into single JSON file"""
    formatted = {f"{i:03d}": src._recorder.simplify_server(item) for i, item in enumerate(captures)}
    return {"server": src.utils.pformat(formatted)}


def write_snapshots(snapshots: dict[str, str], target_dir: Path, suffix: str) -> dict[str, Path]:
    """Write snapshots to {filename}.{suffix} files"""
    target_dir.mkdir(parents=True, exist_ok=True)
    files = {}
    for filename, content in snapshots.items():
        file = target_dir / f"{filename}.{suffix}"
        file.write_text(content)
        files[filename] = file
    return files
