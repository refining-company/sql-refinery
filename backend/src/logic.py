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
from dataclasses import dataclass, field

import Levenshtein
from src import code


@dataclass
class Alternative:
    this: code.Expression
    others: list[code.Expression]
    reliability: int
    similarity: float


def compare(this: code.Tree, that: code.Tree, threshold: float = 0.7) -> list[Alternative]:
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
