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

from dataclasses import dataclass, field
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
    _tree: Tree
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
    _file: Path
    _tree: Tree
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
    _tree: Tree
    _node: sql.Node

    dataset: str | None
    table: str | None
    alias: str | None

    def __repr__(self) -> str:
        return "Table({}.{}{})".format(self.dataset or "?", self.table, f" as {self.alias}" if self.alias else "")


@dataclass(frozen=True)
class Query:
    _file: Path
    _tree: Tree
    _node: sql.Node

    sources: list[Table | Query]
    expressions: list[Expression]
    location: Location

    def __repr__(self) -> str:
        return f"Query({self.location})"


@dataclass()
class Tree:
    files: dict[Path, list[Query]] = field(default_factory=dict)
    index: dict[type, list[Query | Expression | Column | Table]] = field(default_factory=dict)

    def __repr__(self) -> str:
        files_str = ", ".join(str(f).replace(str(Path.cwd()), ".") for f in self.files)
        return f"Tree({files_str})"

    def ingest_file(self, path: Path, content: str) -> Tree:
        parse_tree = sql.parse(content.encode())
        self.files[path] = self._parse_node(parse_tree.root_node, path)
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
                location = Location(
                    file=file,
                    range=Range(
                        start_line=op_node.start_point[0],
                        start_char=op_node.start_point[1],
                        end_line=op_node.end_point[0],
                        end_char=op_node.end_point[1],
                    ),
                )
                ops.append(
                    self._make(
                        Expression,
                        _file=file,
                        _node=op_node,
                        columns=op_cols,
                        alias=sql.find_alias(op_node),
                        location=location,
                        sql=op_node.text.decode("utf-8"),
                    )
                )

            subqueries = self._parse_node(select_node, file=file)
            query_location = Location(
                file=file,
                range=Range(
                    start_line=select_node.start_point.row,
                    start_char=select_node.start_point.column,
                    end_line=select_node.end_point.row,
                    end_char=select_node.end_point.column,
                ),
            )
            query = self._make(
                Query,
                _file=file,
                _node=select_node,
                sources=tables + subqueries,
                expressions=ops,
                location=query_location,
            )
            queries.append(query)

        return queries
