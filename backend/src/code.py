"""
SQL Refining — Syntactic Code Layer

Parse SQL files into syntactic tree (1:1 mapping with SQL AST).
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import src


@dataclass(frozen=True)
class Range:
    start_line: int
    start_char: int
    end_line: int
    end_char: int

    def __repr__(self) -> str:
        return "code.Range"

    def __str__(self) -> str:
        return f"{self.start_line}:{self.start_char}-{self.end_line}:{self.end_char}"


@dataclass(frozen=True)
class Location:
    file: Path
    range: Range

    def __repr__(self) -> str:
        return "code.Location"

    def __str__(self) -> str:
        return f"{src.utils.trunk_path(self.file)}:{self.range}"

    def __hash__(self) -> int:
        return hash((self.file, self.range))


@dataclass(frozen=True)
class Column:
    _node: src.sql.Node

    dataset: str | None
    table: str | None
    column: str | None
    location: Location

    def __repr__(self) -> str:
        return f"code.Column({self.location!s})"

    def __str__(self) -> str:
        return f"{self.dataset or "?"}.{self.table or "?"}.{self.column or "?"}"

    def __hash__(self) -> int:
        return hash((type(self), self.location))


@dataclass(frozen=True)
class Expression:
    _node: src.sql.Node

    columns: list[Column]
    alias: str | None
    location: Location
    sql: str

    def __repr__(self) -> str:
        return f"code.Expression({self.location!s})"

    def __str__(self) -> str:
        return f"{self.sql}"

    def __hash__(self) -> int:
        return hash((type(self), self.location))


@dataclass(frozen=True)
class Table:
    _node: src.sql.Node

    dataset: str | None
    table: str | None
    alias: str | None
    location: Location

    def __repr__(self) -> str:
        return f"code.Table({self.location!s})"

    def __str__(self) -> str:
        return f"{self.dataset or "?"}.{self.table or "?"}"

    def __hash__(self) -> int:
        return hash((type(self), self.location))


@dataclass(frozen=True)
class Query:
    _node: src.sql.Node

    sources: list[Table | Query]
    expressions: list[Expression]
    location: Location

    def __repr__(self) -> str:
        return f"code.Query({self.location!s})"

    def __hash__(self) -> int:
        return hash((type(self), self.location))


@dataclass(frozen=True)
class Tree:
    files: dict[Path, list[Query]]
    index: dict[type, list[Query | Expression | Column | Table]]

    def __repr__(self) -> str:
        return f"code.Tree(files={len(self.files)})"


def parse_range(node: src.sql.Node) -> Range:
    return Range(
        start_line=node.start_point.row,
        start_char=node.start_point.column,
        end_line=node.end_point.row,
        end_char=node.end_point.column,
    )


def _parse_tables(query_node: src.sql.Node, file: Path) -> list[Table]:
    tables = []
    for node in src.sql.find_desc(query_node, "@table", local=True):
        loc = Location(file=file, range=parse_range(node))
        tables.append(Table(_node=node, location=loc, **src.sql.decode_table(node), alias=src.sql.find_alias(node)))
    return tables


def _parse_columns(query_node: src.sql.Node, file: Path) -> list[Column]:
    columns = []
    for node in src.sql.find_desc(query_node, "@column", local=True):
        col_dict = src.sql.decode_column(node)
        location = Location(file=file, range=parse_range(node))
        columns.append(Column(_node=node, location=location, **col_dict))
    return columns


def _parse_expressions(query_node: src.sql.Node, file: Path) -> list[Expression]:
    expressions = []
    for expr_node in src.sql.find_desc(query_node, "@expression", local=True):
        expr_cols = _parse_columns(expr_node.parent, file)  # type: ignore
        expressions.append(
            Expression(
                _node=expr_node,
                columns=expr_cols,
                alias=src.sql.find_alias(expr_node),
                location=Location(file=file, range=parse_range(expr_node)),
                sql=expr_node.text.decode("utf-8") if expr_node.text else "",
            )
        )
    return expressions


def _parse_query(query_node: src.sql.Node, file: Path) -> Query:
    tables = _parse_tables(query_node, file)
    expressions = _parse_expressions(query_node, file)
    subquery_nodes = src.sql.find_desc(query_node, "@query", local=True)
    subqueries = [_parse_query(sub_node, file) for sub_node in subquery_nodes]
    return Query(
        _node=query_node,
        sources=tables + subqueries,
        expressions=expressions,
        location=Location(file=file, range=parse_range(query_node)),
    )


def _parse_tree(parse_tree: src.sql.Tree, file: Path) -> list[Query]:
    root_query_nodes = src.sql.find_desc(parse_tree.root_node, "@query", local=True)
    return [_parse_query(node, file) for node in root_query_nodes]


def _build_index(files: dict[Path, list[Query]]) -> dict[type, list[Query | Expression | Column | Table]]:
    index: defaultdict[type, list[Query | Expression | Column | Table]] = defaultdict(list)

    def traverse(query: Query):
        index[Query].append(query)
        for expr in query.expressions:
            index[Expression].append(expr)
            for col in expr.columns:
                if col not in index[Column]:
                    index[Column].append(col)
        for source in query.sources:
            if isinstance(source, Table):
                index[Table].append(source)
            elif isinstance(source, Query):
                traverse(source)

    for queries in files.values():
        for query in queries:
            traverse(query)

    return dict(index)


def build(parse_trees: dict[Path, src.sql.Tree]) -> Tree:
    files = {file: _parse_tree(parse_tree, file) for file, parse_tree in parse_trees.items()}
    index = _build_index(files)
    return Tree(files=files, index=index)
