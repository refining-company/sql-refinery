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


@dataclass
class Alternative:
    this: code.Expression = None
    others: list[code.Expression] = None
    reliability: int = None
    similarity: float = None


@dataclass
class Map:
    tree: code.Tree = None
    all_queries: list[code.Query] = None
    all_expressions: dict[tuple[str, set[str]], code.Expression] = None


def parse(tree: code.Tree) -> Map:
    all_queries = get_all_queries(tree.queries)
    all_expressions = get_all_expressions(all_queries)

    return Map(tree=tree, all_queries=all_queries, all_expressions=all_expressions)


def get_all_queries(queries: list[code.Query]) -> list[code.Query]:
    nested_queries = []
    for query in queries:
        nested_queries += get_all_queries([s for s in query.sources if isinstance(s, code.Query)])
    return queries + nested_queries


def get_all_expressions(queries: list[code.Query]) -> dict[tuple[str, set[str]], code.Expression]:
    all_expressions = defaultdict(list)
    for query in queries:
        for expression in query.expressions:
            op_key = (str(expression), tuple(sorted(map(str, expression.columns))))
            all_expressions[op_key].append(expression)

    return dict(all_expressions)


def compare(this: Map, that: Map, threshold=0.7) -> list[Alternative]:
    alternatives = []
    for this_id, this_exprs in this.all_expressions.items():
        for that_id, that_exprs in that.all_expressions.items():
            sim_exprs = Levenshtein.ratio(this_id[0], that_id[0])

            this_set = set(this_id[1])
            that_set = set(that_id[1])
            sim_cols = len(this_set & that_set) / len(this_set | that_set)
            sim_total = sim_exprs * sim_cols

            if threshold < sim_total < 1:
                for expr in this_exprs:
                    alternatives.append(
                        Alternative(
                            reliability=len(that_exprs),
                            similarity=sim_total,
                            this=expr,
                            others=that_exprs,
                        )
                    )

    return alternatives
