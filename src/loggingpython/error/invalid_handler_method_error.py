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
This module defines a custom exception class `InvalidHandlerMethodError` for
handling errors related to handlers that do not implement the required 'emit'
method. This exception is part of the `loggingpython` package, designed to
ensure that all handlers used in the logging system are correctly implemented
and capable of processing log messages.

The `InvalidHandlerMethodError` class inherits from the built-in `TypeError`
class, allowing it to be raised and caught like any other exception. It takes
a handler object as a parameter, which is used to construct a descriptive
error message indicating the handler class that failed to implement the 'emit'
method.

Example usage:

    try:
        # Attempt to add a handler that does not implement the 'emit' method
        logger.addHandler(some_invalid_handler)
    except InvalidHandlerMethodError as e:
        print(f"Error: {e}")

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""

from ..handler.handler import Handler


class InvalidHandlerMethodError(TypeError):
    """
    `loggingpython`

    Raised when a handler does not have the required 'emit' method.
    This error indicates that the handler object passed to the logger does not
    implement the 'emit' method, which is necessary for processing log
    messages.
    """
    def __init__(self, handler: Handler):
        message: str = f"Handler '{handler.__class__.__name__}' must have an \
'emit' method"
        super().__init__(message)
