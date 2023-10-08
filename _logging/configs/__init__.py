from logging import getLogger, DEBUG, WARNING, StreamHandler, Formatter
from sys import stdout

from _logging.formatters import *
from _logging.handlers import *
from _logging.handlers.console_handler import ConsoleHandler
from _logging.loggers.logger import Logger


def brief_console_config(logger_name, level=WARNING, propagate_on=False, colors_on=True):
    # Setting the Formatter
    formatter = ColorFormatter if colors_on else Formatter
    brief_formatter = formatter(fmt=brief_format, datefmt=date_format)

    # Setting up the Console Handler
    console_handler = ConsoleHandler(level, brief_formatter)

    # Setting up the logger
    logger = getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.propagate = propagate_on


def detailed_console_config(logger_name, level=DEBUG, propagate_on=False, colors_on=True):
    # Setting the Formatter
    formatter = ColorFormatter if colors_on else Formatter
    detailed_formatter = formatter(fmt=detailed_format, datefmt=date_format)

    # Setting up the Console Handler
    console_handler = ConsoleHandler(level, detailed_formatter)

    # Setting up the logger
    logger = getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.propagate = propagate_on


def detailed_json_file_config(logger_name, level=DEBUG, propagate_on=False):
    # Setting up the json file handler
    file_handler = JsonFileHandler(LOG_FILE_PATH, level)

    # Setting up the logger
    logger = getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.propagate = propagate_on
