import os
import json
from datetime import datetime

from .handler import Handler


class JSONHandler(Handler):
    def __init__(self, name: str, path: str = "logs") -> None:
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
        self.file: str = f"{self.path}/{self.name}_{self._current_date}.json"
        self._mk_logfile(self.file)
        # Initialisieren Sie das JSON-Objekt hier
        self.log_data = {}

    def emit(self, record: dict) -> None:
        """
        Fügt eine Log-Nachricht zum JSON-Objekt hinzu und überprüft, ob das
            Datum geändert wurde.

        Args:
            record (dict): Ein Wörterbuch, das die Details des Log-Eintrags
                enthält.
        """
        # Generieren Sie einen Hash für die Log-Nachricht
        message_hash = hash(str(record))
        # Fügen Sie die Log-Nachricht zum JSON-Objekt hinzu
        self.log_data[str(message_hash)] = record
        # Überprüfen Sie, ob das Datum geändert wurde und aktualisieren Sie
        # die Datei entsprechend
        self._update_file()
        # Schreiben Sie das JSON-Objekt in die Datei
        self._write_log_data_to_file()

    def _write_log_data_to_file(self) -> None:
        """
        Writes the JSON object to the file.
        """
        with open(self.file, 'w') as file:
            file.write(json.dumps(self.log_data, indent=4))

    def _update_file(self):
        """
        Updates the log file if the current date has changed.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != self._current_date:
            self._current_date = current_date
            self._close_file()
            filename = f"{self.path}/{self.name}_{self._current_date}.json"
            self.file = open(filename, "a")
            # Reset log_data for the new file
            self.log_data = {}

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

        return self._format_in_json(values)

    def _format_in_json(self, record: dict) -> dict:
        """
        Formats a log message based on the provided log data into a JSON
            object with hashed keys.

        Args:
            record (dict): A dictionary containing the log message details.

        Returns:
            dict: The formatted log message as a JSON object with hashed keys.
        """
        sorted_keys = sorted(record.keys())
        string_representation = str({key: record[key] for key in sorted_keys})
        message_hash = hash(string_representation)
        values = {
            message_hash: record,
        }
        return values

    def __repr__(self) -> str:
        return f"JSONHandler:{self.name}, {self.path}, {self.logformat_string}"

    def __str__(self) -> str:
        return f"JSONHandler:{self.name}, {self.path}, {self.logformat_string}"
