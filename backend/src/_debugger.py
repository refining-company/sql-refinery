"""Custom patch for debugpy to handle debugging in a multi-threaded environment.

It addresses issues with VSCode's debugpy when dealing with forked processes and ensures the backend can connect to the debugger without crashing the frontend.
"""

import time

import debugpy

import src

log = src.logger.get(__name__)


def connect_debugpy(host="localhost", port=5678, retry_interval=1, max_retries=10):
    for attempt in range(max_retries):
        try:
            log.info(f"Attempting to connect to debug server {attempt + 1} of {max_retries} attempts")
            debugpy.connect((host, port))
            log.info("Started custom debugger")
            break
        except ConnectionRefusedError:
            log.error(f"Failed to connect. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
    else:
        log.error(f"Failed to connect after {max_retries} attempts")


def start():
    connect_debugpy()
    debugpy.wait_for_client()
