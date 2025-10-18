import json
import re
from pathlib import Path


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
