import logging
import sys

import src

formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s", datefmt="%H:%M:%S")

LOG_FILE = src.ROOT_DIR / "logs" / "backend.log"
LOG_FILE.parent.mkdir(exist_ok=True)


def _handle_exception(exc_type, exc_value, exc_traceback):
    """Log uncaught exceptions to file and stderr"""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.getLogger().critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def _setup(logger: logging.Logger) -> None:
    if not logger.hasHandlers():
        logger.handlers.clear()

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(formatter)
        logger.addHandler(stderr_handler)

        file_handler = logging.FileHandler(LOG_FILE, mode="w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)
    sys.excepthook = _handle_exception


_setup(logging.getLogger())


def get(name: str) -> logging.Logger:
    return logging.getLogger(name)
