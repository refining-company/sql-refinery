"""SQL parsing with tree-sitter"""

from __future__ import annotations

from pathlib import Path

import sqlglot
import tree_sitter
import tree_sitter_sql_bigquery
from tree_sitter import Node, Tree  # noqa: F401

import src

_language = tree_sitter.Language(tree_sitter_sql_bigquery.language())
# BUG: `WITH RECURSIVE date_ranges(date_day) ...` fails in tree-sitter-bigquery-sql


# ============================================================================
# Tree Traversal
# ============================================================================


def find_desc(node: tree_sitter.Node, types: str | list[str], local: bool = True) -> list[tree_sitter.Node]:
    # TODO: migrate to Tree.walk() https://github.com/tree-sitter/py-tree-sitter/blob/master/examples/walk_tree.py
    results = []
    for child in node.named_children:
        if is_type(child, types):
            results.append(child)

        if not (local and is_type(child, types=["@scope", "@query"])):
            results += find_desc(child, types, local)

    return results


def find_asc(node: tree_sitter.Node, types: str | list[str], local: bool = True) -> tree_sitter.Node | None:
    if node.parent is None:
        return None

    if local and is_type(node, types=["@scope", "@query"]):
        return None

    if is_type(node.parent, types):
        return node.parent

    return find_asc(node.parent, types, local)


def find_alias(node: tree_sitter.Node) -> str | None:
    # BUG: `GROUP BY <expr>, <expr>` columns for expressions are duplicated
    if not is_type(node, ["@table", "@expression"]):
        return None

    if node.next_named_sibling:
        alias_node = find_desc(node.next_named_sibling, "@alias")
        if len(alias_node):
            return alias_node[0].text.decode("utf-8")  # type: ignore

    return None


# ============================================================================
# Type System
# ============================================================================


def is_type(node: tree_sitter.Node, types: str | list[str]) -> bool:
    types = [types] if isinstance(types, str) else types
    if get_type(node) in types or node.type in types:
        return True

    return False


def get_type(node: tree_sitter.Node, meta: bool = True, helper: bool = True, original: bool = True) -> str | None:
    node_type = node.type.lower()

    if node.parent is None:
        node_type = "@root"

    elif node_type == "query_expr" and node.named_children[0] and node.named_children[0].type in {"select"}:
        node_type = "@query"
    elif node_type == "query_expr":
        node_type = "@scope"

    elif node_type in {"select_list"}:
        node_type = "@columns"
    elif node_type in {"from_clause"}:
        node_type = "@sources"
    elif node_type in {"group_by_clause"}:
        node_type = "@grouping"
    elif node_type in {"where_clause"}:
        node_type = "@filter"
    elif node_type in {"order_by_clause"}:
        node_type = "@ordering"
    elif node_type in {"join_condition"}:
        node_type = "@join"

    elif node_type not in {"as_alias", "(", ")", ",", "using", "on", "identifier"} and node.parent.type in {
        "select_expression",
        "join_condition",
        "grouping_item",
        "order_by_clause_body",
    }:
        node_type = "@expression"

    elif node_type in {"function_call", "binary_expression"}:
        node_type = "#function"

    elif node_type in {"identifier", "select_all"} and node.parent.type not in {
        "from_clause",
        "from_item",
        "function_call",
        "as_alias",
        "drop_table_statement",
        "create_table_statement",
        "cte",
    }:
        node_type = "@column"

    elif node_type in {"identifier"} and node.parent.type in {"from_item", "from_clause"}:
        node_type = "@table"

    elif node_type in {"identifier"} and node.parent.type in {"as_alias"}:
        node_type = "@alias"

    elif node_type in {"number", "string"}:
        node_type = "#constant"

    # TODO: rewrite to return node_type.startswith("@") or None and drop "original"
    if node_type.startswith("@") and meta:
        return node_type
    elif node_type.startswith("#") and helper:
        return node_type
    elif original:
        return node_type

    return None


# ============================================================================
# Decoders
# ============================================================================


def decode_function(node: tree_sitter.Node) -> tuple[str, list[tree_sitter.Node]]:
    if node.type == "function_call":
        name = node.named_children[0].text.decode("utf-8").capitalize()  # type: ignore
        # taking children of the `attribute` node
        args = sum([child.named_children for child in node.named_children[1:]], [])
        return name, args

    if node.type == "binary_expression":
        name = node.children[1].text.decode("utf-8").capitalize()  # type: ignore
        args = node.named_children
        return name, args

    raise ValueError("Node type is not #function")


def decode_column(node: tree_sitter.Node) -> dict[str, str | None]:
    *_, dataset, table, column = (None, None, None) + tuple(node.text.decode("utf-8").split("."))  # type: ignore
    return {"dataset": dataset, "table": table, "column": column}


def decode_table(node: tree_sitter.Node) -> dict[str, str | None]:
    *_, dataset, table = (None, None) + tuple(node.text.decode("utf-8").split("."))  # type: ignore
    return {"dataset": dataset, "table": table}


# ============================================================================
# Debug Utilities
# ============================================================================


def to_str(obj: tree_sitter.Tree | tree_sitter.Node) -> str:
    """Get grammar name and compacted text content"""
    match obj:
        case tree_sitter.Tree():
            node = obj.root_node
        case tree_sitter.Node():
            node = obj

    text = node.text.decode("utf-8") if node.text else ""
    return f"{node.grammar_name}: {src.utils.compact_str(text, max_len=80)}"


def to_repr(obj: tree_sitter.Tree | tree_sitter.Node) -> str:
    """Get formatted representation of node"""
    match obj:
        case tree_sitter.Tree():
            node = obj.root_node
            return f"sql.Tree({node.start_point.row}:{node.start_point.column}-{node.end_point.row}:{node.end_point.column})"
        case tree_sitter.Node():
            node_type = get_type(obj, meta=True, helper=False, original=False)
            if not node_type:
                return ""
            return (
                f"sql.Node({obj.start_point.row}:{obj.start_point.column}-{obj.end_point.row}:{obj.end_point.column})"
            )


def to_struct(node: tree_sitter.Node) -> dict | list:
    """Convert node to simplified structure"""
    children = [to_struct(child) for child in node.children]
    children = [child for child in children if child]
    children = sum([child if isinstance(child, list) else [child] for child in children], [])

    node_repr = to_repr(node)
    if node_repr:
        return {f"{node_repr} = {to_str(node)}": children}
    else:
        return children


# ============================================================================
# Builder
# ============================================================================


def build(ws: src.workspace.Workspace) -> dict[Path, tree_sitter.Tree]:
    """Build tree_sitter.Tree for each SQL file"""
    parser = tree_sitter.Parser()
    parser.language = _language

    def _register(obj):
        """Recursively register tree-sitter Tree and Node objects"""
        match obj:
            case tree_sitter.Tree():
                ws.new(obj)
                _register(obj.root_node)
            case tree_sitter.Node():
                if get_type(obj, meta=True, helper=False, original=False):
                    ws.new(obj)
                for child in obj.children:
                    _register(child)
        return obj

    return {path: _register(parser.parse(content.encode())) for path, content in ws.layer_files.items()}


# ============================================================================
# Formatter
# ============================================================================


def format(sql: str) -> str:
    """Format SQL code using sqlglot"""
    parsed = sqlglot.parse_one(sql, dialect="bigquery")
    return parsed.sql(
        dialect="bigquery",
        pretty=True,
        indent=4,
        pad=4,
        max_text_width=120,
        normalize_functions="upper",
        leading_comma=False,
        comments=True,
    )
