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
    files = load_files(path)
    queries = sum([to_queries(t.root_node) for t in files.values()], [])
    codebase = Codebase(files=files, queries=queries)
    pprint(codebase)

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
            # TODO: resolve using data model
            # TODO: resolve when different datasets
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
        # BUG: `USING (account_id, date_month)` is captured incorrectly
        # BUG: `GROUP BY <expr>, <expr>` columns for expressions are duplicated (parent is the issue)
        # XXX add tests for this function
        nodes_columns = {n: col for col in columns for n in col.nodes}
        ops = []
        for op_node in sql.find_desc(select_node, "@expression"):
            op_cols = []
            for col_node in sql.find_desc(op_node.parent, "@column"):
                if nodes_columns[col_node] not in op_cols:
                    op_cols.append(nodes_columns[col_node])
            ops.append(Op(node=op_node, columns=op_cols, alias=sql.find_alias(op_node)))

        subqueries = to_queries(select_node)

        query = Query(node=select_node, sources=tables + subqueries, ops=ops)
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
