"""
SQL Refining — Variations Analysis

Finds groups of similar SQL expressions across the codebase.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import Levenshtein

from src import code


@dataclass(frozen=True)
class ExpressionGroup:
    """A group of identical expressions"""

    expressions: list[code.Expression]
    repr: str
    columns: frozenset[str]
    reliability: int

    def __repr__(self) -> str:
        return f"ExpressionGroup(reliability={self.reliability}, {", ".join(repr(expr) for expr in self.expressions)})"


@dataclass(frozen=True)
class ExpressionVariation:
    """A variation with its similarity score"""

    group: ExpressionGroup
    similarity: float

    def __repr__(self) -> str:
        return f"ExpressionVariation(group={self.group}, similarity={self.similarity:.2f})"


@dataclass(frozen=True)
class ExpressionVariations:
    """All variations for a specific expression"""

    this: code.Expression
    others: list[ExpressionVariation]

    def __repr__(self) -> str:
        return f"ExpressionVariations({self.this.location.file.name}:{self.this._node.start_point.row + 1}:{self.this._node.start_point.column + 1}, {len(self.others)} variations)"


def build(tree: code.Tree, threshold: float = 0.7) -> dict[Path, list[ExpressionVariations]]:
    """Compute variations for all files in the tree, return path->variations mapping."""

    # Group identical expressions
    dict_expr_groups: dict[tuple[str, frozenset[str]], list[code.Expression]] = defaultdict(list)
    for expr in tree.index[code.Expression]:
        assert type(expr) is code.Expression
        key = (str(expr), frozenset(map(str, expr.columns)))
        dict_expr_groups[key].append(expr)
    expr_groups = [ExpressionGroup(exprs, text, cols, len(exprs)) for (text, cols), exprs in dict_expr_groups.items()]

    # Build output directly - for each group, find similar groups and add to result
    result: dict[Path, list[ExpressionVariations]] = defaultdict(list)
    for gr1 in expr_groups:
        variations = [
            ExpressionVariation(gr2, sim)
            for gr2 in expr_groups
            if gr2 != gr1 and (sim := get_similarity(gr1, gr2)) >= threshold
        ]

        if variations:
            for expr in gr1.expressions:
                result[expr.location.file].append(ExpressionVariations(expr, variations))

    return dict(result)


def get_similarity(v1: ExpressionGroup, v2: ExpressionGroup) -> float:
    """Get distance between two variations (0.0 = identical, 1.0 = completely different)"""
    text_sim = Levenshtein.ratio(v1.repr, v2.repr)
    cols_sim = len(v1.columns & v2.columns) / len(v1.columns | v2.columns) if v1.columns | v2.columns else 1.0
    sim = text_sim * cols_sim
    return sim
