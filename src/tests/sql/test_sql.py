import pickle
import pytest
import json
import re
from src import sql

####  run "python -m src.tests.sql.test_sql" from project directory (backend folder)
####  Tells Python to treat the directory as a package and set the appropriate context for relative imports


def read_test_file(file_path: str):

    file = open(file_path, "r")
    text = file.read()

    title_regex = "(?<=\=\n)(.*?)(?=\n\=)"
    query_regex = "=\n([^=]+)\n-QUERYEND-"

    titles = re.findall(title_regex, text)
    queries = re.findall(query_regex, text)

    # This code assumes that the tester provides the tree himself, add trees list to return statement in that case
    """
    tree_regex = "(?<=\-QUERYEND-\n)((\n|.)*?)(?=\n\=|\Z)"
    trees = re.findall(tree_regex, text)
    """

    return titles, queries


def pickle_trees(file_path: str):

    _, queries = read_test_file(file_path)

    trees = []

    for query in queries:
        trees.append(sql.parse(query.encode("utf-8")))

    with open("src/tests/sql/output.json", "wb+") as f:
        json.dump(trees, f)


if __name__ == "__main__":

    titles, queries = read_test_file("src/tests/sql/input.sql")
    pickle_trees()
    pickled_trees = pickle.load(open("src/tests/sql/output.json", "rb"))
    test_cases = zip(titles, queries, pickled_trees)

    @pytest.mark.parametrize("test_name, query, target_tree", test_cases)
    def test_parser(test_name, query, target_tree):
        parsed_tree = sql.parse(query.encode("utf-8"))
        assert parsed_tree == target_tree, "Test case: " + test_name + " failed!"
