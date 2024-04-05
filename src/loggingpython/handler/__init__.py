"""
`loggingpython` is a Python package that provides a simple and extensible way
 to integrate logging into your applications. The package starts with a basic
 logger and can be extended with additional functions to meet the requirements
of your application.

In the Docs you will find further information about.
"""

from .handler import Handler

from .filehandler import FileHandler
from .consolehandler import ConsoleHandler
from .jsonhandler import JSONHandler
from .sqlhandler import SQLHandler
from .csvhandler import CSVHandler
from .syshandler import SysHandler


__all__ = ["Handler",
           "FileHandler",
           "ConsoleHandler",
           "JSONHandler",
           "SQLHandler",
           "CSVHandler",
           "SysHandler"]
