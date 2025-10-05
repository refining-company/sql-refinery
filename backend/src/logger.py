import logging
import sys
from pathlib import Path

formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s", datefmt="%H:%M:%S")

log_dir = Path(__file__).parent.parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "backend.log"


class FlushHandler(logging.Handler):
    def __init__(self, stream):
        super().__init__()
        self.stream = stream

    def emit(self, record):
        msg = self.format(record)
        self.stream.write(msg + '\n')
        self.stream.flush()


def _setup(logger: logging.Logger) -> None:
    if not logger.hasHandlers():
        logger.handlers.clear()

        stderr_handler = FlushHandler(sys.stderr)
        stderr_handler.setFormatter(formatter)
        logger.addHandler(stderr_handler)

        file_handler = FlushHandler(open(log_file, 'w'))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)


_setup(logging.getLogger())


def get(name: str) -> logging.Logger:
    return logging.getLogger(name)
