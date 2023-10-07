def get_path():
    from os import getcwd
    from os.path import join

    _project_folder = getcwd()
    return join(_project_folder, "log.json")


LOG_FILE_PATH = get_path()
