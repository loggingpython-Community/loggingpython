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

Raised when a handler does not have the required 'emit' method.
This error indicates that the handler object passed to the logger does not
implement the 'emit' method, which is necessary for processing log
messages.
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
