from logging import getLogger, DEBUG, WARNING, Formatter, StreamHandler
from sys import stdout

from _logging.formatters import DATE_FORMAT
from _logging.handlers import LOG_FILE_PATH
from _logging.handlers.json_file_handler import JsonFileHandler


def get_brief_formatter():
    return Formatter(
        "%(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s",
        datefmt=DATE_FORMAT
    )


def get_detailed_json_formatter():
    return Formatter(
        """
        {
            "Level": "%(levelname)s",
            "File": "%(filename)s",
            "Function": "%(funcName)s",
            "Line": "%(lineno)d",
            "Time": "%(asctime)s",
            "Message": "%(message)s"
        }
        """,
        datefmt=DATE_FORMAT
    )


def brief_console_config(logger_name, level=WARNING, propagate=False):
    # Setting the Formatter
    brief_formatter = get_brief_formatter()

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
