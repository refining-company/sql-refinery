from __future__ import annotations
import dataclasses
from dataclasses import dataclass
from pathlib import Path
from . import sql

__all__ = ["Codebase", "Query", "Table", "Op", "Column"]


@dataclass
class Query:
    node: sql.Node
    sources: list[Table | Query] = None
    ops: list[Op] = None
    alias: str = None


@dataclass
class Table:
    node: sql.Node
    dataset: str = None
    table: str = None
    alias: str = None


@dataclass
class Op:
    node: sql.Node
    columns: list[Column] = None
    alias: str = None


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
    codebase = Codebase(files=files, queries=queries)
    pprint(codebase)
    for query in codebase.queries:
        resolve(query)

    return codebase


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
            tables = []
            for table_node in sql.find_desc(select, "@table"):
                alias = sql.find_alias(table_node)
                table = Table(node=table_node, table=table_node.text, alias=alias)

                tables.append(table)

            ops = []
            for op_n in sql.find_desc(select, "@expression"):
                op_cols = []
                for col_n in sql.find_desc(op_n, "@column"):
                    op_cols.append(Column(node=col_n))

                op = Op(node=op_n, columns=op_cols)
                ops.append(op)

            subqueries = to_queries(select)

            query = Query(node=select, sources=tables + subqueries, ops=ops)
            queries.append(query)

    return queries


def resolve(query: Query):
    """Qualify all columns in the query"""
    for source in query.sources:
        alias = sql.find_desc(source.node, "@alias")
        if alias:
            source.alias = alias[0].text
            print(source.alias)

        if isinstance(source, Query):
            resolve(source)


def pprint(obj):
    """Pretty print objects in this module"""
    print(to_str(obj))


def to_str(obj, lvl: int = 0, indent: int = 2):
    # Convert all to tuples
    if isinstance(obj, list):
        lvl += len(obj) > 1
        fields = tuple(to_str(v, lvl) for v in obj)
        return "[{fields}]".format(fields=to_str(fields, lvl))
    if isinstance(obj, dict):
        lvl += len(obj) > 1
        fields = tuple("{}:{}".format(k, to_str(v, lvl)) for k, v in obj.items())
        return "{{{fields}}}".format(fields=to_str(fields, lvl))
    if isinstance(obj, (Codebase, Query, Table, Op, Column)):
        lvl += len(dataclasses.fields(obj)) > 1
        fields = [(f.name, getattr(obj, f.name)) for f in dataclasses.fields(obj)]
        fields = tuple("{}={}".format(f, to_str(v, lvl)) for f, v in fields)
        return "{name}({fields})".format(name=obj.__class__.__name__, fields=to_str(fields, lvl))

    # Convert tall to strings
    if isinstance(obj, tuple):
        pad = "\n" + " " * (lvl * indent)
        lvl += len(obj) > 1
        return "".join("{}{}".format(pad if len(obj) > 1 else "", to_str(o, lvl)) for o in obj)
    if isinstance(obj, sql.Tree):
        return "sql.Tree"
    if isinstance(obj, sql.Node):
        fields = [obj.type] + [to_str(obj.text, lvl)] if obj.type == "identifier" else []
        return "sql.Node({fields})".format(fields=" ".join(fields))
    if isinstance(obj, (bytearray, bytes)):
        return obj.decode("utf-8")

    return str(obj)
