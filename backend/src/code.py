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


@dataclass(frozen=True)
class Column:
    _file: str
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
        return hash("{}.{}.{}".format(self.dataset, self.table, self.column))


@dataclass(frozen=True)
class Expression:
    _file: str
    _tree: Tree
    _node: sql.Node

    columns: list[Column]
    alias: str | None

    def __repr__(self) -> str:
        return "Expression({}:{}:{})".format(
            self._file, self._node.start_point.row + 1, self._node.start_point.column + 1
        )

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

        return "Expression({})".format(node_to_str(self._node))


@dataclass(frozen=True)
class Table:
    _file: str
    _tree: Tree
    _node: sql.Node

    dataset: str | None
    table: str | None
    alias: str | None

    def __repr__(self) -> str:
        return "Table({}.{}{})".format(
            self.dataset or "?", self.table, " as {}".format(self.alias) if self.alias else ""
        )

    def __str__(self) -> str:
        return "Table({}.{}{})".format(self.dataset or "?", self.table, f" as {self.alias}" if self.alias else "")


@dataclass(frozen=True)
class Query:
    _file: str
    _tree: Tree
    _node: sql.Node

    sources: list[Table | Query]
    expressions: list[Expression]

    def __repr__(self) -> str:
        return "Query({}:{}:{})".format(self._file, self._node.start_point.row + 1, self._node.start_point.column + 1)


@dataclass(frozen=True)
class Tree:
    files: dict[str, list[Query]] = field(default_factory=dict)
    all_expressions: dict[tuple[str, frozenset[str]], list[Expression]] = field(default_factory=dict)

    def __repr__(self) -> str:
        return "Tree({})".format(", ".join(map(str, self.files)))


def from_dir(dir: Path) -> Tree:
    tree = Tree()
    for file in dir.glob("**/*.sql"):
        tree = ingest(tree, str(file.relative_to(dir)), file.read_text())
    return tree


def ingest(tree: Tree, name: str, content: str) -> Tree:
    parse_tree = sql.parse(content.encode())
    queries_tree = _parse_node_to_query(parse_tree.root_node, tree, name)
    new_all_expressions = _get_all_expressions(queries_tree)

    return Tree(
        files=tree.files | {name: queries_tree},
        all_expressions=tree.all_expressions | new_all_expressions,
    )


# BUG: Fix WITH RECURSIVE queries capture


def _parse_node_to_query(node: sql.Node, tree: Tree, file: str) -> list[Query]:
    queries = []
    for select_node in sql.find_desc(node, "@query"):

        # Capture tables
        tables = []
        for n in sql.find_desc(select_node, "@table"):
            tables.append(Table(_node=n, _tree=tree, _file=file, **sql.decode_table(n), alias=sql.find_alias(n)))

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
            columns.append(Column(_nodes=n, _tree=tree, _file=file, dataset=d, table=t, column=c))

        # Capture ops
        nodes_columns = {n: col for col in columns for n in col._nodes}
        ops = []
        for op_node in sql.find_desc(select_node, "@expression"):
            op_cols = []
            for col_node in sql.find_desc(op_node.parent, "@column"):  # type: ignore
                if nodes_columns[col_node] not in op_cols:
                    op_cols.append(nodes_columns[col_node])
            ops.append(
                Expression(_tree=tree, _file=file, _node=op_node, columns=op_cols, alias=sql.find_alias(op_node))
            )

        subqueries = _parse_node_to_query(select_node, tree=tree, file=file)
        query = Query(_tree=tree, _file=file, _node=select_node, sources=tables + subqueries, expressions=ops)
        queries.append(query)

    return queries


def _get_all_expressions(queries: list[Query]) -> dict[tuple[str, frozenset[str]], list[Expression]]:
    """
    Recursively finds all expressions from a `queries` and aggregates into a dictionary
    this will be used by logic.compare() to find similar expressions

       `tuple(expression_as_str, expression_columns_as_str_sorted) = [expression1, expression2, ...]`
    """

    all_expressions = defaultdict(list)
    for query in queries:
        # Process expressions in current query
        for expression in query.expressions:
            op_key = (str(expression), frozenset(map(str, expression.columns)))
            all_expressions[op_key].append(expression)

        # Recursively process subqueries
        nested_expressions = _get_all_expressions([s for s in query.sources if isinstance(s, Query)])
        for key, expressions in nested_expressions.items():
            all_expressions[key].extend(expressions)

    return dict(all_expressions)
