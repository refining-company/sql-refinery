"""Abstraction layer over SQL parsing of byte strings for various dialects.

Uses tree-sitter library.

Tntroduces additional types to simplify the further processing of the parse trees across different SQL dialects.
- `@...` - meta types used for further abstraction into query tree
- `#...` - helper types
- `...` - original tree_sitter types

These additional types are implemented with hard-coded rules.
"""

import tree_sitter
import tree_sitter_sql_bigquery
from tree_sitter import Tree, Node

_language = tree_sitter.Language(tree_sitter_sql_bigquery.language())
# BUG fix `WITH RECURSIVE date_ranges(date_day) ... ` in tree-sitter-bigquery-sql


def find_desc(node: tree_sitter.Node, types: str | list[str], local: bool = True) -> list[tree_sitter.Node]:
    # TODO: migrate to Tree.walk() https://github.com/tree-sitter/py-tree-sitter/blob/master/examples/walk_tree.py
    # TODO: maybe redo with queries like
    #       (function_call function: (identifier) @ignore)
    #       (as_alias alias_name: (identifier) @ignore)
    #       (identifier) @column

    results = []
    for child in node.named_children:
        if is_type(child, types):
            results.append(child)

        # go outside of local scope
        if not (local and is_type(child, types=["@scope", "@query"])):
            results += find_desc(child, types, local)

    return results


def find_asc(node: tree_sitter.Node, types: str | list[str], local: bool = True) -> tree_sitter.Node | None:
    if node.parent is None:
        return None

    # going outside of scope
    if local and is_type(node, types=["@scope", "@query"]):
        return None

    if is_type(node.parent, types):
        return node.parent

    return find_asc(node.parent, types, local)


# BUG: `GROUP BY <expr>, <expr>` columns for expressions are duplicated (parent is the issue)
def find_alias(node: tree_sitter.Node) -> str | None:
    if not is_type(node, ["@table", "@expression"]):
        return None

    if node.next_named_sibling:
        alias_node = find_desc(node.next_named_sibling, "@alias")
        if len(alias_node):
            return alias_node[0].text.decode("utf-8")  # type: ignore

    return None


def is_type(node: tree_sitter.Node, types: str | list[str]) -> bool:
    types = [types] if isinstance(types, str) else types
    if get_type(node) in types or node.type in types:
        return True

    return False


# find 
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

    if node_type.startswith("@") and meta:
        return node_type
    elif node_type.startswith("#") and helper:
        return node_type
    elif original:
        return node_type


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

    assert False, "Node type is not #function"


def decode_column(node: tree_sitter.Node) -> dict[str, str | None]:
    *_, dataset, table, column = (None, None, None) + tuple(node.text.decode("utf-8").split("."))  # type: ignore
    return {"dataset": dataset, "table": table, "column": column}


def decode_table(node: tree_sitter.Node) -> dict[str, str | None]:
    *_, dataset, table = (None, None) + tuple(node.text.decode("utf-8").split("."))  # type: ignore
    return {"dataset": dataset, "table": table}


def parse(text: bytes) -> tree_sitter.Tree:
    parser = tree_sitter.Parser()
    parser.language = _language
    tree = parser.parse(text)
    return tree
