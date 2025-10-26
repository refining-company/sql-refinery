"""
Pipeline — Semantic Model

Semantic abstraction over syntactic code objects with deduplication and resolution.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import src


@dataclass(frozen=True)
class Column:
    _code: list[src.code.Column]
    dataset: str | None
    table: str | None
    column: str | None

    @property
    def frequency(self) -> int:
        return len(self._code)

    def __repr__(self) -> str:
        return f"model.Column(frequency={self.frequency})"

    def __str__(self) -> str:
        return f"{self.dataset or '?'}.{self.table or '?'}.{self.column or '?'}"

    def __hash__(self) -> int:
        return hash((self.dataset, self.table, self.column))


@dataclass(frozen=True)
class Table:
    _code: list[src.code.Table]
    dataset: str | None
    table: str | None
    frequency: int

    def __repr__(self) -> str:
        return f"model.Table(frequency={self.frequency})"

    def __str__(self) -> str:
        return f"{self.dataset or '?'}.{self.table or '?'}"

    def __hash__(self) -> int:
        return hash((self.dataset, self.table))


@dataclass(frozen=True)
class Expression:
    _code: list[src.code.Expression]
    locations: list[src.code.Location]
    columns: frozenset[Column]
    frequency: int
    canonical: str
    sql: str

    def __repr__(self) -> str:
        return f"model.Expression(frequency={self.frequency})"

    def __str__(self) -> str:
        return self.canonical


@dataclass(frozen=True)
class Semantics:
    columns: list[Column]
    tables: list[Table]
    expressions: list[Expression]
    expr_code_to_model: dict[src.code.Expression, Expression]


def _resolve_columns(tree: src.code.Tree) -> dict[src.code.Column, tuple[str | None, str | None, str | None]]:
    """Resolve column references using query-scoped alias lookup"""
    resolved: dict[src.code.Column, tuple[str | None, str | None, str | None]] = {}

    for query in tree.index[src.code.Query]:
        assert isinstance(query, src.code.Query)
        alias_to_table = {
            source.alias: source for source in query.sources if isinstance(source, src.code.Table) and source.alias
        }

        for expr in query.expressions:
            for code_col in expr.columns:
                col_dataset, col_table, col_column = code_col.dataset, code_col.table, code_col.column
                if col_table and col_table in alias_to_table:
                    resolved_table = alias_to_table[col_table]
                    col_table = resolved_table.table
                    col_dataset = resolved_table.dataset or col_dataset

                resolved[code_col] = (col_dataset, col_table, col_column)

    return resolved


def _group_columns(
    tree: src.code.Tree, resolved: dict[src.code.Column, tuple[str | None, str | None, str | None]]
) -> tuple[list[Column], dict[src.code.Column, Column]]:
    """Group code.Column by (dataset, table, column) → model.Column"""
    columns_dict: defaultdict[tuple[str | None, str | None, str | None], list[src.code.Column]] = defaultdict(list)
    for code_col in tree.index[src.code.Column]:
        assert isinstance(code_col, src.code.Column)
        key = resolved[code_col]
        columns_dict[key].append(code_col)

    model_columns = [Column(_code=code, dataset=d, table=t, column=c) for (d, t, c), code in columns_dict.items()]
    code_to_model = {code_col: model_col for model_col in model_columns for code_col in model_col._code}

    return model_columns, code_to_model


def _resolve_expression(code_expr: src.code.Expression, code_to_model: dict[src.code.Column, Column]) -> str:
    """Compute resolved representation of expression using model columns"""
    # Build mapping from sql nodes to resolved model columns
    nodes_to_col: dict[src.sql.Node, Column] = {}
    for code_col in code_expr.columns:
        if code_col in code_to_model:
            nodes_to_col[code_col._node] = code_to_model[code_col]

    def node_to_str(node: src.sql.Node) -> str:
        if node in nodes_to_col:
            result = str(nodes_to_col[node])
        elif src.sql.is_type(node, "#constant"):
            result = node.text.decode("utf-8")  # type: ignore
        elif src.sql.is_type(node, "#function"):
            parsed_name, parsed_args = src.sql.decode_function(node)
            result = "{}({})".format(parsed_name, ", ".join(map(node_to_str, parsed_args)))
        else:
            result = node.type.capitalize()
            if len(node.children):
                result += "({})".format(", ".join(map(node_to_str, node.named_children)))
        return result

    return f"{node_to_str(code_expr._node)}"


def _group_tables(tree: src.code.Tree) -> list[Table]:
    """Group code.Table by (dataset, table) → model.Table"""
    tables_dict: defaultdict[tuple[str | None, str | None], list[src.code.Table]] = defaultdict(list)
    for code_table in tree.index[src.code.Table]:
        assert isinstance(code_table, src.code.Table)
        key = (code_table.dataset, code_table.table)
        tables_dict[key].append(code_table)

    return [Table(_code=code, dataset=d, table=t, frequency=len(code)) for (d, t), code in tables_dict.items()]


def _group_expressions(tree: src.code.Tree, column_code_to_model: dict[src.code.Column, Column]) -> list[Expression]:
    """Group code.Expression by canonical representation → model.Expression"""
    expr_dict: defaultdict[str, list[src.code.Expression]] = defaultdict(list)
    for code_expr in tree.index[src.code.Expression]:
        assert isinstance(code_expr, src.code.Expression)
        canonical = _resolve_expression(code_expr, column_code_to_model)
        expr_dict[canonical].append(code_expr)

    model_expressions = []
    for canonical, code_exprs in expr_dict.items():
        first_expr = code_exprs[0]
        model_cols = frozenset(column_code_to_model[code_col] for code_col in first_expr.columns)
        model_expressions.append(
            Expression(
                _code=code_exprs,
                locations=[expr.location for expr in code_exprs],
                columns=model_cols,
                frequency=len(code_exprs),
                canonical=canonical,
                sql=first_expr.sql,
            )
        )

    return model_expressions


def build(tree: src.code.Tree) -> Semantics:
    """Build semantic model: resolve columns → group columns/tables → group expressions"""
    columns_resolved = _resolve_columns(tree)
    model_columns, code_to_model = _group_columns(tree, columns_resolved)
    model_tables = _group_tables(tree)
    model_expressions = _group_expressions(tree, code_to_model)
    expr_code_to_model = {code_expr: model_expr for model_expr in model_expressions for code_expr in model_expr._code}

    return Semantics(
        columns=model_columns,
        tables=model_tables,
        expressions=model_expressions,
        expr_code_to_model=expr_code_to_model,
    )
