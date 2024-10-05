from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
import Levenshtein
from src import code


"""
We take in the the whole codebase and construct a computational query tree, we then create a mapping between columns and 
expressions that use that column, afterwards when we input an expression from the editor we search which operations in the 
codebase use the same column, then measure how similar the texts of the expressions are and based on the similarity and the 
frequency we suggest an expression from the codebase.  
"""

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


@dataclass
class Alternative:
    op: code.Op = None
    alt: list[code.Op] = None
    reliability: int = None
    similarity: float = None


@dataclass
class Map:
    tree: code.Tree = None
    all_queries: list[code.Query] = None
    all_ops: dict[tuple[str, set[str]], code.Op] = None


def parse(tree: code.Tree) -> Map:
    all_queries = get_all_queries(tree.queries)
    all_ops = get_all_ops(all_queries)

    return Map(tree=tree, all_queries=all_queries, all_ops=all_ops)


def get_all_queries(queries: list[code.Query]) -> list[code.Query]:
    nested_queries = []
    for query in queries:
        nested_queries += get_all_queries([s for s in query.sources if isinstance(s, code.Query)])
    return queries + nested_queries


def get_all_ops(queries: list[code.Query]) -> dict[tuple[str, set[str]], code.Op]:
    all_ops = defaultdict(list)
    for query in queries:
        for op in query.ops:
            op_key = (str(op), tuple(sorted(map(str, op.columns))))
            all_ops[op_key].append(op)

    return dict(all_ops)


def compare(this: Map, that: Map, threshold=0.7) -> list[Alternative]:
    alternatives = []
    for this_id, this_ops in this.all_ops.items():
        for that_id, that_ops in that.all_ops.items():
            sim_ops = Levenshtein.ratio(this_id[0], that_id[0])

            this_set = set(this_id[1])
            that_set = set(that_id[1])
            sim_cols = len(this_set & that_set) / len(this_set | that_set)
            sim_total = sim_ops * sim_cols

            if threshold < sim_total < 1:
                for op in this_ops:
                    alternatives.append(
                        Alternative(reliability=len(that_ops), similarity=sim_total, op=op, alt=that_ops)
                    )

    return alternatives
