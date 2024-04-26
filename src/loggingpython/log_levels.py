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
This module defines the `LogLevel` class, an enumeration of the different
log levels used within the `loggingpython` package. Log levels are a
fundamental aspect of logging, allowing developers to categorize log messages
by their severity or importance. This module provides a clear and consistent
way to specify log levels across the application, ensuring that log messages
are handled appropriately based on their level.

The `LogLevel` class includes five levels: DEBUG, INFO, WARNING, ERROR, and
CRITICAL. These levels are used to indicate the severity of the log message,
with DEBUG being the lowest level and CRITICAL being the highest. This
classification helps in filtering log messages based on their importance,
allowing for more efficient debugging and monitoring of the application.

Example usage:

    from loggingpython.log_levels import LogLevel

    # Set the log level to INFO
    logger.setLevel(LogLevel.INFO)

    # Log a message at the INFO level
    logger.info('This is an informational message.')

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
The focus here is on defining and using log levels to ensure clear and
effective logging practices.
"""

from enum import Enum


class LogLevel(Enum):
    """
    `loggingpython`

    Enum class that represents the different log levels.

    This class defines five enum members: DEBUG, INFO, WARNING, ERROR, and
    CRITICAL, which represent the corresponding log levels used in logging.
    DEBUG is the lowest level, used for detailed debugging information. INFO
    is used for general information messages. WARNING is used for warning
    messages. ERROR is used for error messages. CRITICAL is used for critical
    error messages that may prevent the program from running.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
