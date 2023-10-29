"""test."""
import io
import logging

from formatter_logrus import formatter


def test_overview() -> None:
    """動作テスト."""
    stream_io = io.StringIO()
    stream = logging.StreamHandler(stream=stream_io)
    stream.setFormatter(formatter.ColorLogFormatter())
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")

    assert stream_io.getvalue() == "debug message\ninfo message\nwarning message\nerror message\n"
    for line in stream_io.getvalue().splitlines():
        assert line.endswith("message")
