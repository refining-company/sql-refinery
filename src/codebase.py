from __future__ import annotations
import sqlite3
import dataclasses
from dataclasses import dataclass
from src import sql

"""
We will take in all sql files and parse the queries into tree-sitter trees,
afterwards we convert them into query trees containing all relveant information and 
traverse them resolving column names in the process, in the end the whole codebase is 
represented in form of a tree of each query in the database which itself is a query tree
"""

__all__ = ["Codebase", "Query", "Table", "Op", "Column"]


@dataclass
class Query:
    file: str
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
    file: str
    node: sql.Node
    columns: list[Column] = None
    alias: str = None


@dataclass
class Column:
    nodes: list[sql.Node]
    dataset: str = None
    table: str = None
    column: str = None


@dataclass
class Codebase:
    files: dict[str, sql.Tree]
    queries: list[Query]


def load(path: str) -> Codebase:
    """Load codebase from `path`"""
    files = sql.parse_files(path)
    queries = sum([to_queries(file, tree.root_node) for file, tree in files.items()], [])
    codebase = Codebase(files=files, queries=queries)

    return codebase


### TODO: make sure all identifiers are minimally resolved:
### it takes sql files, and makes a Database object that contains a tree of queries
### each query would have columns and tables that have:
###    - aliases resolved (so e.g. a.id becomes account.id)
###    - tables resolved if no JOINS (e.g. SELECT id FROM accounts -> accounts.id)

### TODO: capture all expressions and identifiers
### so in checker.py we can find similar experessions it will creat this
###  sort of a mapping {<column name> : [all expressions that use it]}

### TODO: think and tell me what about table mapping


def to_queries(file: str, node: sql.Node) -> list[Query]:
    """Create list of queries trees from parse tree"""
    queries = []
    for select_node in sql.find_desc(node, "@query"):
        # Capture tables
        tables = []
        for n in sql.find_desc(select_node, "@table"):
            tables.append(Table(node=n, **sql.get_table_path(n), alias=sql.find_alias(n)))

        # Capture columns
        nodes_columns = {n: sql.get_column_path(n) for n in sql.find_desc(select_node, "@column")}

        # Resolve columns
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

        # Squash multiple nodes into single column
        columns_nodes = {}
        for k, v in nodes_columns.items():
            columns_nodes.setdefault(tuple(v.values()), []).append(k)

        # Create columns
        columns = []
        for (d, t, c), n in columns_nodes.items():
            columns.append(Column(nodes=n, dataset=d, table=t, column=c))

        # Capture ops
        nodes_columns = {n: col for col in columns for n in col.nodes}
        ops = []
        for op_node in sql.find_desc(select_node, "@expression"):
            op_cols = []
            for col_node in sql.find_desc(op_node.parent, "@column"):
                if nodes_columns[col_node] not in op_cols:
                    op_cols.append(nodes_columns[col_node])
            ops.append(Op(file=file, node=op_node, columns=op_cols, alias=sql.find_alias(op_node)))

        subqueries = to_queries(file, select_node)
        for subquery in subqueries:
            queries.append(subquery)

        query = Query(file=file, node=select_node, sources=tables + subqueries, ops=ops)
        queries.append(query)

    return queries


### HELPERS


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
        fields = [obj.type]
        fields += ["{}:{}-{}:{}".format(*obj.start_point, *obj.end_point)]
        fields += [to_str(obj.text, lvl)] if obj.type == "identifier" else []
        return "sql.Node({fields})".format(fields=" ".join(fields))
    if isinstance(obj, (bytearray, bytes)):
        return obj.decode("utf-8")

    return str(obj)
