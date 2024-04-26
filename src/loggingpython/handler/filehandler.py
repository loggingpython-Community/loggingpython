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
This module defines the `FileHandler` class, a component of the `loggingpython`
package designed to handle logging messages by writing them to a file. The
`FileHandler` class is a concrete implementation of the abstract `Handler`
class, providing the functionality to output log messages to a specified file.

The `FileHandler` class supports various file handling modes, such as
appending to an existing file or overwriting it, and can be configured with a
custom log format string to control the appearance of the log messages.

Example usage:

    from loggingpython.handler import FileHandler

    # Set up a file handler to append to a log file
    file_handler = FileHandler('logfile.log', mode='a')

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Log a message
    logger.info('This is an informational message.')

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""

import os
from datetime import timedelta
from datetime import datetime


from .handler import Handler


class FileHandler(Handler):
    """
    `loggingpython`

    A class for handling log messages in files.

    This class inherits from the Handler class and implements specific
    methods for formatting and outputting log messages to files. It supports
    the creation of log files in a specified directory, automatic file rotation
    based on the current date, and allows customization of the formatting
    string. The FileHandler ensures that log messages are stored persistently
    and can be reviewed later for debugging or auditing purposes.
    """

    def __init__(self,
                 name: str,
                 path: str = "logs",
                 logformat_string: str = "%(asctime)s: [%(loggername)s]: \
[%(loglevel)s]: %(message)s",
                 new_file_after: timedelta = timedelta(days=1)
                 ) -> None:
        """
        Initializes the FileHandler with the given name, log path, and log
            format string.

        Args:
            name (str): The name of the log file.
            path (str, optional): The path where the log files will be
                stored. Defaults to "logs".
            logformat_string (str, optional): The format string for the log
                messages. Defaults to "%(asctime)s: [%(loggername)s]:
                [%(loglevel)s]: %(message)s".
        """
        self._mk_logdir(path)
        self.name: str = name
        self.path: str = path
        self._current_date: str = datetime.now().strftime("%Y-%m-%d")
        self.file: str = f"{self.path}/{self.name}_{self._current_date}.log"
        self._mk_logfile(self.file)
        self.file = open(self.file, "a")

        self.logformat_string: str = logformat_string

    def emit(self, record: dict) -> None:
        """
        Writes a log record to the file.

        Args:
            record (dict): A dictionary containing the log record details.
        """
        formatted_message_values = self._format_message(record)
        formatted_message = self.logformat_string % formatted_message_values

        self._update_file()
        self.file.write(formatted_message + "\n")
        self.file.flush()

    def _update_file(self) -> None:
        """
        Updates the log file if the current date has changed.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != self._current_date:
            self.current_date = current_date
            self._close_file()
            filename = f"{self.logpath}/{self.name}_{self._current_date}.log"
            self.file = open(filename, "a")

    def _close_file(self) -> None:
        """
        Closes the current log file.
        """
        if self.file:
            self.file.close()

    def _mk_logdir(self, logpath: str) -> None:
        """
        Creates the log directory if it does not exist.

        Args:
            logpath (str): The path of the log directory.
        """
        if not os.path.exists(logpath):
            os.makedirs(logpath)

    def _mk_logfile(self, file: str) -> None:
        """
        Creates the log file if it does not exist.

        Args:
            file (str): The path of the log file.
        """
        if not os.path.exists(file):
            os.open(file, os.O_CREAT)

    def _get_datestemp(self) -> str:
        """
        Returns the current date in the format "YYYY-MM-DD".

        Returns:
            str: The current date.
        """
        return datetime.now().strftime("%Y-%m-%d")

    def __repr__(self) -> str:
        return f"FileHandler({self.name}, {self.path}, \
{self.logformat_string})"

    def __str__(self) -> str:
        return f"FileHandler with: {self.name}, {self.path} and \
{self.logformat_string}"
