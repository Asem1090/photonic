from json import load, dump
from logging import LogRecord, Handler, NOTSET

class JsonFileHandler(Handler):
    def __init__(self, file_path, level=NOTSET):
        super().__init__(level)

        self.file_path = file_path

    def emit(self, record: LogRecord) -> None:
        log = self.format(record)

        with open(self.file_path, "r+") as file:
            data = load(file)
            data.append(log)

            file.seek(0)
            dump(data, file)
