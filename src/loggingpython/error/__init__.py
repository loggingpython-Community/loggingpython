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
This module serves as the entry point for all custom exception classes within
the `loggingpython` package, specifically those related to error handling in
the logging system. The exceptions defined here are designed to provide more
specific error information and handling capabilities for various
logging-related issues, such as invalid log levels, missing handlers, and
server/client method call errors.

The exceptions are organized into separate files for clarity and
maintainability, each focusing on a specific type of error. This modular
approach allows for easy extension and customization of the error handling
capabilities of the `loggingpython` package.

Example usage:

    from loggingpython.error import InvalidLogLevelError

    try:
        # Attempt to set an invalid log level
        logger.setLevel("INVALID_LEVEL")
    except InvalidLogLevelError as e:
        print(f"Error: {e}")

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""


from .server_unreachable_error import ServerUnreachableError
from .server_method_call_error import ServerMethodCallError
from .client_method_call_error import ClientMethodCallError
from .invalid_log_level_error import InvalidLogLevelError
from .invalid_handler_method_error import InvalidHandlerMethodError
from .handler_not_found_error import HandlerNotFoundError

__all__ = [
    "ServerUnreachableError",
    "ServerMethodCallError",
    "ClientMethodCallError",
    "InvalidLogLevelError",
    "InvalidHandlerMethodError",
    "HandlerNotFoundError"
    ]
