"""Logging configuration."""

import logging
import sys
from config.settings import Settings


def setup_logging() -> logging.Logger:
    """Configure and return the application logger."""
    logger = logging.getLogger("qa-generator")
    logger.setLevel(Settings.LOG_LEVEL)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(Settings.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger


logger = setup_logging()
