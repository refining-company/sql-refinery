"""Process SQL parse tree into Code tree

It takes tree-sitter sql.Tree and sql.Node and constructs a new fixed data structure:
- tree
- query
- table
- expression
- column
"""

from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass, field
from collections import defaultdict

from src import sql


@dataclass
class Column:
    nodes: list[sql.Node]
    dataset: str | None
    table: str | None
    column: str | None

    def __repr__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __str__(self) -> str:
        return "Column({}.{}.{})".format(self.dataset or "?", self.table or "?", self.column or "?")

    def __hash__(self) -> int:
        return hash("{}.{}.{}".format(self.dataset, self.table, self.column))


@dataclass
class Expression:
    file: str  # TODO: add root to all objects
    node: sql.Node
    columns: list[Column]
    alias: str | None

    def __repr__(self) -> str:
        return "Expression({}:{}:{})".format(self.file, self.node.start_point.row + 1, self.node.start_point.column + 1)

    def __str__(self) -> str:
        # TODO: maybe should be a different method
        nodes_to_col = {node: column for column in self.columns for node in column.nodes}

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

        return "Expression({})".format(node_to_str(self.node))


@dataclass
class Table:
    node: sql.Node
    dataset: str | None
    table: str | None
    alias: str | None

    def __repr__(self) -> str:
        return "Table({}.{}{})".format(
            self.dataset or "?", self.table, " as {}".format(self.alias) if self.alias else ""
        )

    def __str__(self) -> str:
        return "Table({}.{}{})".format(self.dataset or "?", self.table, f" as {self.alias}" if self.alias else "")


@dataclass
class Query:
    file: str
    node: sql.Node
    sources: list[Table | Query]
    expressions: list[Expression]
    alias: str | None

    def __repr__(self) -> str:
        return "Query({}:{}:{})".format(self.file, self.node.start_point.row + 1, self.node.start_point.column + 1)


@dataclass
class Tree:
    files: dict[str, sql.Tree] = field(default_factory=dict)
    queries: list[Query] = field(default_factory=list)
    all_queries: list[Query] = field(default_factory=list)
    all_expressions: dict[tuple[str, set[str]], list[Expression]] = field(default_factory=dict)

    def __repr__(self) -> str:
        return "Tree({})".format(", ".join(map(str, self.queries)))


def from_dir(dir: Path) -> Tree:
    tree = Tree()
    for file in dir.glob("**/*.sql"):
        tree = ingest(tree, str(file.relative_to(dir)), file.read_text())
    return tree


def ingest(tree: Tree, name: str, content: str) -> Tree:
    parse_tree = sql.parse(content.encode())
    new_files = {name: parse_tree}
    new_queries = _parse_sql_to_query(name, parse_tree.root_node)
    new_all_queries = _get_all_queries(new_queries)
    new_all_expressions = _get_all_expressions(new_all_queries)

    return Tree(
        files=tree.files | new_files,
        queries=tree.queries + new_queries,
        all_queries=tree.all_queries + new_all_queries,
        all_expressions=tree.all_expressions | new_all_expressions,
    )


### TODO: make sure all identifiers are minimally resolved:
### it takes sql files, and makes a Database object that contains a tree of queries
### each query would have columns and tables that have:
###    - aliases resolved (so e.g. a.id becomes account.id)
###    - tables resolved if no JOINS (e.g. SELECT id FROM accounts -> accounts.id)

### TODO: capture all expressions and identifiers
### so in checker.py we can find similar experessions it will creat this
###  sort of a mapping {<column name> : [all expressions that use it]}

### TODO: think and tell me what about table mapping


def _parse_sql_to_query(file: str, node: sql.Node) -> list[Query]:
    queries = []
    for select_node in sql.find_desc(node, "@query"):

        # Capture tables
        tables = []
        for n in sql.find_desc(select_node, "@table"):
            tables.append(Table(node=n, **sql.decode_table(n), alias=sql.find_alias(n)))

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
            columns.append(Column(nodes=n, dataset=d, table=t, column=c))

        # Capture ops
        nodes_columns = {n: col for col in columns for n in col.nodes}
        ops = []
        for op_node in sql.find_desc(select_node, "@expression"):
            op_cols = []
            for col_node in sql.find_desc(op_node.parent, "@column"):  # type: ignore
                if nodes_columns[col_node] not in op_cols:
                    op_cols.append(nodes_columns[col_node])
            ops.append(Expression(file=file, node=op_node, columns=op_cols, alias=sql.find_alias(op_node)))

        subqueries = _parse_sql_to_query(file, select_node)
        # FIXME: check if alias is needed at all in Query
        query = Query(file=file, node=select_node, sources=tables + subqueries, expressions=ops, alias=None)
        queries.append(query)

    return queries


def _get_all_queries(queries: list[Query]) -> list[Query]:
    nested_queries = []
    for query in queries:
        nested_queries += _get_all_queries([s for s in query.sources if isinstance(s, Query)])
    return queries + nested_queries


def _get_all_expressions(queries: list[Query]) -> dict[tuple[str, set[str]], list[Expression]]:
    all_expressions = defaultdict(list)
    for query in queries:
        for expression in query.expressions:
            op_key = (str(expression), tuple(sorted(map(str, expression.columns))))
            all_expressions[op_key].append(expression)

    return dict(all_expressions)
