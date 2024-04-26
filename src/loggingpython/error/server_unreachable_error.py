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
This module defines a custom exception class `ServerUnreachableError` for
handling errors related to the inability to establish a connection to a
server. This exception is part of the `loggingpython` package, designed to
ensure that network issues, incorrect server addresses or ports, or server
inactivity are correctly identified and handled.

The `ServerUnreachableError` class inherits from the built-in `Exception`
class, allowing it to be raised and caught like any other exception. It takes
a server name and port as parameters, which are used to construct a
descriptive error message indicating the server that could not be reached.

Example usage:

    try:
        # Attempt to connect to a server that is not reachable
        connect_to_server("unreachable.server", 1234)
    except ServerUnreachableError as e:
        print(f"Error: {e}")

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""


class ServerUnreachableError(Exception):
    """
    `loggingpython`

    Raised when the client fails to establish a connection to the server.
    This error indicates that the server might be unreachable due to network
    issues, incorrect server address or port, or the server not being active.
    """
    def __init__(self, servername: str, port: int):
        message: str = f"Failed to connect to the server: {servername}:{port}"
        super().__init__(message)
