from .json_file_handler import JsonFileHandler


def _get_path():
    from os import getcwd
    from os.path import join

    _project_folder = getcwd()
    return join(_project_folder, "log.json")


LOG_FILE_PATH = _get_path()
