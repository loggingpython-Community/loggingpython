# Documentation for `FileHandler.py`
## Overview
The `FileHandler.py `file is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `FileHandler` class defined in this file.

## `FileHandler` Class
The `FileHandler` class is responsible for handling log messages in files. It inherits from the `Handler` class and implements specific methods for formatting and outputting log messages to files. It supports the creation of log files in a specified directory, automatic file rotation based on the current date, and allows customization of the formatting string. The `FileHandler` ensures that log messages are stored persistently and can be reviewed later for debugging or auditing purposes.

## Initialization
A `FileHandler` object is initialized with a given name, a log path, and a log format string. By default, the path "logs" is used and the format string contains the timestamp, the name of the logger, the severity of the log message, and the message itself.
```python
file_handler = FileHandler(name="my_log", path="logs", logformat_string="%(asctime)s: [%(loggername)s]: [%(loglevel)s]: %(message)s")
```

## Variables
 - `name`: The name of the log file.
 - `path`: The path in which the log files are saved.
 - `logformat_string`: The format string for the log messages.
 - `file`: The path to the current log file.
 - `_current_date`: The current date in the format "YYYY-MM-DD", used for file rotation.

## Methods
 - `emit(self, record: dict) -> None`: Writes a log data record to the file.
 - `_update_file(self) -> None`: Updates the log file if the current date has been changed.
 - `_close_file(self) -> None`: Closes the current log file.
 - `_mk_logdir(self, logpath: str) -> None`: Creates the log directory if it does not exist.
 - `_mk_logfile(self, file: str) -> None`: Creates the log file if it does not exist.
 - `_get_datestemp(self) -> str`: Returns the current date in the format "YYYY-MM-DD".
 - `_format_message(self, record: dict[str]) -> str`: Formats a log message based on the log data provided.

## Example
Here is a simple example of how to create a `FileHandler`, log a message, and close the log file.
```python
from loggingpython.handler.filehandler import FileHandler

# Create a FileHandler
file_handler = FileHandler(name="my_log", path="logs")

# Log a message
file_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})

# Close the log file
file_handler._close_file()
```

## Summary
The `FileHandler` class in `FileHandler.py` provides a robust and flexible way to store log messages in files. By supporting the creation of new log files based on the current date and the customization of the log format string, the logging system can be adapted to the specific requirements of each application.

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