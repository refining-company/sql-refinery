import tests.test_codebase
import tests.test_logic
import tests.test_sql
import tests.conftest


def create_masters():
    create_funcs = [tests.test_codebase.create_masters, tests.test_logic.create_masters, tests.test_sql.create_masters]
    paths = tests.conftest.get_paths()

    print("Creating golden masters...")
    for func in create_funcs:
        print("\t", func.__module__)
        func(paths)
    print("Golder masters created")


if __name__ == "__main__":
    create_masters()
