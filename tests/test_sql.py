import pytest
import json
from src import sql
from src.tests.sql.utils import *  ### TODO: Ask ChatGPT if Google's python code rules allow this

### check how to make comments copilot fiendly (not coding perspective but business logic perspective)


####  to run manually "python -m src.tests.sql.test_sql" from project directory (backend folder)
####  Tells Python to treat the directory as a package and set the appropriate context for relative imports
####  Input.sql -> TreeSitter.Tree -> Dictionary  ?=   Dictionary <- Output.json

"""
We will take input.sql file, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields). Then we'll compare it with benchmark that is stored
in the output.json
"""

titles, queries = read_test_file("src/tests/sql/input.sql")
pickled_trees = json.load(open("src/tests/sql/output.json", "rb"))
encoder = TreeSitterJSONEncoder()
test_cases = zip(titles, queries, pickled_trees)


@pytest.mark.parametrize("test_name, query, target_tree", test_cases)
def test_parser(test_name, query, target_tree):
    parsed_tree = encoder.default(sql.parse(query.encode("utf-8")))
    assert parsed_tree == target_tree, "Test case: " + test_name + " failed!"
