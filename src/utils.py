import re
import json
import sqlite3
import dataclasses
import tree_sitter
from src import codebase


# The issue is when we simplify a codebase we don't want to capture the column identifiers at
# the tree-sitter level since they are not resolved, so once we are simplifing one of the
# codebase dataclasses we pass include_identifier = false recursivly
# if we are simpifying a tree sitter tree or node then the include_identifier defaults to true and is never set to false
# since it doesn't enter the codebase dataclasses block


def simplify(obj, include_identifier=True) -> dict | list | str:
    if isinstance(obj, (codebase.Codebase, codebase.Query, codebase.Table, codebase.Op, codebase.Column)):
        keys = [field.name for field in dataclasses.fields(obj)]
        return {":".join(keys): [simplify(getattr(obj, field), include_identifier) for field in keys]}

    if isinstance(obj, tree_sitter.Tree):
        return {"root": [simplify(obj.root_node, include_identifier)]}

    if isinstance(obj, tree_sitter.Node):
        keys = [obj.grammar_name]
        if obj.type in ("identifier", "number", "string"):
            if include_identifier:
                return {":".join(keys): obj.text.decode("utf-8")}
            return {":".join(keys): ""}
        return {":".join(keys): [simplify(child, include_identifier) for child in obj.children]}

    if isinstance(obj, dict):
        return {str(key): simplify(value, include_identifier) for key, value in obj.items()}

    if isinstance(obj, list):
        return [simplify(item, include_identifier) for item in obj]

    if isinstance(obj, bytes):
        return obj.decode("utf-8")

    try:
        return str(obj)
    except Exception as e:
        raise TypeError(f"Object of type {type(obj)} is not simplifiable: {e}")


def json_minify(string: str) -> str:
    """Minify JSON string."""
    string = re.sub(r"\{\s+(.*)\s+\}", r"{ \1 }", string)  # small one-item objects
    string = re.sub(r"(\n[ \t]*)\{\s+", r"\1{ ", string)  # hanging {
    string = re.sub(r"\s+(?=[\}\]])", " ", string)  # combine closing brackets on one line

    return string


def prettify(obj, fn: callable) -> str:
    output_simp = fn(obj)
    output_json = json.dumps(output_simp, indent=2)
    output_mini = json_minify(output_json)
    return output_mini


def pprint(obj, fn: callable):
    print(prettify(obj, fn))


def extract_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = {}

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        table_name = table_name.encode("utf-8")
        schema[table_name] = []

        for column in columns:
            ## retrieve only the name
            schema[table_name].append(column[1].encode("utf-8"))

    conn.close()
    return schema
