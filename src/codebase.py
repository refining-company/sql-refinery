from .parser import sql, Tree
from pathlib import Path


def load(path: str) -> Tree:
    root = Path(path)
    files = list(root.glob("**/*.sql"))

    codebase = {f.relative_to(root): f for f in files}
    print(codebase)
    ...
    # tree = sql.parse(files[0].read_bytes())
