# Built-in libs
from logging import Formatter

# Custom Libs
from _logging.formatters.color_formatter import ColorFormatter

date_format = "%Y-%m-%d %H:%M:%S"
brief_format = "%(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s"


def get_brief_formatter():
    return Formatter(fmt=brief_format, datefmt=date_format)


def get_colored_brief_formatter():
    return ColorFormatter(fmt=brief_format, datefmt=date_format)


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
        datefmt=date_format
    )
