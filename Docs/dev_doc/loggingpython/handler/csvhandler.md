# Documentation for `CSVHandler.py`
## Overview
The `CSVHandler.py` file is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `CSVHandler` class defined in this file.

## `CSVHandler` class
The `CSVHandler` class is responsible for handling log messages in CSV format. It inherits from the `Handler` class and implements specific methods for formatting and outputting log messages in CSV files. It supports the creation of new log files based on the current date and allows the log format string to be customized. The `CSVHandler` ensures that log messages are stored in a structured and easily accessible format, making them suitable for further analysis or review.

## Initialization
A `CSVHandler` object is initialized with a given name, a log path and a log format string. By default, the path "logs" is used and the format string contains the timestamp, the name of the logger, the severity of the log message and the message itself.
```python
csv_handler = CSVHandler(name="my_log", path="logs", logformat_string="%(asctime)s: [%(loggername)s]: [%(loglevel)s]: %(message)s")
```

## Variables
 - `name`: The name of the log file.
 - `path`: The path in which the log files are saved.
 - `logformat_string`: The format string for the log messages.
 - `file`: The path to the current log file.

## Methods
 - `emit(self, record: dict) -> None`: Writes a log data record to the file.
 - `_update_file(self)`: Updates the log file if the current date has been changed.
 - `_close_file(self)`: Closes the current log file.
 - `_mk_logdir(self, logpath: str) -> None`: Creates the log directory if it does not exist.
 - `_mk_logfile(self, file: str) -> None`: Creates the log file if it does not exist.
 - `_get_datestemp(self) -> str`: Returns the current date in the format "YYYY-MM-DD".
 - `_format_message(self, record: dict[str]) -> str`: Formats a log message based on the log data provided.

## Example
Here is a simple example of how to create a `CSVHandler`, log a message and close the log file.
```python
from loggingpython.handler.csvhandler import CSVHandler

# Create a CSVHandler
csv_handler = CSVHandler(name="my_log", path="logs")

# Log a message
csv_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})

# Close the log file
csv_handler._close_file()
```

## Summary
The `CSVHandler` class in `CSVHandler.py` provides a robust and flexible way to store log messages in CSV files. By supporting the creation of new log files based on the current date and the customization of the log format string, the logging system can be adapted to the specific requirements of each application.

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