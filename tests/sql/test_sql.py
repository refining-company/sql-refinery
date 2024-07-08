import pytest
import json
import os
import logging
from src import sql
from tests.utils.utils import TreeSitterJSONEncoder, read_test_file


# TODO dissable pytest input logging

### check how to make comments copilot fiendly (not coding perspective but business logic perspective)

####  to run manually "python -m tests.sql.test_sql" from project directory (backend folder)
####  Tells Python to treat the directory as a package and set the appropriate context for relative imports

"""
We will take input.sql file, parse it with sql.parse() function and turn the parse tree
into a dictionary (by using only some of the fields). Then we'll compare it with benchmark that is stored
in the output.json
"""

output_dir = "tests/output/code"
input_dir = "tests/input/code"
encoder = TreeSitterJSONEncoder()

test_file = []
titles = []
queries = []
pickled_trees = []


for root, _, files in os.walk(input_dir):
    for file in files:

        input_file_path = os.path.join(root, file)
        output_file_name = file[:-4] + ".json"
        output_file_path = os.path.join(output_dir, output_file_name)

        current_titles, current_queries = read_test_file(input_file_path)
        current_pickled_trees = json.load(open(output_file_path, "rb"))
        current_test_file = [file for _ in range(len(current_titles))]

        test_file.extend(current_test_file)
        titles.extend(current_titles)
        queries.extend(current_queries)
        pickled_trees.extend(current_pickled_trees)


test_cases = zip(test_file, titles, queries, pickled_trees)


@pytest.mark.parametrize("test_file, test_name, query, target_tree", test_cases)
def test_parser(test_file, test_name, query, target_tree):

    parsed_tree = encoder.default(sql.parse(query.encode("utf-8")))
    assert parsed_tree == target_tree, "Test case: " + test_name + " in file " + test_file + " failed!"
