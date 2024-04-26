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
This module defines a custom exception class `HandlerNotFoundError` for
handling errors related to the absence of a specified handler in a logger's
handlers list. This exception is part of the `loggingpython` package, designed
to ensure that operations related to logging handlers are performed safely and
correctly.

The `HandlerNotFoundError` class inherits from the built-in `ValueError`
class, allowing it to be raised and caught like any other exception. It takes
an optional message parameter that defaults to "Handler not found in logger's
handlers." This message is passed to the base class constructor to provide a
descriptive error message when the exception is raised.

Example usage:

    try:
        # Attempt to remove a handler that does not exist in the logger's
        # handlers
        logger.removeHandler(some_handler)
    except HandlerNotFoundError as e:
        print(f"Error: {e}")

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""


class HandlerNotFoundError(ValueError):
    """
    `loggingpython`

    Raised when a handler is not found in the logger's handlers.
    This error indicates that the specified handler was not added to the
    logger, and therefore cannot be removed.
    """
    def __init__(self,
                 message="Handler not found in logger's handlers.") -> None:
        super().__init__(message)
