import json
import re
from pathlib import Path


def load_ndjson(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def json_compact(string: str) -> str:
    string = re.sub(r"\{\s+(.*)\s+\}", r"{ \1 }", string)  # small one-item objects
    string = re.sub(r"(\n[ \t]*)\{\s+", r"\1{ ", string)  # hanging {
    string = re.sub(r"\s+(?=[\}\]])", " ", string)  # combine closing brackets on one line

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
