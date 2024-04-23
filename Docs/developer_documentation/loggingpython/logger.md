# Documentation for `logger.py`
## Overview

The `logger.py` file is a central part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionalities and usage of the logger class defined in this file.

## Class `Logger`
The `Logger` class is the heart of the logging system. It provides methods for adding and removing handlers, for logging messages at different severity levels and for catching and logging exceptions.

## Initialization
A `Logger` object is initialized with a name, an optional time format and the minimum and maximum log severities.
```python
logger = Logger(name="my_logger", time_format="%Y-%m-%d %H:%M:%S", min_loglevel=LogLevel.INFO, max_loglevel=LogLevel.CRITICAL)
```

## Variables
`name`: The name of the logger.
`min_loglevel`: The minimum log level that is logged.
`max_loglevel`: The maximum log level that is logged.
`handlers`: A list of handlers that are responsible for processing and outputting log messages.
`iso_8601_format`: The format for timestamps in ISO 8601 format.
`time_format`: The user-defined format for timestamps.

## Methods
 - `_validate_loglevel(self, loglevel: LogLevel) -> None`:  Validates the passed log level. If an unsupported level is passed, a ValueError is triggered.

 - `_loglevel_over_min_loglevel(self, loglevel: LogLevel) -> bool`: Checks whether the transferred log level is above the minimum log level.

 - `_loglevel_under_max_loglevel(self, loglevel: LogLevel) -> bool`: Checks whether the transferred log level is below the maximum log level.

 - `_get_iso_8601_timestamp(self) -> str`: Returns the current timestamp in ISO 8601 format.

 - `_get_timestamp(self) -> str`: Returns the current timestamp in user-defined or ISO 8601 format.

 - `_format_message(self, message: str, loglevel: LogLevel) -> dict[str]`: Formats the log message with additional information such as timestamp, log level and logger name.

 - `addHandler(self, handler: Handler) -> None`: Adds a handler to the logger.

 - `removeHandler(self, handler: Handler) -> None`: Removes a handler from the logger.

 - `_log(self, message: str, loglevel: LogLevel = LogLevel.INFO) -> None`: Logs a message with the specified log level.

 - `debug(self, message: str) -> None`: Logs a message with the DEBUG level.

 - `info(self, message: str) -> None`: Logs a message with the INFO level.

 - `warning(self, message: str) -> None`: Logs a message with the WARNING level.

 - `error(self, message: str) -> None`: Logs a message with the ERROR level.

 - `critical(self, message: str) -> None`: Logs a message with the CRITICAL level.

 - `catch_debug(self, func)`: A decorator for catching and logging exceptions with the DEBUG level.

 - `catch_info(self, func)`: A decorator for catching and logging exceptions with the INFO level.

 - `catch_warning(self, func, except_type: BaseException = Exception)`: A decorator for catching and logging exceptions with the WARNING level.

 - `catch_error(self, func, except_type: BaseException = Exception)`: A decorator for catching and logging exceptions with the ERROR level.

 - `catch_critical(self, func, except_type: BaseException = Exception)`: A decorator for catching and logging exceptions with the CRITICAL level.

## Example
Here is a simple example of how to create a logger, add a handler and log messages at different severity levels.
```python
from loggingpython.logger import Logger
from loggingpython.handler.consolehandler import ConsoleHandler

# Create a logger
logger = Logger()

# Add a handler
logger.addHandler(ConsoleHandler())

# Logging messages
logger.info("The program is starting")
try:
    # Code that could throw an exception
    raise ValueError("An error has occurred")
except ValueError as e:
    logger.error(f "An error has occurred: {e}")
```

## Summary
The logger class in `logger.py` provides a robust and flexible way to implement logging in Python applications. By supporting different log levels and handlers, the logging system can be adapted to the specific requirements of each application.

---

## License

`loggingpython` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Further resources

- [GitHub Repository](https://github.com/loggingpython-Community/loggingpython)
- [Issue Tracker](https://github.com/loggingpython-Community/loggingpython/issues)
- [Changelog](https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md)
- [PyPi](https://pypi.org/project/loggingpython/)

## Social media

- [GitHub](https://github.com/loggingpython-Community)

---