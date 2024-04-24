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
`loggingpython`
Raised when the client fails to establish a connection to the server.
This error indicates that the server might be unreachable due to network
issues, incorrect server address or port, or the server not being active.
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
