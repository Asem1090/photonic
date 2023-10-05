from logging import getLogger, DEBUG, Formatter, StreamHandler, FileHandler
from sys import stdout
# from jsonformatter import jsonformatter

from _logging.formatters import DATE_FORMAT
from _logging.handlers import LOG_FILE_PATH
from _logging.handlers.json_file_handler import JsonFileHandler


def bc_djf_config(logger_name):
    # Formatters
    brief_formatter = Formatter(
        "%(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s",
        datefmt=DATE_FORMAT
    )

    json_detailed_formatter = Formatter(
        "{\n"  # Maybe stack_info is needed
        "\tLevel: %(levelname)s,\n"
        "\tFile: %(filename)s,\n"
        "\tFunction %(funcName)s,\n"
        "\tLine: %(lineno)d,\n"
        "\tTime: %(asctime)s,\n"
        "\tMessage: %(message)s,\n"
        "}",
        datefmt=DATE_FORMAT
    )

    # Handlers
    console_handler = StreamHandler(stream=stdout)
    console_handler.setLevel(DEBUG)
    console_handler.setFormatter(brief_formatter)

    file_handler = JsonFileHandler(LOG_FILE_PATH)
    file_handler.setLevel(DEBUG)
    file_handler.setFormatter(json_detailed_formatter)

    # Loggers
    logger = getLogger(logger_name)
    logger.setLevel(DEBUG)
    logger.propagate = False

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
