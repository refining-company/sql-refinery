from tree_sitter import Language, Parser, Tree, Node
import tree_sitter_sql_bigquery

__all__ = ["parse", "find", "Tree", "Node"]

language = Language(tree_sitter_sql_bigquery.language(), "sql-bigquery")


def find(node: Tree | Node, type: str | list[str], deep: bool = False) -> list[Node]:
    if isinstance(node, Tree):
        return find(node.root_node, type, deep)
    if isinstance(type, str):
        type = [type]

    results = []
    # TODO: migrate to Tree.walk() https://github.com/tree-sitter/py-tree-sitter/blob/master/examples/walk_tree.py
    for child in node.children:
        if child.type in type:
            results.append(child)

        if deep or child.type not in {"query_expr"}:
            results += find(child, type, deep)

    return results


def parse(text: bytes) -> Tree:
    parser = Parser()
    parser.set_language(language)
    tree = parser.parse(text)
    return tree
