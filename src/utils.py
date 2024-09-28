import re
import json


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
