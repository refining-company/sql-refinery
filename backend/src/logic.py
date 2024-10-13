from __future__ import annotations
from dataclasses import dataclass

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
