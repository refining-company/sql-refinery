import sys
from pathlib import Path
import shutil
import tests.test_code
import tests.test_logic
import tests.test_sql
import tests.conftest


def update(origin: Path | str):
    path = Path(origin)
    if not path.exists():
        raise FileNotFoundError("Provided path does not exist")
    print("Using new test inputs {}".format(str(origin)))

    update_funcs = [
        tests.test_logic.update_snapshots,
        # tests.test_code.update_snapshots,
        # tests.test_sql.update_snapshots,
    ]

    paths = tests.conftest.get_paths()
    if paths["inputs"].exists():
        shutil.rmtree(paths["inputs"])
        print("Deleted old inputs")

    print("Test inputs copied to {}".format(paths["inputs"]))
    shutil.copytree(origin, paths["inputs"])

    print("Updating snapshots...")
    for func in update_funcs:
        print("\t", func.__module__)
        func(paths)
    print("Snapshots updated")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        update(sys.argv[1])
    else:
        print("Please provide the path to the codebase")
