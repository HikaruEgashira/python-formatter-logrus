"""formatter-logrus.

A Python package for formatting colored logs.
"""
from __future__ import annotations

import logging
from typing import ClassVar


class Color:
    """A class for terminal colors."""

    BOLD = "\033[1m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD_WHITE = BOLD + WHITE
    BOLD_BLUE = BOLD + BLUE
    BOLD_GREEN = BOLD + GREEN
    BOLD_YELLOW = BOLD + YELLOW
    BOLD_RED = BOLD + RED
    END = "\033[0m"


class ColorLogFormatter(logging.Formatter):
    """A class for formatting colored logs.

    INFO[0000] A group of warlus.      acean=1, bcean=2, ccean=3
    WARN[0000] A group of warlus.      acean=1, bcean=2, ccean=3
    FATA[0000] The ice break!          acean=1, bcean=2, ccean=3
    """

    LOG_LEVEL_COLOR: ClassVar[dict[str, dict[str, str]]] = {
        "DEBUG": {"prefix": "", "suffix": ""},
        "INFO": {"prefix": "", "suffix": ""},
        "WARNING": {"prefix": Color.BOLD_YELLOW, "suffix": Color.END},
        "ERROR": {"prefix": Color.BOLD_RED, "suffix": Color.END},
        "CRITICAL": {"prefix": Color.BOLD_RED, "suffix": Color.END},
    }
    log_format: ClassVar[str] = "%(prefix)s%(msg)s%(suffix)s"

    def format(self, record: logging.LogRecord) -> str:  # noqa: A003
        """Format a log record and return the formatted string."""
        if not hasattr(record, "prefix"):
            record.prefix = self.LOG_LEVEL_COLOR.get(record.levelname.upper(), {}).get("prefix")

        if not hasattr(record, "suffix"):
            record.suffix = self.LOG_LEVEL_COLOR.get(record.levelname.upper(), {}).get("suffix")

        formatter = logging.Formatter(self.log_format)
        return formatter.format(record)
