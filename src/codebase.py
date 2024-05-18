from pathlib import Path
from . import sql

__all__ = ["Codebase"]


class Codebase:
    files: dict[str : sql.Tree]
    columns_expr: dict[str : sql.Tree]

    def __init__(self, path: str):
        self._load_files(path)
        self._get_columns_expr()

    def _load_files(self, path: str):
        """Load all sql files from `path` into dict {file: AST, ...}"""
        root = Path(path)
        files = list(root.glob("**/*.sql"))

        self.files = {
            str(f.relative_to(root)): sql.parse(f.read_bytes()) for f in files
        }

    def _get_columns_expr(self):
        """Get all column expressions"""
        self.columns_expr = {}

        expressions = {
            "select_expression",
            "join_condition",
            "grouping_item",
            "order_by_clause_body",
        }

        # TODO: move to sql.py as too low-level
        # TODO: base on queries like
        #       (function_call function: (identifier) @ignore)
        #       (as_alias alias_name: (identifier) @ignore)
        #       (identifier) @column
        for file, tree in self.files.items():
            for sel in sql.find(tree, type="select", deep=True):
                for expr in sql.find(sel, type=expressions, deep=False):
                    for col in sql.find(expr, type="identifier", deep=False):
                        if col.parent.type not in {"function_call", "alias"}:
                            self.columns_expr.setdefault(col.text, set())
                            self.columns_expr[col.text].add(expr)

        pass
