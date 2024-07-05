import pytest
import json
from src import sql
from src.tests.sql.utils import *

####  to run manually "python -m src.tests.sql.test_sql" from project directory (backend folder)
####  Tells Python to treat the directory as a package and set the appropriate context for relative imports


titles, queries = read_test_file("src/tests/sql/input.sql")
pickled_trees = json.load(open("src/tests/sql/output.json", "rb"))
encoder = TreeSitterJSONEncoder()
test_cases = zip(titles, queries, pickled_trees)


@pytest.mark.parametrize("test_name, query, target_tree", test_cases)
def test_parser(test_name, query, target_tree):
    parsed_tree = encoder.default(sql.parse(query.encode("utf-8")))
    assert parsed_tree == target_tree, "Test case: " + test_name + " failed!"
