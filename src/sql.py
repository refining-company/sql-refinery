from pathlib import Path
from tree_sitter import Language, Parser, Tree, Node
import tree_sitter_sql_bigquery

__all__ = ["Tree", "Node"]

language = Language(tree_sitter_sql_bigquery.language())
# BUG fix `WITH RECURSIVE date_ranges(date_day) ... ` in tree-sitter-bigquery-sql


def find_desc(node: Node, types: str | list[str], local: bool = True) -> list[Node]:
    """Find descendants"""
    # TODO: migrate to Tree.walk() https://github.com/tree-sitter/py-tree-sitter/blob/master/examples/walk_tree.py
    # TODO: maybe redo with queries like
    #       (function_call function: (identifier) @ignore)
    #       (as_alias alias_name: (identifier) @ignore)
    #       (identifier) @column

    results = []
    for child in node.named_children:
        if is_type(child, types):
            results.append(child)

        # go outside of scope
        if local and is_type(child, types="@scope"):
            continue

        results += find_desc(child, types, local)

    return results


def find_asc(node: Node, types: str | list[str], local: bool = True) -> Node:
    """Find first matching ascendant"""
    if node.parent is None:
        return None

    # going outside of scope
    if local and is_type(node, types="@scope"):
        return None

    if is_type(node.parent, types):
        return node.parent

    return find_asc(node.parent, types, local)


def find_alias(node: Node) -> str:
    """Find alias name"""
    if not is_type(node, ["@table", "@expression"]):
        return None

    if node.next_named_sibling:
        alias_node = find_desc(node.next_named_sibling, "@alias")
        if len(alias_node):
            return alias_node[0].text

    return None


def is_type(node: Node, types: str | list[str]) -> bool:
    """Check node type against tree-sitter types and meta types"""
    types = [types] if isinstance(types, str) else types

    for _type in types:
        # meta types
        if (_type == "@scope") and node.type in {"query_expr"}:
            return True

        if (_type == "@query") and node.type in {"query_expr"} and node.named_child(0).type in {"select"}:
            return True

        # BUG: `USING (account_id, date_month)` is captured incorrectly
        if (_type == "@table") and (node.type == "identifier" and node.parent.type in {"from_item"}):
            return True

        # BUG: `USING (account_id, date_month)` is captured incorrectly
        if (
            (_type == "@expression")
            and node.type not in {"as_alias", "(", ")"}
            # using group_by_clause causes both columns to appear in both grouping_items
            and node.parent.type in {"select_expression", "join_condition", "grouping_item", "order_by_clause_body"}
        ):
            return True

        if (_type == "@column") and (
            node.type in ["identifier", "select_all"]
            and node.parent.type
            not in {
                "from_item",
                "function_call",
                "as_alias",
                "drop_table_statement",
                "create_table_statement",
                "cte",
            }
        ):
            return True

        if (_type == "@alias") and (node.type == "identifier" and node.parent.type == "as_alias"):
            return True

        # tree-sitter grammar type
        if node.type == _type:
            return True

    return False


def get_column_path(node: Node) -> dict[str, str, str]:
    """Parse column from `<database>.<table>.<column>` into dictionary"""
    *_, dataset, table, column = (None, None, None) + tuple(node.text.split(b"."))
    return {"dataset": dataset, "table": table, "column": column}


def get_table_path(node: Node) -> dict[str, str]:
    """Parse column from `<database>.<table>.<column>` into dictionary"""
    *_, dataset, table = (None, None) + tuple(node.text.split(b"."))
    return {"dataset": dataset, "table": table}


def parse(text: bytes) -> Tree:
    parser = Parser()
    parser.language = language
    tree = parser.parse(text)
    return tree


def parse_files(path: str) -> dict[Path, Tree]:
    """Load all sql files from `path` into dict `{<file Path>: <sql tree>, ...}`"""
    root = Path(path)
    paths = list(root.glob("**/*.sql"))
    files = {f.relative_to(root): parse(f.read_bytes()) for f in paths}

    return files


### HELPERS


def pprint(node: Tree):
    """Pretty print objects in this module"""
    print(to_str(node))


def to_str(node: Tree, indent: str = 0) -> str:
    res = " " * indent + "(" + str(node.type)
    if hasattr(node, "children"):
        for child in node.children:
            res += "\n" + to_str(child, indent + 2)
    res += ")"
    return res



def simplify(obj) -> dict | list | str:
    """Transform into standard JSON serialisable objects."""
    if isinstance(obj, tree_sitter.Tree):
        return {"root": [simplify(obj.root_node)]}

    if isinstance(obj, tree_sitter.Node):
        keys = [obj.grammar_name]
        if obj.type in ("identifier", "number", "string"):
            keys.append(obj.text.decode("utf-8"))
        return {":".join(keys): [simplify(child) for child in obj.children]}

    if isinstance(obj, dict):
        return {str(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    try:
        return str(obj)
    except Exception as e:
        raise TypeError(f"Object of type {type(obj)} is not simplifiable: {e}")