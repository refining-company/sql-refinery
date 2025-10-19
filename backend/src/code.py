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

from dataclasses import dataclass
from pathlib import Path

from src import sql


@dataclass(frozen=True)
class Range:
    start_line: int
    start_char: int
    end_line: int
    end_char: int

    def __repr__(self) -> str:
        return f"{self.start_line}:{self.start_char}-{self.end_line}:{self.end_char}"


@dataclass(frozen=True)
class Location:
    file: Path
    range: Range

    def __repr__(self) -> str:
        filename = str(self.file).replace(str(Path.cwd()), ".")
        return f"{filename}:{self.range}"


@dataclass(frozen=True)
class Column:
    _file: Path
    _nodes: list[sql.Node]

    dataset: str | None
    table: str | None
    column: str | None

    def __repr__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __hash__(self) -> int:
        return hash(f"{self.dataset}.{self.table}.{self.column}")


@dataclass(frozen=True)
class Expression:
    _node: sql.Node

    columns: list[Column]
    alias: str | None
    location: Location
    sql: str  # The SQL text of this expression

    def __repr__(self) -> str:
        return f"Expression({self.location})"

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
    _node: sql.Node

    dataset: str | None
    table: str | None
    alias: str | None

    def __repr__(self) -> str:
        return "Table({}.{}{})".format(self.dataset or "?", self.table, f" as {self.alias}" if self.alias else "")


@dataclass(frozen=True)
class Query:
    _node: sql.Node

    sources: list[Table | Query]
    expressions: list[Expression]
    location: Location

    def __repr__(self) -> str:
        return f"Query({self.location})"


@dataclass(frozen=True)
class Tree:
    files: dict[Path, list[Query]]
    index: dict[type, list[Query | Expression | Column | Table]]

    def __repr__(self) -> str:
        files_str = ", ".join(str(f).replace(str(Path.cwd()), ".") for f in self.files)
        return f"Tree({files_str})"


# Helper functions (pure)


def _resolve_columns(
    nodes_columns: dict[sql.Node, dict[str, str | None]], tables: list[Table]
) -> dict[sql.Node, dict[str, str | None]]:
    """Resolve column references to their actual table/dataset"""
    tables_aliases = {t.alias: t for t in tables}

    for col_path in nodes_columns.values():
        table = None
        if col_path["table"] in tables_aliases:
            table = tables_aliases[col_path["table"]]
        if not col_path["table"] and len(tables) == 1:
            table = tables[0]
        if table:
            col_path["table"] = table.table
            col_path["dataset"] = table.dataset

    return nodes_columns


def _deduplicate_columns(nodes_columns: dict[sql.Node, dict[str, str | None]], file: Path) -> list[Column]:
    """Create unique Column objects from potentially duplicate column nodes"""
    columns_nodes: dict = {}
    for node, col_dict in nodes_columns.items():
        key = tuple(col_dict.values())
        columns_nodes.setdefault(key, []).append(node)

    columns = []
    for (d, t, c), nodes in columns_nodes.items():
        columns.append(Column(_nodes=nodes, _file=file, dataset=d, table=t, column=c))

    return columns


# Independent parsers


def _parse_tables(query_node: sql.Node, file: Path) -> list[Table]:
    """Parse Table objects at this query level"""
    tables = []
    for node in sql.find_desc(query_node, "@table", local=True):
        tables.append(Table(_node=node, _file=file, **sql.decode_table(node), alias=sql.find_alias(node)))
    return tables


def _parse_columns(query_node: sql.Node, file: Path, tables: list[Table]) -> list[Column]:
    """Parse and resolve Column objects at this query level"""
    # Find all column nodes
    nodes_columns = {n: sql.decode_column(n) for n in sql.find_desc(query_node, "@column", local=True)}

    # Resolve columns against tables
    nodes_columns = _resolve_columns(nodes_columns, tables)

    # Deduplicate into Column objects
    columns = _deduplicate_columns(nodes_columns, file)

    return columns


def _parse_expressions(query_node: sql.Node, file: Path, columns: list[Column]) -> list[Expression]:
    """Parse Expression objects at this query level"""
    node_to_column = {node: col for col in columns for node in col._nodes}

    expressions = []
    for expr_node in sql.find_desc(query_node, "@expression", local=True):
        expr_cols = []
        for col_node in sql.find_desc(expr_node.parent, "@column", local=True):  # type: ignore
            if col_node in node_to_column and node_to_column[col_node] not in expr_cols:
                expr_cols.append(node_to_column[col_node])

        expressions.append(
            Expression(
                _node=expr_node,
                columns=expr_cols,
                alias=sql.find_alias(expr_node),
                location=Location(
                    file=file,
                    range=Range(
                        start_line=expr_node.start_point.row,
                        start_char=expr_node.start_point.column,
                        end_line=expr_node.end_point.row,
                        end_char=expr_node.end_point.column,
                    ),
                ),
                sql=expr_node.text.decode("utf-8") if expr_node.text else "",
            )
        )

    return expressions


# Recursive tree builder


def _parse_query(query_node: sql.Node, file: Path) -> Query:
    """Recursively parse a single Query node into Query tree structure"""
    # Parse components at this query level
    tables = _parse_tables(query_node, file)
    columns = _parse_columns(query_node, file, tables)
    expressions = _parse_expressions(query_node, file, columns)

    # Recursively parse subqueries (tree grows here)
    subquery_nodes = sql.find_desc(query_node, "@query", local=True)
    subqueries = [_parse_query(sub_node, file) for sub_node in subquery_nodes]

    return Query(
        _node=query_node,
        sources=tables + subqueries,
        expressions=expressions,
        location=Location(
            file=file,
            range=Range(
                start_line=query_node.start_point.row,
                start_char=query_node.start_point.column,
                end_line=query_node.end_point.row,
                end_char=query_node.end_point.column,
            ),
        ),
    )


# File-level parser


def _parse_tree(parse_tree: sql.Tree, file: Path) -> list[Query]:
    """Parse a sql.Tree into top-level Query objects for a single file"""
    # Find all top-level query nodes starting from root
    root_query_nodes = sql.find_desc(parse_tree.root_node, "@query", local=True)

    # Parse each top-level query (which will recursively handle subqueries)
    return [_parse_query(node, file) for node in root_query_nodes]


# Index builder


def _build_index(files: dict[Path, list[Query]]) -> dict[type, list[Query | Expression | Column | Table]]:
    """Build index by traversing Query tree recursively"""
    index: dict[type, list[Query | Expression | Column | Table]] = {}

    def traverse(query: Query):
        index.setdefault(Query, []).append(query)

        for expr in query.expressions:
            index.setdefault(Expression, []).append(expr)
            for col in expr.columns:
                if col not in index.get(Column, []):
                    index.setdefault(Column, []).append(col)

        for source in query.sources:
            if isinstance(source, Table):
                index.setdefault(Table, []).append(source)
            elif isinstance(source, Query):
                traverse(source)

    for queries in files.values():
        for query in queries:
            traverse(query)

    return index


# Main build function


def build(parse_trees: dict[Path, sql.Tree]) -> Tree:
    """Build code.Tree from dict of sql.Tree objects"""
    files = {file: _parse_tree(parse_tree, file) for file, parse_tree in parse_trees.items()}
    index = _build_index(files)
    return Tree(files=files, index=index)
