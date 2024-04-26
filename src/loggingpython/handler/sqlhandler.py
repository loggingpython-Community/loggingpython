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
A class for handling log messages in SQL databases.

This class inherits from the Handler class and implements specific
methods for formatting and outputting log messages into SQL databases. It
supports the creation of new log databases based on the current date and
allows customization of the log format string. The SQLHandler ensures
that log messages are stored in a structured and easily accessible format,
making it suitable for further analysis or review. It also includes
features for updating the log database if the current date has changed and
for creating the necessary database structure.
"""

import os
from datetime import datetime
import sqlite3

from .handler import Handler


class SQLHandler(Handler):
    """
    A class for handling log messages in SQL databases.

    This class inherits from the Handler class and implements specific
    methods for formatting and outputting log messages into SQL databases. It
    supports the creation of new log databases based on the current date and
    allows customization of the log format string. The SQLHandler ensures
    that log messages are stored in a structured and easily accessible format,
    making it suitable for further analysis or review. It also includes
    features for updating the log database if the current date has changed and
    for creating the necessary database structure.
    """

    def __init__(self,
                 name: str,
                 path: str = "logs") -> None:
        """
        Initializes the SQLHandler with the given name, log path, and log
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
        self.file: str = f"{self.path}/{self.name}_{self._current_date}.db"
        self._mk_logfile(self.file)
        self._creat_db()

    def emit(self, record: dict) -> None:
        """
        Writes a log record to the database.

        Args:
            record (dict): A dictionary containing the log record details.
        """
        hash_message = hash(str(record))
        message = record.get("message", "")
        loglevel = record.get("loglevel", "")
        asctime = record.get("asctime", "")
        iso_8601_time = record.get("iso_8601_time", "")
        loggername = record.get("loggername", "")

        with sqlite3.connect(self.file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO logs (hash_message, message, loglevel, asctime, \
iso_8601_time, loggername)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (hash_message, message, loglevel, asctime, iso_8601_time,
                 loggername)
            )
            conn.commit()

    def _creat_db(self) -> None:
        with sqlite3.connect(self.file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS logs (
                    hash_message TEXT PRIMARY KEY,
                    message TEXT,
                    loglevel TEXT,
                    asctime TEXT,
                    iso_8601_time TEXT,
                    loggername TEXT
                )"""
            )
            conn.commit()

    def _update_file(self) -> None:
        """
        Updates the log file if the current date has changed.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != self._current_date:
            self._current_date = current_date
            self.file = f"{self.path}/{self.name}_{self._current_date}.db"
            self._mk_logfile(self.file)
            self._creat_db()

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
        return f"SQLHandler({self.name}, {self.path})"

    def __str__(self) -> str:
        return f"SQLHandler with:{self.name} and {self.path}"
