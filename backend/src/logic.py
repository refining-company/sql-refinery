"""
SQL Refining — Backend Component (Stage 1c: Workspace & Logic Analysis)

Architecture Overview:
1. Backend pipeline:
   a) SQL parsing (sql.py)
   b) Code AST abstraction (code.py)
   c) Workspace & logic analysis (workspace.py, logic.py)
2. LSP server (server.py) transforms pipeline outputs into LSP diagnostics and code lenses
3. VS Code frontend (frontend-vscode) visualizes and interacts with LSP features

This module provides:
- `Variation`, representing groups of similar expressions with similarity and reliability
- `compare()`, which finds expressions with potentially flawed or duplicated business logic

Analysis description:
- Find expressions that look similar but not exact; likely variations of the same business logic
- Drives diagnostics for variations such as:
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

# FIXME: Variation should be structured differentlthere should be a set of expressions that are deemed
# equivalent based on `str(expr)`
# then each has a list of close sets of expressions


@dataclass(frozen=True)
class Variation:
    this: code.Expression
    others: list[code.Expression]
    reliability: int
    similarity: float

    def __repr__(self) -> str:
        return "Variation({}:{})".format(repr(self.this), ", ".join(map(repr, self.others)))


def compare(this: Path, tree: code.Tree, threshold: float = 0.7) -> list[Variation]:
    variations = []

    for this_expr in tree.map_file_to_expr[this]:
        # FIXME: calculate hash just in one place
        this_id = (str(this_expr), frozenset(map(str, this_expr.columns)))
        for that_id, that_exprs in tree.map_key_to_expr.items():
            # FIXME: explicitly skip this_expr =
            sim_exprs = Levenshtein.ratio(this_id[0], that_id[0])
            sim_cols = len(this_id[1] & that_id[1]) / len(this_id[1] | that_id[1])
            sim_total = sim_exprs * sim_cols

            if threshold < sim_total < 1:
                variations.append(
                    Variation(
                        reliability=len(that_exprs),
                        similarity=sim_total,
                        this=this_expr,
                        others=that_exprs,
                    )
                )

    return variations
