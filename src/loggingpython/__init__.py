"""
`loggingpython` is a Python package that provides a simple and extensible way
 to integrate logging into your applications. The package starts with a basic
 logger and can be extended with additional functions to meet the requirements
of your application.

Look at the Docs for more in
"""


from .logger import Logger
from .filehandler import FileHandler
from .consolehandler import ConsoleHandler
from .jsonhandler import JSONHandler
from .sqlhandler import SQLHandler
from .csvhandler import CSVHandler

from .handler import Handler
from .log_levels import LogLevel


__version__ = "1.1.2"
__all__ = ["Logger",
           # Hander
           "Handler",
           "FileHandler",
           "ConsoleHandler",
           "JSONHandler",
           "SQLHandler",
           "CSVHandler",
           # help class
           "LogLevel"]

__license__ = "MIT"


def hello_from_loggingpython() -> None:
    """
    Outputs a welcome message containing information about the
    loggingpython community.
    """
    print(f"""Hello from the loggingpython-community.
We also use other libs, for a list of all libs look here: \
https://github.com/loggingpython-Community/loggingpython/wiki/Lib-List
Version: {__version__}
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


def get_all_handlers() -> dict:
    """
    Returns a dictionary of all available handler classes.

    Returns:
        dict: A dictionary where keys are the handler names and values are
            the handler classes.
    """
    handlers = {}
    for handler_name in __all__:
        if handler_name.endswith("Handler"):
            module_name = f"{__name__}.{handler_name.lower()}"
            handler_module = __import__(module_name, fromlist=[handler_name])
            handler_class = getattr(handler_module, handler_name)
            handlers[handler_name] = handler_class
    return handlers


if __name__ != '__main__':
    hello_from_loggingpython()
