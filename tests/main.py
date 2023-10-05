import json
from uuid import uuid1

from _logging.configs.bc_djf_config import bc_djf_config
from _logging.loggers.logger import Logger


def main():
    with open("log.json", "a+") as file:
        json.load(file)
    # logger_name = "test_logger"
    # bc_djf_config(logger_name)
    # logger = Logger(logger_name)
    # logger.info(f"Test Message from logger.info #{uuid1}")


if __name__ == "__main__":
    main()
