from tree_sitter import Language, Parser, Tree, Node
import tree_sitter_sql_bigquery

__all__ = ["parse", "find", "Tree", "Node"]


def find(node: Tree | Node, type: str | list[str], deep: bool = False) -> list[Node]:
    if isinstance(node, Tree):
        return find(node.root_node, type, deep)
    if isinstance(type, str):
        type = [type]

    print(node.type)

    results = []
    for child in node.children:
        if child.type in type:
            results.append(child)

        if child.type not in {"select", "subquery"} or deep:
            results += find(child, type, deep)

    return results


language = Language(tree_sitter_sql_bigquery.language(), "sql-bigquery")
parser = Parser()
parser.set_language(language)
parse = parser.parse
