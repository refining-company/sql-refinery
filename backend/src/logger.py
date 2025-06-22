import logging
import sys

import pygls.server

formatter = logging.Formatter("[backend:%(name)s] %(message)s")


class FlushStreamHandler(logging.StreamHandler):
    # FIXME: This ensures each message is flushed to stderr immediately, however is ugly and likely the bug is on the VSCode end
    def emit(self, record):
        super().emit(record)
        sys.stderr.write("")
        self.flush()


def _setup(logger: logging.Logger, level=logging.DEBUG) -> None:
    # All intentional logging via stderr => Extension Output panel
    # RPC communication via stdin => Debug Console

    if not logger.hasHandlers():
        logger.handlers.clear()
        handler = FlushStreamHandler(sys.stderr)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)


_setup(pygls.server.logger, level=logging.ERROR)


def get(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    _setup(logger)
    return logger
