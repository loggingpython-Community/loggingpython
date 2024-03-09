from .logger import Logger
from .filehandler import FileHandler
from .consolehandler import ConsoleHandler
from .jsonhandler import JSONHandler

from .handler import Handler
from .log_levels import LogLevel


__version__ = "1.0.3s"
__all__ = ["Logger",
           "FileHandler",
           "ConsoleHandler",
           "JSONHandler",
           "LogLevel"]

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


def getLogger(name: str = "Root-Logger") -> Logger:
    """
        Creates and returns an instance of the logger.

        Returns:
            Logger: An instance of the logger.
        """
    return Logger(name)


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


def all_handlers() -> list:
    """
    Returns a list of all available handler classes.

    Returns:
        list: A list of all handler classes.
    """
    handlers = [FileHandler, ConsoleHandler, JSONHandler]
    handler_classes = []
    for cls in handlers:
        if issubclass(cls, Handler) and cls is not Handler:
            handler_classes.append(cls)
    return handler_classes


if __name__ != '__main__':
    hello_from_loggingpython()
