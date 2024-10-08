import sys
from pathlib import Path
import shutil
import tests.test_snapshots
import tests.conftest


def copy(origin: Path | str):
    raise NotImplemented("Need to rewrite test updating functionality")

    path = Path(origin)
    if not path.exists():
        raise FileNotFoundError("Provided path does not exist")
    print("Using new test inputs {}".format(str(origin)))

    paths = tests.conftest.get_paths()
    if paths["inputs"].exists():
        shutil.rmtree(paths["inputs"])
        print("Deleted old inputs")

    print("Test inputs copied to {}".format(paths["inputs"]))
    shutil.copytree(origin, paths["inputs"])


def update():
    update_funcs = [tests.test_snapshots.update_snapshots]
    paths = tests.conftest.get_paths()

    print("Updating snapshots...")
    for func in update_funcs:
        print("\t", func.__module__)
        func(paths)
    print("Snapshots updated")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        copy(sys.argv[1])
    update()
