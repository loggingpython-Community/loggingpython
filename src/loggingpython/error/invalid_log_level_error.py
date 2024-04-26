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
This module defines a custom exception class `InvalidLogLevelError` for
handling errors related to the specification of an invalid log level. This
exception is part of the `loggingpython` package, designed to ensure that
log levels are correctly specified and recognized by the logging system.

The `InvalidLogLevelError` class inherits from the built-in `ValueError`
class, allowing it to be raised and caught like any other exception. It takes
a log level string as a parameter, which is used to construct a descriptive
error message indicating the invalid log level.

Example usage:

    try:
        # Attempt to set an invalid log level
        logger.setLevel("INVALID_LEVEL")
    except InvalidLogLevelError as e:
        print(f"Error: {e}")

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""


class InvalidLogLevelError(Exception):
    """
    `loggingpython`

    Raised when an invalid log level is specified.
    This error indicates that the provided log level does not match any of the
    supported log levels.
    """
    def __init__(self, log_level: str) -> None:
        message: str = f"Invalid log level specified: {log_level}"
        super().__init__(message)
