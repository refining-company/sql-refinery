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
        return f"ExpressionVariations({self.this._file.name}:{self.this._node.start_point.row + 1}:{self.this._node.start_point.column + 1}, {len(self.others)} variations)"


def get_variations(path: Path, tree: code.Tree, threshold: float = 0.7) -> list[ExpressionVariations]:
    """Find variation groups containing expressions from the given file."""

    # Create variations (groups of identical expressions)
    dict_expr_groups: dict[tuple[str, frozenset[str]], list[code.Expression]] = defaultdict(list)
    for exprs in tree.map_file_to_expr.values():
        for expr in exprs:
            key = (str(expr), frozenset(map(str, expr.columns)))
            dict_expr_groups[key].append(expr)
    expr_groups = [ExpressionGroup(exprs, text, cols, len(exprs)) for (text, cols), exprs in dict_expr_groups.items()]

    # Build map from expression to group (use id since Expression is not hashable)
    map_expr_to_group = {id(expr): gr for gr in expr_groups for expr in gr.expressions}

    # Build similarity map between variations
    map_group_to_other: dict[int, list[tuple[ExpressionGroup, float]]] = defaultdict(list)
    for gr1 in expr_groups:
        map_group_to_other[id(gr1)] = [(gr2, get_similarity(gr1, gr2)) for gr2 in expr_groups if gr2 != gr1]

    # Find variations related to the requested file
    file_variations: list[ExpressionVariations] = []
    for expr in tree.map_file_to_expr.get(path, []):
        gr = map_expr_to_group[id(expr)]
        other = map_group_to_other[id(gr)]
        variations = [ExpressionVariation(gr2, sim) for (gr2, sim) in other if sim >= threshold]
        if variations:
            file_variations.append(ExpressionVariations(expr, variations))

    return file_variations


def get_similarity(v1: ExpressionGroup, v2: ExpressionGroup) -> float:
    """Get distance between two variations (0.0 = identical, 1.0 = completely different)"""
    text_sim = Levenshtein.ratio(v1.repr, v2.repr)
    cols_sim = len(v1.columns & v2.columns) / len(v1.columns | v2.columns) if v1.columns | v2.columns else 1.0
    sim = text_sim * cols_sim
    return sim
