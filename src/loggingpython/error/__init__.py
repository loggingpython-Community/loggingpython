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

This module contains functions and classes used for error handling in the
`loggingpython` library.

It provides specific error classes for different types of errors that can
occur during interaction with a server or the execution of methods on the
client.

Example:
    >>> from loggingpython.error import ServerUnreachableError
    >>> try:
    ...     # Code that could trigger a ServerUnreachableError
    ... except ServerUnreachableError as e:
    ...     print(f “Server could not be reached: {e}”)

In the Docs you will find further information about.
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
