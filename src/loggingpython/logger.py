from datetime import datetime, timezone

from .log_levels import LogLevel
from .handler import Handler


class Logger:
    """
    Simple logger class for custom logging functionality.
    """

    _SUPPORTED_LEVELS: list = list(LogLevel)

    def __init__(self, name: str = "Root-Logger",
                 time_format: str = None,
                 min_loglevel: LogLevel = LogLevel.INFO,
                 max_loglevel: LogLevel = LogLevel.CRITICAL) -> None:

        self.name: str = name
        self.min_loglevel: LogLevel = min_loglevel
        self.max_loglevel: LogLevel = max_loglevel

        self.handlers: list[Handler] = []

        self.iso_8601_format: str = "%Y-%m-%dT%H:%M:%S.%f%z"
        self.time_format: str = time_format

    def _validate_loglevel(self, loglevel: LogLevel) -> None:
        """
        Validates the provided log level.

        Args:
            loglevel (LogLevel): The log level to be validated.

        Raises:
            ValueError: If the loglevel is not supported.
        """

        if loglevel not in self._SUPPORTED_LEVELS:
            raise ValueError

    def _loglevel_over_min_loglevel(self, loglevel: LogLevel) -> bool:
        """
        Checks if the provided log level is over the minimum log level.

        Args:
            loglevel (LogLevel): The log level to check.

        Returns:
            bool: True if the log level is over the minimum, False otherwise.
        """
        return self._SUPPORTED_LEVELS.index(loglevel) >= \
            self._SUPPORTED_LEVELS.index(self.min_loglevel)

    def _loglevel_under_max_loglevel(self, loglevel: LogLevel) -> bool:
        """
        Checks if the provided log level is under the maximum log level.

        Args:
            loglevel (LogLevel): The log level to check.

        Returns:
            bool: True if the log level is under the maximum, False otherwise.
        """
        return self._SUPPORTED_LEVELS.index(loglevel) <= \
            self._SUPPORTED_LEVELS.index(self.min_loglevel)

    def _get_iso_8601_timestamp(self) -> str:
        """
        Returns the current timestamp in a formatted string in ISO 8601.

        Returns:
            str: The current timestamp in ISO 8601 format.
        """

        return datetime.now(timezone.utc).strftime(self.iso_8601_format)

    def _get_timestamp(self) -> None:
        """
        Returns the current timestamp in a formatted string.

        Returns:
            str: The current timestamp in the specified format.
        """
        if self.time_format is not None:
            return datetime.now(timezone.utc).strftime(self.time_format)
        return self._get_iso_8601_timestamp()

    def _format_message(self, message: str, loglevel: LogLevel) -> dict:
        """
        Formats the log message with additional information.

        Args:
            message (str): The message to log.
            loglevel (LogLevel): The log level of the message.

        Returns:
            dict: A dictionary containing the formatted log message.
        """
        values = {
            "message": message,
            "loglevel": loglevel.name,
            "asctime": self._get_timestamp(),
            "iso_8601_time": self._get_iso_8601_timestamp(),
            "loggername": self.name,
        }
        return values

    def addHandler(self, handler: Handler) -> None:
        """
        Adds a handler to the logger.

        Args:
            handler (Handler): An object that implements the 'emit' method,
                responsible for handling log messages.
        """
        if not hasattr(handler, "emit"):
            raise TypeError("Handler must have an 'emit' method")
        self.handlers.append(handler)

    def removeHandler(self, handler: Handler) -> None:
        """
        Removes a handler from the logger.

        Args:
            handler (Handler): The handler to be removed.

        Raises:
            ValueError: If the handler is not found in the logger's handlers.
        """
        if handler not in self.handlers:
            raise ValueError("Handler not found in logger's handlers.")
        self.handlers.remove(handler)

    def _log(self, message: str, loglevel: LogLevel = LogLevel.INFO) -> None:
        """
        Logs a message with the specified log level and includes
            a full traceback.

        Args:
            message (str): The message to log.
            loglevel (LogLevel, optional): The log level. Defaults to INFO.
                Must be one of the supported levels:
                DEBUG, INFO, WARNING, ERROR, CRITICAL.

        Raises:
            ValueError: If the level is not supported.
        """
        try:
            self._validate_loglevel(loglevel)
            if self._loglevel_over_min_loglevel(loglevel):
                if self._loglevel_under_max_loglevel(loglevel):
                    formatted_message = self._format_message(message, loglevel)
                    for handler in self.handlers:
                        handler.emit(formatted_message)
        except ValueError as e:
            self.error(f"ValueError: {e}")

    def debug(self, message: str) -> None:
        """
        Logs a message at the DEBUG level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.DEBUG)

    def info(self, message: str) -> None:
        """
        Logs a message at the INFO level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.INFO)

    def warning(self, message: str) -> None:
        """
        Logs a message at the WARNING level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.WARNING)

    def error(self, message: str) -> None:
        """
        Logs a message at the ERROR level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.ERROR)

    def critical(self, message: str) -> None:
        """
        Logs a message at the CRITICAL level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """
        self._log(message, loglevel=LogLevel.CRITICAL)
