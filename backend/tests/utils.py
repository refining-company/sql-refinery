import os
import inspect
from collections import defaultdict
from functools import wraps

captured_snapshots = defaultdict(list)


def start_snapshot_capture():
    captured_snapshots.clear()
    os.environ["CAPTURE_SNAPSHOTS"] = "true"


def capture_snapshot(fn_simplify: callable):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if os.getenv("CAPTURE_SNAPSHOTS") == "true":
                module = inspect.getmodule(func)
                if module is not None:
                    key = f"{module.__name__}:{func.__name__}"
                    simplified_result = fn_simplify(result)
                    captured_snapshots[key].append(simplified_result)

            return result

        return wrapper

    return decorator
