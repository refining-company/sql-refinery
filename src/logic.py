from . import codebase
from codebase import Codebase, Column


# Algorithm:
# [x] Load and parse codebase
# [x] Capture all column identifiers and their respective expressions
# [x] Resolve all column identifiers to include table name derrived from surrounding code
# [ ] Creat `editor.sql` file that will be part of a codebase
# [ ] Create data model (data classes) for `logic.py`
# [ ] Find all expressions in the SELECT clause and create a map dict{Column dataclass: [Op dataclass, ...]}
# [ ] In the current document go expression by expression from those that are in `editor.sql`
# [ ] Match each against other expressions in the codebase map using Levenstein distance of the SQL string
# [ ] For those that are similar but not exactly equal (e.g. > .7 and <0.99)
# [ ] Suggest alternatives ordered by how close they are and how frequently they've been used

# TODO: write hacky code to make it work and output an example. this code will be 100% discarded. we'll use it to undestand
#       how to structure the actual solution.


def map_column_uses(codebase: Codebase) -> dict[Column, Op]:

    column_map = {}

    for query in codebase.queries:
        for op in query.ops:
            for column in op.columns:
                column_map.setdefault(tuple(column.dataset, column.table, column.column), []).append(op)

    return column_map


codebase = codebase.load(".submodules/playground/code")
