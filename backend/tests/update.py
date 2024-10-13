import tests.test_pipeline
import tests.conftest


if __name__ == "__main__":
    tests.test_pipeline.update_snapshots(tests.conftest.get_paths())
