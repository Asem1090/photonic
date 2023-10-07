from logging import getLogger, DEBUG, WARNING, StreamHandler
from sys import stdout

from _logging.formatters import get_brief_formatter, get_colored_brief_formatter, get_detailed_json_formatter
from _logging.handlers import LOG_FILE_PATH
from _logging.handlers.json_file_handler import JsonFileHandler


def brief_console_config(logger_name, level=WARNING, propagate=False, colors_on=True):
    # Setting the Formatter
    brief_formatter = get_colored_brief_formatter() if colors_on else get_brief_formatter()

    # Setting up the Console Handler
    console_handler = StreamHandler(stream=stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(brief_formatter)

    # Setting up the logger
    logger = getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.propagate = propagate


def detailed_json_file_config(logger_name, level=DEBUG, propagate=False):
    detailed_json_formatter = get_detailed_json_formatter()

    # Setting up the json file handler
    file_handler = JsonFileHandler(LOG_FILE_PATH)
    file_handler.setLevel(level)
    file_handler.setFormatter(detailed_json_formatter)

    # Setting up the logger
    logger = getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.propagate = propagate
