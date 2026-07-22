import logging

from pythonjsonlogger.json import JsonFormatter


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    handler = logging.StreamHandler()

    formatter = JsonFormatter(
        "%(asctime)s %(levelname)s %(filename)s %(lineno)d %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)