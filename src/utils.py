import re
import json
import sqlite3
from src import sql


def node_preview(node: sql.Node):
    text = node.text.decode("utf-8")[:100]
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s\s+", " ", text)
    return text


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
