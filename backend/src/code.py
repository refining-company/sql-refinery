"""
Pipeline — Code AST Abstraction

Architecture:
- Pipeline: Code AST abstraction (this module)
- Server: LSP server (server.py)
- Frontend: VS Code extension (frontend-vscode)

This module provides:
- Data classes for Table, Column, Expression, Query, and Tree
- Logic to transform raw tree-sitter nodes into a structured code AST
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from src import sql


@dataclass(frozen=True)
class Column:
    _file: Path
    _tree: Tree
    _nodes: list[sql.Node]

    dataset: str | None
    table: str | None
    column: str | None

    def __repr__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __str__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __hash__(self) -> int:
        return hash(f"{self.dataset}.{self.table}.{self.column}")


@dataclass(frozen=True)
class Expression:
    _file: Path
    _tree: Tree
    _node: sql.Node

    columns: list[Column]
    alias: str | None

    def __repr__(self) -> str:
        return f"Expression({self._file}:{self._node.start_point.row + 1}:{self._node.start_point.column + 1})"

    def __str__(self) -> str:
        # TODO: maybe should be a different method
        nodes_to_col = {node: column for column in self.columns for node in column._nodes}

        def node_to_str(node: sql.Node) -> str:
            if node in nodes_to_col:
                result = str(nodes_to_col[node])
            elif sql.is_type(node, "#constant"):
                # FIXME: not sure we need capturing this, probably there is a way around in src.code.op.__str__
                result = node.text.decode("utf-8")  # type: ignore
            elif sql.is_type(node, "#function"):
                parsed_name, parsed_args = sql.decode_function(node)
                result = "{}({})".format(parsed_name, ", ".join(map(node_to_str, parsed_args)))
            else:
                result = node.type.capitalize()
                if len(node.children):
                    result += "({})".format(", ".join(map(node_to_str, node.named_children)))

            return result

        return f"Expression({node_to_str(self._node)})"


@dataclass(frozen=True)
class Table:
    _file: Path
    _tree: Tree
    _node: sql.Node

    dataset: str | None
    table: str | None
    alias: str | None

    def __repr__(self) -> str:
        return "Table({}.{}{})".format(self.dataset or "?", self.table, f" as {self.alias}" if self.alias else "")

    def __str__(self) -> str:
        return "Table({}.{}{})".format(self.dataset or "?", self.table, f" as {self.alias}" if self.alias else "")


@dataclass(frozen=True)
class Query:
    _file: Path
    _tree: Tree
    _node: sql.Node

    sources: list[Table | Query]
    expressions: list[Expression]

    def __repr__(self) -> str:
        return f"Query({self._file}:{self._node.start_point.row + 1}:{self._node.start_point.column + 1})"


@dataclass()
class Tree:
    files: dict[Path, list[Query]] = field(default_factory=dict)
    index: dict[type, list[Query | Expression | Column | Table]] = field(default_factory=dict)
    map_key_to_expr: dict[tuple[str, frozenset[str]], list[Expression]] = field(default_factory=dict)
    map_file_to_expr: dict[Path, list[Expression]] = field(default_factory=dict)

    def __repr__(self) -> str:
        return "Tree({})".format(", ".join(map(str, self.files)))

    def ingest_file(self, path: Path, content: str) -> Tree:
        parse_tree = sql.parse(content.encode())
        self.files[path] = self._parse_node(parse_tree.root_node, path)
        self.map_key_to_expr |= _map_key_to_expr(self.index[Expression])  # type: ignore
        self.map_file_to_expr |= _map_file_to_expr(self.index[Expression])  # type: ignore

        return self

    def _make(self, cls, *args, **kwargs) -> object:
        obj = cls(_tree=self, *args, **kwargs)
        self.index.setdefault(cls, []).append(obj)
        return obj

    def _parse_node(self, node: sql.Node, file: Path) -> list[Query]:
        queries = []
        for select_node in sql.find_desc(node, "@query"):

            # Capture tables
            tables = []
            for n in sql.find_desc(select_node, "@table"):
                tables.append(self._make(Table, _node=n, _file=file, **sql.decode_table(n), alias=sql.find_alias(n)))

            # Capture columns
            nodes_columns = {n: sql.decode_column(n) for n in sql.find_desc(select_node, "@column")}

            tables_aliases = {t.alias: t for t in tables}
            for col, path in nodes_columns.items():
                table = None
                if path["table"] in tables_aliases:
                    table = tables_aliases[path["table"]]
                if not path["table"] and len(tables) == 1:
                    table = tables[0]
                if table:
                    path["table"] = table.table
                    path["dataset"] = table.dataset

                # TODO: resolve using data model (when no table is specified in JOIN but could be inferred)
                # TODO: resolve when different datasets/catalogs
                # TODO: resolve `*` into columns

            # Squash multiple column nodes into single column object
            columns_nodes = {}
            for k, v in nodes_columns.items():
                columns_nodes.setdefault(tuple(v.values()), []).append(k)

            # Create columns
            columns = []
            for (d, t, c), n in columns_nodes.items():
                columns.append(self._make(Column, _nodes=n, _file=file, dataset=d, table=t, column=c))

            # Capture ops
            nodes_columns = {n: col for col in columns for n in col._nodes}
            ops = []
            for op_node in sql.find_desc(select_node, "@expression"):
                op_cols = []
                for col_node in sql.find_desc(op_node.parent, "@column"):  # type: ignore
                    if nodes_columns[col_node] not in op_cols:
                        op_cols.append(nodes_columns[col_node])
                ops.append(
                    self._make(Expression, _file=file, _node=op_node, columns=op_cols, alias=sql.find_alias(op_node))
                )

            subqueries = self._parse_node(select_node, file=file)
            query = self._make(Query, _file=file, _node=select_node, sources=tables + subqueries, expressions=ops)
            queries.append(query)

        return queries


# BUG: Fix WITH RECURSIVE queries capture


def _map_key_to_expr(exprs: list[Expression]) -> dict[tuple[str, frozenset[str]], list[Expression]]:
    mapped = defaultdict(list)
    for expr in exprs:
        op_key = (str(expr), frozenset(map(str, expr.columns)))
        mapped[op_key].append(expr)

    return dict(mapped)


def _map_file_to_expr(exprs: list[Expression]) -> dict[str, list[Expression]]:
    mapped = defaultdict(list)
    for expr in exprs:
        op_key = expr._file
        mapped[op_key].append(expr)

    return dict(mapped)
