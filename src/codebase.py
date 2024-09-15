from __future__ import annotations
from pathlib import Path
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
class Column:
    nodes: list[sql.Node]
    dataset: str = None
    table: str = None
    column: str = None

    def __repr__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __str__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __hash__(self) -> tuple[str, str, str]:
        return hash("{}.{}.{}".format(self.dataset, self.table, self.column))


@dataclass
class Op:
    file: Path
    node: sql.Node
    columns: list[Column] = None
    alias: str = None

    def __str__(self) -> str:
        nodes_to_col = {node: column for column in self.columns for node in column.nodes}

        def node_to_str(node: sql.Node) -> str:
            if node in nodes_to_col:
                result = str(nodes_to_col[node])
            elif sql.is_type(node, "@constant"):
                result = node.text.decode("utf-8")
            elif sql.is_type(node, "@function"):
                parsed = sql.parse_function(node)
                result = "{}({})".format(parsed["name"], ", ".join(map(node_to_str, parsed["args"])))
            else:
                result = node.type.capitalize()
                if len(node.children):
                    result += "({})".format(", ".join(map(node_to_str, node.named_children)))

            return result

        return "Op({})".format(node_to_str(self.node))


@dataclass
class Table:
    node: sql.Node
    dataset: str = None
    table: str = None
    alias: str = None

    def __str__(self) -> str:
        return "Table({}.{}{})".format(self.dataset, self.table, f" as {self.alias}" if self.alias else "")


@dataclass
class Query:
    file: str
    node: sql.Node
    sources: list[Table | Query] = None
    ops: list[Op] = None
    alias: str = None


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
            tables.append(Table(node=n, **sql.parse_table(n), alias=sql.find_alias(n)))

        # Capture columns
        nodes_columns = {n: sql.parse_column(n) for n in sql.find_desc(select_node, "@column")}

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

        # Squash multiple column nodes into single column object
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
        query = Query(file=file, node=select_node, sources=tables + subqueries, ops=ops)
        queries.append(query)

    return queries


### HELPERS


def simplify(obj) -> dict | list | str:
    if isinstance(obj, Codebase):
        return {
            "files": [{"File:{}".format(str(file)): []} for file in obj.files.keys()],
            "queries": [simplify(query) for query in obj.queries],
        }

    if isinstance(obj, Query):
        query = {
            "Query:{}:{}:{}".format(obj.file, obj.node.start_point.row + 1, obj.node.start_point.column + 1): {
                "ops": [simplify(op) for op in obj.ops]
            }
        }
        return query

    if isinstance(obj, Table):
        return {str(obj): []}

    if isinstance(obj, Op):
        op = {
            "{} at {}:{}:{}".format(
                op,
                op.file,
                op.node.start_point.row + 1,
                op.node.start_point.column + 1,
            ): simplify(obj.columns)
        }
        return op

    if isinstance(obj, Column):
        return str(obj)

    if isinstance(obj, sql.Tree):
        return {"root": [simplify(obj.root_node)]}

    if isinstance(obj, sql.Node):
        keys = [obj.grammar_name]
        if obj.type in ("identifier", "number", "string"):
            return {":".join(keys): obj.text.decode("utf-8")}
        return {":".join(keys): [simplify(child) for child in obj.children]}

    if isinstance(obj, dict):
        return {str(key): simplify(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    try:
        return str(obj)
    except Exception as e:
        raise TypeError(f"Object of type {type(obj)} is not simplifiable: {e}")
