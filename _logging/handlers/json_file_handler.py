from json import load, dump
from logging import LogRecord, Handler, NOTSET


class JsonFileHandler(Handler):
    def __init__(self, file_name, level=NOTSET):
        super().__init__(level)

        self.file_name = file_name

        with open(file_name, mode="a+"):
            ...

    def emit(self, record: LogRecord) -> None:
        logs = load(self.file_name)
        print(logs)
        print(record)
        print(record.msg)

