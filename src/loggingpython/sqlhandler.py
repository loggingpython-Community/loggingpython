import os
from datetime import datetime
import sqlite3

from .handler import Handler


class SQLHandler(Handler):
    def __init__(self, name: str, path: str = "logs") -> None:
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
        # Extrahieren Sie die Werte aus dem Log-Record
        hash_message = hash(str(record))
        message = record.get("message", "")
        loglevel = record.get("loglevel", "")
        asctime = record.get("asctime", "")
        iso_8601_time = record.get("iso_8601_time", "")
        loggername = record.get("loggername", "")

        # Fügen Sie die Log-Nachricht in die Datenbank ein
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

    def _update_file(self):
        """
        Updates the log file if the current date has changed.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != self._current_date:
            self._current_date = current_date
            # Therefore, no explicit closing action is required here
            # Update the file name for the new database file
            self.file = f"{self.path}/{self.name}_{self._current_date}.db"
            # Create the new database file if it does not yet exist
            self._mk_logfile(self.file)
            # Create the table in the new db file if it does not yet exist
            self._creat_db()

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

    def _format_message(self, record: dict) -> str:
        """
        Formats a log message based on the provided log data.

        Args:
            record (dict): A dictionary containing the log message details.

        Returns:
            str: The formatted log message.
        """
        values = {
            "message": record.get("message", ""),
            "loglevel": record.get("loglevel", ""),
            "asctime": record.get("asctime", ""),
            "iso_8601_time": record.get("iso_8601_time", ""),
            "loggername": record.get("loggername", ""),
        }

        return values

    def __repr__(self) -> str:
        return f"SQLHandler:{self.name}, {self.path}"

    def __str__(self) -> str:
        return f"SQLHandler:{self.name}, {self.path}"
