import dataclasses
import json
import re
import urllib.parse
from pathlib import Path


def trunk_path(path: str | Path) -> str:
    """Replace current working directory with '.' for relative display"""
    return str(path).replace(str(Path.cwd()), ".")


def uri_to_path(uri: str) -> Path:
    path = urllib.parse.urlparse(uri).path
    path = urllib.parse.unquote(path)
    return Path(path)


def serialise(obj):
    """Recursively serialise objects to JSON-compatible format"""
    match obj:
        case _ if dataclasses.is_dataclass(obj):
            data = {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj) if not f.name.startswith("_")}
            return {key: serialise(value) for key, value in data.items()}
        case Path():
            return str(obj)
        case list() | frozenset() | set():
            return [serialise(item) for item in obj]
        case dict():
            return {key: serialise(value) for key, value in obj.items()}
        case _:
            return obj


def load_ndjson(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def json_compact(string: str) -> str:
    # Small one-item objects
    string = re.sub(r"\{\s+(.*)\s+\}", r"{ \1 }", string)
    # Hanging {
    string = re.sub(r"(\n[ \t]*)\{\s+", r"\1{ ", string)
    # Combine closing brackets on one line
    string = re.sub(r"\s+(?=[\}\]])", " ", string)
    # Collapse arrays of integers
    string = re.sub(r"\[\s*\d+\s*(?:,\s*\d+\s*)*\]", lambda m: re.sub(r"\s+", " ", m.group()), string)
    # Collapse arrays of strings
    string = re.sub(r'\[\s*"[^"]*"\s*(?:,\s*"[^"]*"\s*)*\]', lambda m: re.sub(r"\s+", " ", m.group()), string)

    return string


def pformat(obj) -> str:
    output_json = json.dumps(obj, indent=2)
    output_mini = json_compact(output_json)
    return output_mini


class Markdown:
    """Simple markdown document builder"""

    def __init__(self):
        self.lines = []

    def h1(self, text):
        self.lines.append(f"# {text}\n")

    def h2(self, text):
        self.lines.append(f"## {text}\n")

    def h3(self, text):
        self.lines.append(f"### {text}\n")

    def h4(self, text):
        self.lines.append(f"#### {text}\n")

    def code(self, obj, lang="json"):
        self.lines.append(f"```{lang}\n{pformat(obj)}\n```\n")

    def __str__(self):
        return "\n".join(self.lines)
