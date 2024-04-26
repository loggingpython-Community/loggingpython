# MIT License
#
# Copyright (c) 2024 Mr-Major-K
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This module serves as the entry point for all handler classes within the
`loggingpython` package, specifically those responsible for directing
log messages to various destinations. Handlers are the core component of the
logging system, allowing log messages to be written to files, sent over
networks, or displayed on the console, among other destinations.

The handlers defined in this module are designed to be easily extendable and
customizable, providing a flexible framework for integrating logging into
Python applications. Each handler class is responsible for a specific type of
logging destination, such as file logging, console logging, or logging to
a database.

Example usage:

    from loggingpython.handler import FileHandler, ConsoleHandler

    # Set up a file handler
    file_handler = FileHandler('logfile.log')
    # Set up a console handler
    console_handler = ConsoleHandler()

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Log a message
    logger.info('This is an informational message.')

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
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
