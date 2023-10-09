from logging import getLogger
from uuid import uuid1

from _logging.configs import brief_console_config, detailed_json_file_config
from _logging.handlers import log_file_path
log_file_path = "C:\\Users\\asems\\OneDrive\\Desktop\\log.json"

def main():
    logger_name = "test_logger"

    # Configuring the logger
    # globals()["log_file_path"] = "C:\\Users\\asems\\OneDrive\\Desktop\\log.json"

    brief_console_config(logger_name)
    detailed_json_file_config(logger_name)

    print(f"Main func: {log_file_path}")

    logger = getLogger(logger_name)

    logger.debug(f"Test Message from logger.debug #{uuid1}")
    logger.info(f"Test Message from logger.info #{uuid1}")
    logger.warning(f"Test Message from logger.warning #{uuid1}")
    logger.error(f"Test Message from logger.error #{uuid1}")
    logger.critical(f"Test Message from logger.critical #{uuid1}")


if __name__ == "__main__":
    main()
