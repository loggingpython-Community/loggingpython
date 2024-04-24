# MIT License

# Copyright (c) 2024 Mr-Major-K

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
`loggingpython` is a Python package that provides a simple and extensible way
 to integrate logging into your applications. The package starts with a basic
 logger and can be extended with additional functions to meet the requirements
of your application.

This module contains various handler classes that can be used for different
types of logging purposes, including file, console, JSON, SQL, CSV and system
logging.

Examples:
    >>> from loggingpython.handler import FileHandler
    >>> file_handler = FileHandler('myLogger')
    >>> file_handler.emit('This is a log message.')

    >>> from loggingpython.handler import ConsoleHandler
    >>> console_handler = ConsoleHandler()
    >>> console_handler.emit('This is a log message.')

In the Docs you will find further information about.
"""

import importlib

from .logger import Logger

from .log_levels import LogLevel
from .sys_protocolls import SysProtocolls

from .handler.filehandler import FileHandler
from .handler.consolehandler import ConsoleHandler
from .handler.jsonhandler import JSONHandler
from .handler.sqlhandler import SQLHandler
from .handler.csvhandler import CSVHandler
from .handler.syshandler import SysHandler

from .error.server_unreachable_error import ServerUnreachableError
from .error.server_method_call_error import ServerMethodCallError
from .error.client_method_call_error import ClientMethodCallError
from .error.invalid_log_level_error import InvalidLogLevelError
from .error.invalid_handler_method_error import InvalidHandlerMethodError
from .error.handler_not_found_error import HandlerNotFoundError


__version__ = "1.4.1"
__all__ = [
    # Bacis
    "Logger",

    # Enum
    "LogLevel",
    "SysProtocolls",

    # Hander
    "Handler",
    "FileHandler",
    "ConsoleHandler",
    "JSONHandler",
    "SQLHandler",
    "CSVHandler",
    "SysHandler",

    # Error
    "ServerUnreachableError",
    "ServerMethodCallError",
    "ClientMethodCallError",
    "InvalidLogLevelError",
    "InvalidHandlerMethodError",
    "HandlerNotFoundError"
    ]

__license__ = "MIT"


def hello_from_loggingpython() -> None:
    """
    Outputs a welcome message containing information about the
    loggingpython community.
    """
    print(f"""
Hello from the loggingpython-community.
We also use other libs, for a list of all libs look here: \
https://github.com/loggingpython-Community/loggingpython/wiki/Lib-List
Version: {__version__}
GitHub: https://github.com/loggingpython-Community/loggingpython
""")


def getLogger(name: str = "Root-Logger",
              time_format: str = None,
              min_loglevel: LogLevel = None,
              max_loglevel: LogLevel = None) -> Logger:
    """
    Creates and returns an instance of the logger.

    Returns:
        Logger: An instance of the logger.
    """
    return Logger(name=name,
                  time_format=time_format,
                  min_loglevel=min_loglevel,
                  max_loglevel=max_loglevel)


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
            module_name = f"{__name__}.handler.{handler_name.lower()}"
            try:
                handler_module = importlib.import_module(module_name)
                handler_class = getattr(handler_module, handler_name)
                handlers[handler_name] = handler_class
            except ModuleNotFoundError as e:
                print(f"Failed to import {handler_name}: {e}")
    return handlers


if __name__ != '__main__':
    hello_from_loggingpython()
