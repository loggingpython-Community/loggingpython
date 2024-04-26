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
`loggingpython`

Enum class that represents the different log levels.

This class defines five enum members: DEBUG, INFO, WARNING, ERROR, and
CRITICAL, which represent the corresponding log levels used in logging.
DEBUG is the lowest level, used for detailed debugging information. INFO
is used for general information messages. WARNING is used for warning
messages. ERROR is used for error messages. CRITICAL is used for critical
error messages that may prevent the program from running.
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
