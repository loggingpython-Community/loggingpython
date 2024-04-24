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
A class for handling log messages in a structured and extensible way.

This class, `Logger`, is designed to provide a simple and customizable
logging solution for Python applications. It inherits from a base `Handler`
class and implements specific methods for formatting and outputting log
messages. The `Logger` class supports various log levels, including DEBUG,
INFO, WARNING, ERROR, and CRITICAL, allowing for detailed and flexible
logging.

The `Logger` class is equipped with methods for adding and removing
handlers, which are responsible for processing and outputting log messages.
Handlers can be customized to output log messages to various destinations,
such as the console, files, databases, or external systems. This
extensibility makes the `Logger` class suitable for a wide range of
applications, from simple scripts to complex systems.

The `Logger` class also includes methods for logging messages at different
severity levels, ensuring that developers can easily categorize and
prioritize log messages based on their importance. Additionally, the class
provides a mechanism for catching exceptions and logging them,
facilitating error handling and debugging.

In summary, the `Logger` class offers a straightforward and powerful way
to integrate logging into Python applications, providing a foundation for
both basic and advanced logging requirements.
"""

from datetime import datetime, timezone

from .log_levels import LogLevel
from .handler import Handler
from .error.invalid_log_level_error import InvalidLogLevelError
from .error.invalid_handler_method_error import InvalidHandlerMethodError
from .error.handler_not_found_error import HandlerNotFoundError


class Logger:
    """
    A class for handling log messages in a structured and extensible way.

    This class, `Logger`, is designed to provide a simple and customizable
    logging solution for Python applications. It inherits from a base `Handler`
    class and implements specific methods for formatting and outputting log
    messages. The `Logger` class supports various log levels, including DEBUG,
    INFO, WARNING, ERROR, and CRITICAL, allowing for detailed and flexible
    logging.

    The `Logger` class is equipped with methods for adding and removing
    handlers, which are responsible for processing and outputting log messages.
    Handlers can be customized to output log messages to various destinations,
    such as the console, files, databases, or external systems. This
    extensibility makes the `Logger` class suitable for a wide range of
    applications, from simple scripts to complex systems.

    The `Logger` class also includes methods for logging messages at different
    severity levels, ensuring that developers can easily categorize and
    prioritize log messages based on their importance. Additionally, the class
    provides a mechanism for catching exceptions and logging them,
    facilitating error handling and debugging.

    In summary, the `Logger` class offers a straightforward and powerful way
    to integrate logging into Python applications, providing a foundation for
    both basic and advanced logging requirements.
    """

    _SUPPORTED_LEVELS: list = list(LogLevel)

    def __init__(self, name: str,
                 time_format: str = None,
                 min_loglevel: LogLevel = LogLevel.INFO,
                 max_loglevel: LogLevel = LogLevel.CRITICAL) -> None:
        """
        Initializes the Logger with the given name, time format, and log
        levels.

        Args:
            name (str): The name of the logger.
            time_format (str, optional): The format string for the log
                timestamps. Defaults to None, which uses the ISO 8601 format.
            min_loglevel (LogLevel, optional): The minimum log level to be
                logged. Defaults to LogLevel.INFO.
            max_loglevel (LogLevel, optional): The maximum log level to be
                logged. Defaults to LogLevel.CRITICAL.

        Raises:
            InvalidLogLevelError: If the provided log levels are not supported.
        """

        if min_loglevel in LogLevel:
            self.min_loglevel: LogLevel = min_loglevel

        else:
            self.min_loglevel: LogLevel = LogLevel.INFO

        if min_loglevel in LogLevel:
            self.min_loglevel: LogLevel = min_loglevel

        else:
            self.min_loglevel: LogLevel = LogLevel.CRITICAL

        self.name: str = name
        
        self.handlers: list[Handler] = []

        self.iso_8601_format: str = "%Y-%m-%dT%H:%M:%S.%f%z"
        self.time_format: str = time_format

    def _validate_loglevel(self, loglevel: LogLevel) -> None:
        """
        Validates the provided log level.

        Args:
            loglevel (LogLevel): The log level to be validated.

        Raises:
            InvalidLogLevelError: If the loglevel is not supported.
        """

        if loglevel not in self._SUPPORTED_LEVELS:
            raise InvalidLogLevelError(loglevel)

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
            self._SUPPORTED_LEVELS.index(self.max_loglevel)

    def _get_iso_8601_timestamp(self) -> str:
        """
        Returns the current timestamp in a formatted string in ISO 8601.

        Returns:
            str: The current timestamp in ISO 8601 format.
        """

        return datetime.now(timezone.utc).strftime(self.iso_8601_format)

    def _get_timestamp(self) -> str:
        """
        Returns the current timestamp in a formatted string.

        Returns:
            str: The current timestamp in the specified format.
        """
        if self.time_format is not None:
            return datetime.now(timezone.utc).strftime(self.time_format)
        return self._get_iso_8601_timestamp()

    def _format_message(self, message: str, loglevel: LogLevel) -> dict[str]:
        """
        Formats the log message with additional information.

        Args:
            message (str): The message to log.
            loglevel (LogLevel): The log level of the message.

        Returns:
            dict: A dictionary containing the formatted log message.
        """
        values = {
            "loggername": self.name,
            "iso_8601_time": self._get_iso_8601_timestamp(),
            "asctime": self._get_timestamp(),
            "loglevel": loglevel.name,
            "message": message,
        }
        return values

    def addHandler(self, handler: Handler) -> None:
        """
        Adds a handler to the logger.

        Args:
            handler (Handler): An object that implements the 'emit' method,
                responsible for handling log messages.

        Raises:
            InvalidHandlerMethodError: If the handler does not have the
                required 'emit' method.
        """
        if not hasattr(handler, "emit"):
            raise InvalidHandlerMethodError()
        self.handlers.append(handler)

    def removeHandler(self, handler: Handler) -> None:
        """
        Removes a handler from the logger.

        Args:
            handler (Handler): The handler to be removed.

        Raises:
            HandlerNotFoundError: If the handler is not found in the logger's
                handlers.
        """
        if handler not in self.handlers:
            raise HandlerNotFoundError()
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

    def catch_debug(self, func):
        """
        A decorator for catching exceptions and logging them at the DEBUG
        level.

        This method is a decorator that wraps a function, catches any
        exceptions thrown by the function, logs the exception at the DEBUG
        level, and then re-raises the exception. This is useful for debugging
        purposes, as it allows developers to see the exceptions that occur
        during the execution of a function without stopping the program.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: The decorated function.
    """
        def wrapper(*args, **kwargs):
            try:
                self.debug(f"func '{func.__name__}' with {args}, {kwargs}")
                result = func(*args, **kwargs)
                self.debug(f"func '{func.__name__}' completed successfully, \
with '{result}'")
                return result
            except Exception as e:
                self.error(f"{func.__name__} failed with error: {str(e)}")
        return wrapper

    def catch_info(self, func):
        """
        A decorator for catching exceptions and logging them at the INFO level.

        This method is a decorator that wraps a function, catches any
        exceptions thrown by the function, logs the exception at the INFO
        level, and then re-raises the exception. This is useful for
        informational purposes, as it allows developers to see the exceptions
        that occur during the execution of a function without stopping the
        program.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: The decorated function.
        """
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                self.info(f"func '{func.__name__}' completed successfully, \
with '{result}'")
                return result
            except Exception as e:
                self.error(f"{func.__name__} failed with error: {str(e)}")
        return wrapper

    def catch_warning(self, func, except_type: BaseException = Exception):
        """
        A decorator for catching exceptions and logging them at the WARNING
        level.

        This method is a decorator that wraps a function, catches any
        exceptions thrown by the function, logs the exception at the WARNING
        level, and then re-raises the exception. This is useful for warning
        purposes, as it allows developers to see the exceptions that occur
        during the execution of a function without stopping the program.

        Args:
            func (callable): The function to be decorated.
            except_type (BaseException, optional): The type of exception to
                catch. Defaults to Exception, which catches all exceptions
                that inherit from BaseException.

        Returns:
            callable: The decorated function.

        Raises:
            TypeError: If except_type is not a class that inherits from
            BaseException.
        """
        if not isinstance(except_type, type) or not issubclass(except_type,
                                                               BaseException):
            raise TypeError("except_type must be a class that inherits from \
BaseException")

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except except_type as e:
                self.warning(f"{func.__name__} failed with error: {str(e)}")
        return wrapper

    def catch_error(self, func, except_type: BaseException = Exception):
        """
        A decorator for catching exceptions and logging them at the ERROR
        level.

        This method is a decorator that wraps a function, catches any
        exceptions thrown by the function, logs the exception at the ERROR
        level, and then re-raises the exception. This is useful for error
        handling purposes, as it allows developers to see the exceptions that
        occur during the execution of a function without stopping the program.

        Args:
            func (callable): The function to be decorated.
            except_type (BaseException, optional): The type of exception to
                catch. Defaults to Exception, which catches all exceptions
                that inherit from BaseException.

        Returns:
            callable: The decorated function.

        Raises:
            TypeError: If except_type is not a class that inherits from
            BaseException.
        """
        if not isinstance(except_type, type) or not issubclass(except_type,
                                                               BaseException):
            raise TypeError("except_type must be a class that inherits from \
BaseException")

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except except_type as e:
                self.error(f"{func.__name__} failed with error: {str(e)}")
        return wrapper

    def catch_critical(self, func, except_type: BaseException = Exception):
        """
        A decorator for catching exceptions and logging them at the CRITICAL
        level.

        This method is a decorator that wraps a function, catches any
        exceptions thrown by the function, logs the exception at the CRITICAL
        level, and then re-raises the exception. This is useful for critical
        error handling purposes, as it allows developers to see the exceptions
        that occur during the execution of a function without stopping the
        program.

        Args:
            func (callable): The function to be decorated.
            except_type (BaseException, optional): The type of exception to
                catch. Defaults to Exception, which catches all exceptions
                that inherit from BaseException.

        Returns:
            callable: The decorated function.

        Raises:
            TypeError: If except_type is not a class that inherits from
            BaseException.
        """
        if not isinstance(except_type, type) or not issubclass(except_type,
                                                               BaseException):
            raise TypeError("except_type must be a class that inherits from \
BaseException")

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except except_type as e:
                self.critical(f"{func.__name__} failed with error: {str(e)}")
        return wrapper

    def __repr__(self) -> str:
        return f"Logger({self.name}, {self.time_format}, {self.min_loglevel}, \
{self.max_loglevel})"

    def __str__(self) -> str:
        return f"Logger with: {self.name}, {self.min_loglevel} and \
{self.max_loglevel}"
