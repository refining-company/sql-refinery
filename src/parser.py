from tree_sitter import Language, Parser, Tree

__all__ = ["sql", "Tree"]

language = Language("./parsers/sql.so", "sql")
sql = Parser()
sql.set_language(language)
