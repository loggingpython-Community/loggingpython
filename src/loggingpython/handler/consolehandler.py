from typing import TextIO
from colorama import Fore, Style
import sys

from .handler import Handler
from ..log_levels import LogLevel
from ..error.invalid_log_level_error import InvalidLogLevelError


class ConsoleHandler(Handler):
    """
    A class for handling log messages in the console.

    This class inherits from the Handler class and implements specific
    methods for formatting and outputting log messages in the console.
    It supports the coloring of log messages based on their
    severity and allows customization of the formatting string.
    """

    def __init__(self, stream: TextIO = sys.stdout,
                 logformat_string: str = "%(asctime)s: [%(loggername)s]: \
[%(loglevel)s]: %(message)s") -> None:
        """
        Initializes the ConsoleHandler with an optional stream and an optional
        optional formatting string for log messages.

        Args:
            stream (TextIO, optional): The stream into which the log messages
                are to be written. By default, this is sys.stdout.
            logformat_string (str, optional): The formatting string for the
                log messages. By default, it contains the timestamp,
                logger name, log level and the message itself.
        """
        self.stream: TextIO = stream
        self.logformat_string: str = logformat_string

        self.color_map: dict = {
            LogLevel.DEBUG.name: Fore.GREEN,
            LogLevel.INFO.name: Fore.CYAN,
            LogLevel.WARNING.name: Fore.YELLOW,
            LogLevel.ERROR.name: Fore.RED,
            LogLevel.CRITICAL.name: Fore.MAGENTA,
        }

    def emit(self, record: dict) -> None:
        """
        Outputs a formatted log message based on the transferred
        log data record log data set.

        Args:
            record (dict): A dictionary with the details of the log message,
                including timestamp, logger name, log level and message.
        """

        formatted_message_values = self._format_message(record)
        formatted_message = self.logformat_string % formatted_message_values

        color = self._get_color_for_level(record["loglevel"])
        self.stream.write(color + formatted_message + Style.RESET_ALL + '\n')
        self.stream.flush()

    def set_colors_for_levels(self, color_map: dict) -> None:
        """
        Sets colors for the different log levels.

        Args:
            color_map (dict): A dictionary that assigns log levels (as strings)
                to the corresponding colors from colorama.
        """
        for level in color_map.keys():
            if level not in LogLevel.__members__:
                raise InvalidLogLevelError(level)

        self.color_map.update(color_map)

    def _get_color_for_level(self, loglevel: str) -> str:
        """
        Returns the color for a specific log level.

        Args:
            loglevel (str): The log level for which the color is to
                be retrieved.

        Returns:
            str: The color for the given log level.
        """
        return self.color_map.get(loglevel, Fore.WHITE)

    def __repr__(self) -> str:
        return f"ConsoleHandler({self.name}, {self.logformat_string})"

    def __str__(self) -> str:
        return f"ConsoleHandler with: {self.name} and {self.logformat_string}"
