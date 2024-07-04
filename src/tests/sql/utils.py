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
        elif hasattr(obj, "root_node") and isinstance(obj.root_node, Node):
            return self.encode_tree(obj)
        elif isinstance(obj, list):
            return [self.default(item) for item in obj]
        else:
            print(type(obj))
            return super().default(obj)

    def encode_node(self, node):
        """
        Encode a tree-sitter Node object into a JSON-serializable dictionary.
        """
        encoded_node = {
            "type": node.type,
            "text": node.text.decode(),
            "children": [self.encode_node(child) for child in node.children],
        }
        return encoded_node

    def encode_tree(self, tree):
        """
        Encode a tree-sitter Tree object into a JSON-serializable dictionary.
        """
        encoded_tree = {"root": self.encode_node(tree.root_node)}
        return encoded_tree


# TODO
# Need to access deep layers of tree-sitter API to construct Tree object out of nodes
class TreeSitterJSONDecoder(json.JSONDecoder):
    """
    Custom JSON decoder for decoding tree-sitter Node and Tree objects.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.decode_object, *args, **kwargs)

    def decode_object(self, dct):
        """
        Decode a JSON dictionary into tree-sitter Node or Tree objects.
        """
        if "type" in dct and "start" in dct and "end" in dct and "children" in dct:
            # This is a Node object
            return self.decode_node(dct)
        elif "root" in dct:
            # This is a Tree object
            return self.decode_tree(dct)
        else:
            return dct

    def decode_node(self, dct):
        """
        Decode a JSON dictionary representing a tree-sitter Node object.
        """
        type_ = dct["type"]
        start = dct["start"]
        end = dct["end"]
        children = [self.decode_object(child) for child in dct["children"]]
        # Assuming Node class exists in your tree-sitter implementation
        return Node(type_, start, end, children)

    def decode_tree(self, dct):
        """
        Decode a JSON dictionary representing a tree-sitter Tree object.
        """
        root_node = self.decode_object(dct["root"])
        # Assuming Tree class exists in your tree-sitter implementation
        return Tree(root_node)


# Under construction
def compare_trees(tree1, tree2):
    def compare_nodes(node1, node2):
        if node1.type != node2.type or node1.start_point != node2.start_point or node1.end_point != node2.end_point:
            return False
        if node1.child_count != node2.child_count:
            return False
        for i in range(node1.child_count):
            if not compare_nodes(node1.child(i), node2.child(i)):
                return False
        return True

    root1 = tree1.root_node
    root2 = tree2.root_node
    return compare_nodes(root1, root2)


def read_test_file(file_path: str):
    """
    Extract Test names and queries from input.sql file
    """

    file = open(file_path, "r")
    text = file.read()

    title_regex = "(?<=--Test:).*(?=\n)"
    query_regex = "(?<=--Query:)(.*?)(?=--Test:|\Z)"

    titles = re.findall(title_regex, text)
    queries = re.findall(query_regex, text, re.DOTALL)

    # The code below assumes that the tester provides the tree himself
    # Add trees list to return statement and change query_regex to end with --Tree in that case
    """
    tree_regex = "(?<=\--Tree:\n)((\n|.)*?)(?=--Test:|\Z)"
    trees = re.findall(tree_regex, text)
    """

    return titles, queries


def save_trees(file_path: str):
    """
    Save the encoded trees in
    """

    _, queries = read_test_file(file_path)

    trees = [sql.parse(query.encode("utf-8")) for query in queries]
    encoded_trees = json.dumps(trees, cls=TreeSitterJSONEncoder)

    with open("src/tests/sql/output.json", "wb+") as f:
        f.write(encoded_trees.encode("utf-8"))


# save_trees("src/tests/sql/input.sql")
