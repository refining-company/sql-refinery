"""
SQL Refining — Variations Analysis

Finds groups of similar SQL expressions across the codebase.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import Levenshtein

from src import code, model


@dataclass(frozen=True)
class ExpressionVariation:
    """A variation with its similarity score"""

    group: model.Expression
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


def build(semantics: model.Semantics, threshold: float = 0.7) -> dict[Path, list[ExpressionVariations]]:
    """Compute variations using semantic model, organized by file with code expressions"""
    result: defaultdict[Path, list[ExpressionVariations]] = defaultdict(list)

    for code_expr, semantic_expr in semantics.expr_code_to_model.items():
        variations = [
            ExpressionVariation(other_semantic, sim)
            for other_semantic in semantics.expressions
            if other_semantic != semantic_expr
            and threshold <= (sim := get_similarity(semantic_expr, other_semantic)) < 1.0
        ]

        if variations:
            result[code_expr.location.file].append(ExpressionVariations(code_expr, variations))

    return dict(result)


def get_similarity(v1: model.Expression, v2: model.Expression) -> float:
    """Get similarity between two expressions (0.0 = completely different, 1.0 = identical)"""
    # TODO: replace with MinHash after sql normalisation by tree-sitter combined with column resolution
    text_sim = Levenshtein.ratio(v1.canonical, v2.canonical)
    cols_sim = len(v1.columns & v2.columns) / len(v1.columns | v2.columns) if v1.columns | v2.columns else 1.0
    return text_sim * cols_sim
