"""
`loggingpython` is a Python package that provides a simple and extensible way
 to integrate logging into your applications. The package starts with a basic
 logger and can be extended with additional functions to meet the requirements
of your application.

In the Docs you will find further information about.
"""


from .logger import Logger
from .handler.filehandler import FileHandler
from .handler.consolehandler import ConsoleHandler
from .handler.jsonhandler import JSONHandler
from .handler.sqlhandler import SQLHandler
from .handler.csvhandler import CSVHandler

from .handler import Handler
from .log_levels import LogLevel


import importlib


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
    logger: Logger = getLogger()
    logger.addHandler(FileHandler(logger.name))
    logger.addHandler(ConsoleHandler())
    return logger


def get_all_handlers() -> dict[str]:
    """
    Returns a dictionary of all available handler classes.

    Returns:
        dict: A dictionary where keys are the handler names and values are
            the handler classes.
    """
    handlers = {}
    for handler_name in __all__:
        if handler_name.endswith("Handler"):
            # Adjust the module name to correctly resolve the import path
            module_name = f"{__name__}.handler.{handler_name.lower()}"
            try:
                # Use importlib.import_module for dynamic import
                handler_module = importlib.import_module(module_name)
                handler_class = getattr(handler_module, handler_name)
                handlers[handler_name] = handler_class
            except ModuleNotFoundError as e:
                print(f"Failed to import {handler_name}: {e}")
    return handlers


if __name__ != '__main__':
    hello_from_loggingpython()
