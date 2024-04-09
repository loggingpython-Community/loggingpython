# Documentation for `log_levels.py`
## Overview
The `log_levels.py` file is a crucial component of the `loggingpython` package, providing a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `LogLevel` enum class defined in this file.

## `LogLevel` Enum Class
The `LogLevel` enum class is responsible for defining the various log levels that can be used within the logging system. It inherits from Python's built-in `Enum` class, which allows for the creation of enumerations with a set of symbolic names bound to unique, constant values. The `LogLevel` enum class defines five log levels, each representing a different severity of log messages.

## Enum Values
The `LogLevel` enum class includes the following log levels:

 - `DEBUG`: Represents detailed information, typically of interest only when diagnosing problems.
 - `INFO`: Represents informational messages that highlight the progress of the application at a coarse-grained level.
 - `WARNING`: Represents potentially harmful situations.
 - `ERROR`: Represents other runtime errors or unexpected conditions.
 - `CRITICAL`: Represents very serious error events that may prevent the application from continuing to run.

## Initialization
The `LogLevel` enum class is initialized with the five log levels mentioned above. Each log level is assigned a string value that corresponds to its name.
```python
from enum import Enum

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
```

## Usage
The `LogLevel` enum class can be used to specify the severity of log messages in the logging system. For example, when creating a logger or logging a message, the log level can be set to one of the defined levels to indicate the importance of the message.
```
from loggingpython.logger import Logger
from loggingpython.log_levels import LogLevel

# Create a logger with a specific log level
logger = Logger(min_loglevel=LogLevel.INFO)

# Log a message with a specific log level
logger.log(message="This is an informational message.", loglevel=LogLevel.INFO)
```

## Example
Here is a simple example of how to use the `LogLevel` enum class to log messages at different severity levels.
```python
from loggingpython.logger import Logger
from loggingpython.log_levels import LogLevel

# Create a logger
logger = Logger(name="my_logger")

# Log messages at different severity levels
logger._log(message="Debug message", loglevel=LogLevel.DEBUG)
logger._log(message="Information message", loglevel=LogLevel.INFO)
logger._log(message="Warning message", loglevel=LogLevel.WARNING)
logger._log(message="Error message", loglevel=LogLevel.ERROR)
logger._log(message="Critical message", loglevel=LogLevel.CRITICAL)
```
This example demonstrates how the `LogLevel` enum class can be used to specify the severity of log messages, allowing for a clear and consistent categorization of log data.

## Summary
The `LogLevel` enum class in `log_levels.py `provides a standardized way to represent and use log levels within the `loggingpython `package. By defining a set of predefined log levels, the logging system can be easily adapted to the specific requirements of each application, ensuring that log messages are categorized appropriately based on their severity.

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