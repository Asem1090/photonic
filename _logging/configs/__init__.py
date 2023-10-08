from logging import getLogger, DEBUG, WARNING, Formatter, Handler

from _logging.formatters import *
from _logging.handlers import *


def brief_console_config(logger_name: str, level=WARNING, propagate: bool = False, colors: bool = True) -> None:
    formatter = ColorFormatter if colors else Formatter
    brief_formatter = formatter(fmt=brief_format, datefmt=date_format)

    console_handler = ConsoleHandler(level, brief_formatter)

    setup_logger(logger_name, level, console_handler, propagate)


def detailed_console_config(logger_name: str, level=DEBUG, propagate: bool = False, colors: bool = True) -> None:
    formatter = ColorFormatter if colors else Formatter
    detailed_formatter = formatter(fmt=detailed_format, datefmt=date_format)

    console_handler = ConsoleHandler(level, detailed_formatter)

    setup_logger(logger_name, level, console_handler, propagate)


def detailed_json_file_config(logger_name: str, level=DEBUG, propagate: bool = False) -> None:
    file_handler = JsonFileHandler(log_file_path, level)

    setup_logger(logger_name, level, file_handler, propagate)


def setup_logger(name: str, level, handler: Handler, propagate: bool) -> None:
    logger = getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = propagate
