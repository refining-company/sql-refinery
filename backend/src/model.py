"""Semantic layer with deduplication and resolution"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import src

# ============================================================================
# Data Model
# ============================================================================


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
class Model:
    columns: list[Column]
    tables: list[Table]
    expressions: list[Expression]

    def __repr__(self) -> str:
        return (
            f"model.Model(columns={len(self.columns)}, tables={len(self.tables)}, expressions={len(self.expressions)})"
        )


# ============================================================================
# Resolution Logic
# ============================================================================


def _resolve_columns(query: src.code.Query) -> dict[src.code.Column, tuple[str | None, str | None, str | None]]:
    """Resolve column references using query-scoped alias lookup"""
    alias_to_table = {
        source.alias: source for source in query.sources if isinstance(source, src.code.Table) and source.alias
    }

    resolved: dict[src.code.Column, tuple[str | None, str | None, str | None]] = {}
    for expr in query.expressions:
        for code_col in expr.columns:
            col_dataset, col_table, col_column = code_col.dataset, code_col.table, code_col.column
            if col_table and col_table in alias_to_table:
                resolved_table = alias_to_table[col_table]
                col_table = resolved_table.table
                col_dataset = resolved_table.dataset or col_dataset

            resolved[code_col] = (col_dataset, col_table, col_column)

    return resolved


def _resolve_expression(ws: src.workspace.Workspace, code_expr: src.code.Expression) -> str:
    """Compute canonical representation using model columns"""
    nodes_to_col = ws.map(src.sql.Node, Column, by=("_node", "_code"))

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


# ============================================================================
# Grouping Logic
# ============================================================================


def _group_tables(ws: src.workspace.Workspace) -> list[Table]:
    """Group code.Table by (dataset, table)"""
    tables_dict: defaultdict[tuple[str | None, str | None], list[src.code.Table]] = defaultdict(list)
    for code_table in ws.get(src.code.Table):
        key = (code_table.dataset, code_table.table)
        tables_dict[key].append(code_table)

    return [ws.new(Table(_code=code, dataset=d, table=t, frequency=len(code))) for (d, t), code in tables_dict.items()]


def _group_columns(ws: src.workspace.Workspace) -> list[Column]:
    """Group code.Column by (dataset, table, column)"""
    columns_dict: defaultdict[tuple[str | None, str | None, str | None], list[src.code.Column]] = defaultdict(list)

    for query in ws.get(src.code.Query):
        resolved = _resolve_columns(query)
        for code_col, key in resolved.items():
            columns_dict[key].append(code_col)

    return [ws.new(Column(_code=code, dataset=d, table=t, column=c)) for (d, t, c), code in columns_dict.items()]


def _group_expressions(ws: src.workspace.Workspace) -> list[Expression]:
    """Group code.Expression by canonical representation"""
    expr_dict: defaultdict[str, list[src.code.Expression]] = defaultdict(list)
    for code_expr in ws.get(src.code.Expression):
        canonical = _resolve_expression(ws, code_expr)
        expr_dict[canonical].append(code_expr)

    col_map = ws.map(src.code.Column, Column, by="_code")
    model_expressions = []
    for canonical, code_exprs in expr_dict.items():
        first_expr = code_exprs[0]
        model_cols = frozenset(col_map[code_col] for code_col in first_expr.columns)
        model_expressions.append(
            ws.new(
                Expression(
                    _code=code_exprs,
                    locations=[expr.location for expr in code_exprs],
                    columns=model_cols,
                    frequency=len(code_exprs),
                    canonical=canonical,
                    sql=first_expr.sql,
                )
            )
        )

    return model_expressions


# ============================================================================
# Builder
# ============================================================================


def build(ws: src.workspace.Workspace) -> Model:
    """Build semantic model from syntactic code layer"""
    assert ws.layer_code is not None

    model_columns = _group_columns(ws)
    model_tables = _group_tables(ws)
    model_expressions = _group_expressions(ws)

    return Model(columns=model_columns, tables=model_tables, expressions=model_expressions)
