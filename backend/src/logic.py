"""Analyse code tree to find experssions with potentially flawed business logic

- Find expressions that look similar but not exact
- It is likely these expressions are alternative implementations of the same business logic
- This drives inconsistency that's hard to debug:

    ```sql
    IF revenue > 3000 THEN ... as priority
    ```

    vs

    ```sql
    IF revenue > 2500 THEN ... as priority
    ```
"""

from __future__ import annotations
from dataclasses import dataclass

from pathlib import Path

import Levenshtein
from src import code


@dataclass(frozen=True)
class Alternative:
    this: code.Expression
    others: list[code.Expression]
    reliability: int
    similarity: float

    def __repr__(self) -> str:
        return "Alternative({}:{})".format(repr(self.this), ", ".join(map(repr, self.others)))


def compare(this: Path, tree: code.Tree, threshold: float = 0.7) -> list[Alternative]:
    alternatives = []

    for this_expr in tree.map_file_to_expr[this]:
        # FIXME: calculate hash just in one place
        this_id = (str(this_expr), frozenset(map(str, this_expr.columns)))
        for that_id, that_exprs in tree.map_key_to_expr.items():
            # FIXME: explicitly skip this_expr =
            sim_exprs = Levenshtein.ratio(this_id[0], that_id[0])
            sim_cols = len(this_id[1] & that_id[1]) / len(this_id[1] | that_id[1])
            sim_total = sim_exprs * sim_cols

            if threshold < sim_total < 1:
                alternatives.append(
                    Alternative(
                        reliability=len(that_exprs),
                        similarity=sim_total,
                        this=this_expr,
                        others=that_exprs,
                    )
                )

    return alternatives
