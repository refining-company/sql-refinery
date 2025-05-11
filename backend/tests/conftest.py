import difflib


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, str) and isinstance(right, str) and op == "==" and (left + right).count("\n") >= 5:
        diff = list(difflib.unified_diff(left.splitlines(), right.splitlines(), lineterm="", n=0))
        return ["Strings are not equal:"] + diff
