from logging import Handler, LogRecord
from os.path import getsize

from _logging.handlers import LOG_FILE_PATH


class JsonFileHandler(Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if getsize(LOG_FILE_PATH) == 0:
            self.logIsEmpty = True
        else:
            self.logIsEmpty = False

    def emit(self, record: LogRecord) -> None:
        if self.logIsEmpty:
            record.msg = ",\n" + record.msg
            self.logIsEmpty = False

        super().emit(record)
