from pytest import fixture

from _logging.configs.bc_djf_config import bc_djf_config
from _logging.loggers.logger import Logger


@fixture(scope="session", autouse=True)
def logger_configuration():
    bc_djf_config("test_logger")


@fixture
def log():
    return Logger("test_logger")


def test_logging():
    logger = log
    logger.info()
