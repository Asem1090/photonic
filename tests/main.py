from uuid import uuid1

from _logging.configs import brief_console_config, detailed_json_file_config
from _logging.loggers.logger import Logger


def main():
    logger_name = "test_logger"

    # Configuring the logger
    brief_console_config(logger_name)
    detailed_json_file_config(logger_name)

    logger = Logger(logger_name)
    logger.warning(f"Test Message from logger.info #{uuid1}")


if __name__ == "__main__":
    main()
