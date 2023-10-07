from logging import DEBUG
from uuid import uuid1

from _logging.configs import brief_console_config, detailed_json_file_config, detailed_console_config
from _logging.loggers.logger import Logger


def main():
    logger_name = "test_logger"

    # Configuring the logger
    detailed_console_config(logger_name)
    # detailed_json_file_config(logger_name)

    logger = Logger(logger_name)
    logger.debug(f"Test Message from logger.debug #{uuid1}")
    logger.info(f"Test Message from logger.info #{uuid1}")
    logger.warning(f"Test Message from logger.warning #{uuid1}")
    logger.error(f"Test Message from logger.error #{uuid1}")
    logger.critical(f"Test Message from logger.critical #{uuid1}")


if __name__ == "__main__":
    main()
