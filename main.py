from tree_sitter import Language, Parser

if __name__ == "__main__":
    language = Language("./parsers/sql.so", "sql")
    parser = Parser()
    parser.set_language(language)
    sql = b"""CREATE TABLE _datasette_auth_tokens (
    id INTEGER PRIMARY KEY,
    secret TEXT,
    description TEXT,
    permissions TEXT,
    actor_id TEXT,
    created_timestamp INTEGER,
    last_used_timestamp INTEGER,
    expires_after_seconds INTEGER
    );"""
    tree = parser.parse(sql)
    print(tree.root_node.sexp())
