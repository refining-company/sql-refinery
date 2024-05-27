from . import codebase

# Algorithm:
# [x] Load and parse codebase
# [x] Capture all column identifiers and their respective expressions
# [ ] fix `WITH RECURSIVE date_ranges(date_day) ... ` in tree-sitter-bigquery-sql
# [ ] Resolve all column identifiers to include table name derrived from surrounding code
# [ ] Find all expressions in the SELECT clause and create a map dict{column: set{expression statement, ...}}
# [ ] Load current file and so same analysis
# [ ] In the current document go expression by expression
# [ ] Match each against other expressions in the codebase map using Levenstein distance of the SQL string
# [ ] For those that are similar compare if they are equal using database comparison
# [ ] If they don't match suggest alternatives ordered by how close the Levenstein distaince is and
#     how frequently they've been used

codebase = codebase.load(".playground/code")
