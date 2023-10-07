from json import load, dump, loads
from logging import LogRecord, Handler, NOTSET, getLogger
from os.path import isfile, getsize
from json.decoder import JSONDecodeError


class JsonFileHandler(Handler):
    def __init__(self, file_path, level=NOTSET):
        super().__init__(level)

        self.file_path = file_path

    def emit(self, record: LogRecord) -> None:
        for _ in range(2):  # Repeating once after validate_json
            try:
                str_log = self.format(record)

                with open(self.file_path, "r+") as file:
                    data = load(file)
                    data.append(loads(str_log))

                    file.seek(0)
                    dump(data, file)
                    return
            except (FileNotFoundError or JSONDecodeError) as err:
                getLogger().warning(f"Error Raised in json_file_handler.emit(): {err}\nCalling validate_json.")
                self.validate_json()

    def validate_json(self):
        if not isfile(self.file_path) or getsize(self.file_path) == 0:
            with open(self.file_path, "a") as file:
                dump([], file)
