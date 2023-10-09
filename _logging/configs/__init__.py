from logging import getLogger, DEBUG, WARNING, Formatter, Handler

from _logging.formatters import *
from _logging.handlers import *


def console_config(
        logger_name: str, fmt=brief_format, level=WARNING, propagate: bool = False, colors: bool = True
) -> None:
    formatter = ColorFormatter if colors else Formatter
    _formatter = formatter(fmt=fmt, datefmt=date_format)

    console_handler = ConsoleHandler(level, _formatter)

    setup_logger(logger_name, level, console_handler, propagate)


def json_file_config(logger_name: str, fmt=detailed_json_format, level=DEBUG, propagate: bool = False) -> None:
    file_handler = JsonFileHandler(log_file_path, level, Formatter(fmt=fmt, datefmt=date_format))

    setup_logger(logger_name, level, file_handler, propagate)


def setup_logger(name: str, level, handler: Handler, propagate: bool) -> None:
    logger = getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = propagate
