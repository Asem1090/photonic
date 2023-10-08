from logging import StreamHandler, WARNING, Formatter
from sys import stdout

from _logging.formatters import date_format, brief_format


class ConsoleHandler(StreamHandler):
    def __init__(self, level=WARNING, formatter=Formatter(brief_format, date_format)):
        super().__init__(stream=stdout)
        self.setLevel(level)
        self.setFormatter(formatter)
