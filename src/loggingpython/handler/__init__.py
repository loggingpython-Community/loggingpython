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
    >>> file_handler = FileHandler('logfile.log')
    >>> file_handler.log('This is a log message.')

    >>> from loggingpython.handler import ConsoleHandler
    >>> console_handler = ConsoleHandler()
    >>> console_handler.log('This is a log message.')

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
