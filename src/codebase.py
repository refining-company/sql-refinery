from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from . import sql

__all__ = ["Codebase", "Query", "Table", "Op", "Column"]


@dataclass
class Query:
    node: sql.Node
    sources: list[Table | Query] = None
    ops: list[Op] = None


@dataclass
class Table:
    node: sql.Node
    dataset: str = None
    table: str = None


@dataclass
class Op:
    node: sql.Node
    columns: list[Column] = None


@dataclass
class Column:
    node: sql.Node
    dataset: str = None
    table: str = None
    column: str = None


@dataclass
class Codebase:
    files: dict[str, sql.Tree]
    queries: list[Query]


def load(path: str) -> Codebase:
    """Load codebase from `path`"""
    files = load_files(path)
    queries = sum([to_queries(t.root_node) for t in files.values()], [])

    return Codebase(files=files, queries=queries)


def load_files(path: str) -> dict[str, sql.Tree]:
    """Load all sql files from `path` into dict `{<file name>: <sql tree>, ...}`"""
    root = Path(path)
    paths = list(root.glob("**/*.sql"))
    files = {str(f.relative_to(root)): sql.parse(f.read_bytes()) for f in paths}

    return files


def to_queries(node: sql.Node) -> list[Query]:
    """Create list of queries trees from parse tree"""
    queries = []
    for scope in sql.find_desc(node, "@scope"):
        for select in sql.find_desc(scope, "select"):
            ops = []
            for op_n in sql.find_desc(select, "@expression"):
                op_cols = [Column(node=n) for n in sql.find_desc(op_n, "@column")]
                op = Op(node=op_n, columns=op_cols)
                ops.append(op)

            tables = [Table(node=n) for n in sql.find_desc(select, "@table")]
            subqueries = to_queries(select)

            query = Query(node=select, sources=tables + subqueries, ops=ops)
            queries.append(query)

    return queries
