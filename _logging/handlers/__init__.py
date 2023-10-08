from .console_handler import ConsoleHandler
from .json_file_handler import JsonFileHandler


def _get_path():
    from os import getcwd
    from os.path import join

    _project_folder = getcwd()
    return join(_project_folder, "log.json")


def set_path(path: str):
    globals()["log_file_path"] = path


log_file_path = _get_path()
