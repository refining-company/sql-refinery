"""Custom patch for debugpy to handle debugging in a multi-threaded environment.

It addresses issues with VSCode's debugpy when dealing with forked processes and ensures the backend can connect to the debugger without crashing the frontend.
"""

import sys
import debugpy
import time


def connect_debugpy(host="localhost", port=5678, retry_interval=1, max_retries=10):
    for attempt in range(max_retries):
        try:
            print(f"Attempting to connect to debug server: Attempt {attempt + 1}/{max_retries}", file=sys.stderr)
            debugpy.connect((host, port))
            print("Started custom debugger", file=sys.stderr)
            break
        except ConnectionRefusedError:
            print(f"Failed to connect. Retrying in {retry_interval} seconds...", file=sys.stderr)
            time.sleep(retry_interval)
    else:
        print(f"Failed to connect after {max_retries} attempts.", file=sys.stderr)


connect_debugpy()
debugpy.wait_for_client()
