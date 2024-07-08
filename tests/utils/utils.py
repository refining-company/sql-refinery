import os
import json
import re
from src import sql
from tree_sitter import Node, Tree


class TreeSitterJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder for tree-sitter Tree objects.
    """

    def __init__(self, **kwargs):
        super(TreeSitterJSONEncoder, self).__init__(**kwargs)

    def default(self, obj):
        """
        Override the default method to handle tree-sitter Node, Tree and list of Trees objects.
        """
        if isinstance(obj, bytes):
            return obj.decode()
        elif isinstance(obj, Node):
            return self.encode_node(obj)
        elif isinstance(obj, Tree):
            return self.encode_tree(obj)
        else:
            return super().default(obj)

    def encode_node(self, node: Node):
        """
        Encode a tree-sitter Node object into a JSON-serializable dictionary.
        """
        encoded_node = {
            "type": node.type,
            "text": node.text.decode(),
            "children": [self.encode_node(child) for child in node.children],
        }
        return encoded_node

    def encode_tree(self, tree: Tree):
        """
        Encode a tree-sitter Tree object into a JSON-serializable dictionary.
        """
        encoded_tree = {"root": self.encode_node(tree.root_node)}
        return encoded_tree


## TODO fix this so the --query comment is not neccessary, do line by line regex
def read_test_file(file_path: str):
    """
    Extract Test names and queries from input.sql file
    """

    title_regex = "(?<=--Test:).*"
    title_pattern = re.compile(title_regex)
    titles = []
    queries = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    extracting = False
    current_query_lines = []

    for line in lines:
        # Reading the query
        if not title_pattern.search(line) and extracting:
            current_query_lines.append(line)

        # Starting to read a new query
        if title_pattern.search(line) and extracting:
            titles.append(line)
            query = "".join(current_query_lines)
            queries.append(query)
            current_query_lines = []

        # Starting to read the first query
        if title_pattern.search(line) and not extracting:
            titles.append(line)
            extracting = True

    last_query = "".join(current_query_lines)
    queries.append(last_query)

    return titles, queries


def save_trees(file_path: str):
    """
    Save the encoded trees in
    """

    output_dir = "tests/output/code"
    _, file_name = os.path.split(file_path)
    # Replace the .sql suffix with .json
    file_name = file_name[:-4] + ".json"
    output_file = os.path.join(output_dir, file_name)

    _, queries = read_test_file(file_path)

    trees = [sql.parse(query.encode("utf-8")) for query in queries]
    encoded_trees = json.dumps(trees, cls=TreeSitterJSONEncoder)

    with open(output_file, "wb+") as f:
        f.write(encoded_trees.encode("utf-8"))


for root, _, files in os.walk("tests/input/code"):
    for file in files:
        file_path = os.path.join(root, file)
        save_trees(file_path)
