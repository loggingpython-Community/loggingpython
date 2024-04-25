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
A class for handling log messages in CSV format.

This class inherits from the Handler class and implements specific
methods for formatting and outputting log messages in CSV files. It
supports the creation of new log files based on the current date and
allows customization of the log format string. The CSVHandler ensures
that log messages are stored in a structured and easily accessible format,
making it suitable for further analysis or review.
"""

import os
from datetime import datetime
import pandas as pd

from .handler import Handler


class CSVHandler(Handler):
    """
    A class for handling log messages in CSV format.

    This class inherits from the Handler class and implements specific
    methods for formatting and outputting log messages in CSV files. It
    supports the creation of new log files based on the current date and
    allows customization of the log format string. The CSVHandler ensures
    that log messages are stored in a structured and easily accessible format,
    making it suitable for further analysis or review.
    """

    def __init__(self,
                 name: str,
                 path: str = "logs",
                 logformat_string: str = "%(asctime)s: [%(loggername)s]: \
[%(loglevel)s]: %(message)s") -> None:
        """
        Initializes the CSVHandler with the given name, log path, and log
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
        self.file: str = f"{self.path}/{self.name}_{self._current_date}.csv"
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

        df = pd.DataFrame([formatted_message_values])

        formatted_message = df.to_csv(index=False, header=False, sep=";",
                                      lineterminator="\n")

        self._update_file()
        self.file.write(formatted_message)
        self.file.flush()

    def _update_file(self):
        """
        Updates the log file if the current date has changed.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != self._current_date:
            self.current_date = current_date
            self._close_file()
            filename = f"{self.logpath}/{self.name}_{self._current_date}.csv"
            self.file = open(filename, "a")

    def _close_file(self):
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
        return f"CSVHandler({self.name}, {self.path}, {self.logformat_string})"

    def __str__(self) -> str:
        return f"CSVHandler with: {self.name}, {self.path} and \
{self.logformat_string}"
