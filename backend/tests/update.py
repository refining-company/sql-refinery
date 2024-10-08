import tests.test_snapshots
import tests.conftest


if __name__ == "__main__":
    tests.test_snapshots.update_snapshots(tests.conftest.get_paths())
