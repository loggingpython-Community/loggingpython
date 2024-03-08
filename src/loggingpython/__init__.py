from .logger import Logger
from .filehandler import FileHandler
from .consolehandler import ConsoleHandler

from .log_levels import LogLevel

__version__ = "1.0.0"
__all__ = ["Logger", "FileHandler", "ConsoleHandler", "LogLevel"]

__author__ = "mrmajor.programmer"
__author_email__ = "mrmajork.programmer@gmail.com"
__license__ = "MIT"


def hello_from_loggingpython() -> None:
    """
    Outputs a welcome message containing information about the
    loggingpython community.
    """
    print(f"""Hello from the loggingpython-community.
version: {__version__}
PyPi: https://pypi.org/project/loggingpython
GitHub: https://github.com/loggingpython-Community/loggingpython""")


def getLogger() -> Logger:
    """
        Creates and returns an instance of the logger.

        Returns:
            Logger: An instance of the logger.
        """
    return Logger()


def getBasicLogger() -> Logger:
    """
    Creates a logger with predefined handlers for file and console output.
        console output.

    Returns:
        Logger: A logger with predefined handlers.
    """
    logger = getLogger()
    logger.addHandler(FileHandler(logger.name))
    logger.addHandler(ConsoleHandler())
    return logger


if __name__ != '__main__':
    hello_from_loggingpython()
