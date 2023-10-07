from logging import Formatter, LogRecord

from .color_enum import Color


class ColorFormatter(Formatter):
    color_map = {
        "DEBUG": Color.GREY,
        "INFO": Color.BLUE,
        "WARNING": Color.YELLOW,
        "ERROR": Color.RED,
        "CRITICAL": Color.BOLD_RED
    }

    def format(self, record: LogRecord) -> str:
        log = super().format(record)
        colored_log = ColorFormatter.color_map[record.levelname].value + log + Color.RESET.value

        return colored_log
