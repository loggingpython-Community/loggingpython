JSONHandler Documentation
=========================

The `JSONHandler` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `JSONHandler` class defined in this file.

Overview
--------

The `JSONHandler` class is responsible for handling log messages in JSON format. It inherits from the `Handler` class and implements specific methods for formatting and outputting log messages in JSON files. It supports the creation of new log files based on the current date and allows customization of the log format string. The `JSONHandler` ensures that log messages are stored in a structured and easily accessible format, making them suitable for further analysis or review.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `JSONHandler` class and its members within the `loggingpython.handler` module.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: loggingpython.handler.JSONHandler
   :members:
   :undoc-members:
   :show-inheritance:

Initialization
--------------

A `JSONHandler` object is initialized with a given name, a log path, and an optional log format string. By default, the path "logs" is used and the format string contains the timestamp, the name of the logger, the severity of the log message, and the message itself.

.. code-block:: python

    from loggingpython.handler.jsonhandler import JSONHandler
    
    json_handler = JSONHandler(name="my_log", path="logs", logformat_string="%(asctime)s: [%(loggername)s]: [%(loglevel)s]: %(message)s")

Variables
---------

- `name`: The name of the log file.
- `path`: The path in which the log files are saved.
- `logformat_string`: The format string for the log messages.
- `file`: The path to the current log file.
- `_current_date`: The current date in the format "YYYY-MM-DD", used for file rotation.
- `log_data`: A dictionary that holds the log data to be written to the file.

Methods
-------

- `emit(self, record: dict) -> None`: Adds a log message to the JSON object and checks whether the date has been changed.
- `_write_log_data_to_file(self) -> None`: Writes the JSON object to the file.
- `_update_file(self) -> None`: Updates the log file if the current date has changed.
- `_close_file(self) -> None`: Closes the current log file.
- `_mk_logdir(self, logpath: str) -> None`: Creates the log directory if it does not exist.
- `_mk_logfile(self, file: str) -> None`: Creates the log file if it does not exist.
- `_get_datestemp(self) -> str`: Returns the current date in the format "YYYY-MM-DD".
- `_format_message(self, record: dict[str]) -> str`: Formats a log message based on the provided log data.
- `_format_in_json(self, record: dict[str]) -> dict`: Formats a log message based on the provided log data into a JSON object with hashed keys.

Example
-------

Here is a simple example of how to create a `JSONHandler`, log a message, and close the log file.

.. code-block:: python

    from loggingpython.handler.jsonhandler import JSONHandler
    
    # Create a JSONHandler
    json_handler = JSONHandler(name="my_log", path="logs")
    
    # Log a message
    json_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})
    
    # Close the log file
    json_handler._close_file()

Summary
-------

The `JSONHandler` class in `JSONHandler.py` provides a robust and flexible way to store log messages in JSON files. By supporting the creation of new log files based on the current date and the customization of the log format string, the logging system can be adapted to the specific requirements of each application. The inclusion of hashing for unique identification and automatic file rotation based on the date ensures that log data is organized and easily accessible for analysis or review.

License
-------

`loggingpython` is licensed under the `MIT License <https://opensource.org/licenses/MIT>`_.

Further Resources
-----------------

- `GitHub Repository <https://github.com/loggingpython-Community/loggingpython>`_
- `Issue Tracker <https://github.com/loggingpython-Community/loggingpython/issues>`_
- `Changelog <https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md>`_
- `PyPi <https://pypi.org/project/loggingpython/>`_

Social Media
-------------

- `GitHub <https://github.com/loggingpython-Community>`_