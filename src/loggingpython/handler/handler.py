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
This module defines the `Handler` class, the base class for all handler
implementations within the `loggingpython` package. Handlers are responsible
for processing log messages, directing them to various destinations such as
files, consoles, databases, or external services.

The `Handler` class provides a common interface for all handler subclasses,
requiring them to implement the `emit` method. This method is responsible for
the actual processing of log messages, allowing for a wide range of custom
handling behaviors.

Subclasses of `Handler` can be used to implement specific logging behaviors,
such as writing to files, sending messages over the network, or storing
log data in databases. Each subclass must provide its own implementation of
the `emit` method to define how log messages are handled.

Example usage:

    from loggingpython.handler import Handler, FileHandler

    class CustomHandler(Handler):
        def emit(self, record):
            # Custom handling logic here
            pass

    # Using the custom handler
    custom_handler = CustomHandler()
    logger.addHandler(custom_handler)

    # Log a message
    logger.info('This is an informational message.')

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""


class Handler:
    """
    `loggingpython`

    Base class for all handlers.

    This class defines the interface for all handler classes. Handlers are
    responsible for processing log messages. Subclasses must implement the
    emit method to provide specific handling behavior.
    """

    def emit(self, record: dict) -> None:
        """
        Emits a log message.

        This method is intended to be overridden by subclasses to provide
        specific handling behavior for log messages. The base class raises
        a NotImplementedError to indicate that subclasses must implement this
        method.

        Parameters:
        - message (str): The log message to be processed.

        Raises:
        - NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this!")

    def _format_message(self, record: dict) -> str:
        """
        Formats a log message based on the transferred log data set.

        Args:
            record (dict): A dictionary with the details of the log message.

        Returns:
            str: The formatted log message.
        """
        values = {
            "loggername": record.get("loggername", ""),
            "iso_8601_time": record.get("iso_8601_time", ""),
            "asctime": record.get("asctime", ""),
            "loglevel": record.get("loglevel", ""),
            "message": record.get("message", ""),
        }

        return values

    def __repr__(self) -> str:
        return "Handler()"

    def __str__(self) -> str:
        return "Handler with: None"
