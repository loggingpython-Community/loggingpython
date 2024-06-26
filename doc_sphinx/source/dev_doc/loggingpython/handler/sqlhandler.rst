SQLHandler Documentation
========================

The `SQLHandler` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `SQLHandler` class defined in this file.

Overview
--------

The `SQLHandler` class is responsible for handling log messages in SQL databases. It inherits from the `Handler` class and implements specific methods for formatting and outputting log messages into SQL databases. It supports the creation of new log databases based on the current date and allows customization of the log format string. The `SQLHandler` ensures that log messages are stored in a structured and easily accessible format, making them suitable for further analysis or review.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `SQLHandler` class and its members within the `loggingpython.handler` module.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.handler.SQLHandler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

A `SQLHandler` object is initialized with a given name, a log path, and an optional log format string. By default, the path "logs" is used and the format string contains the timestamp, the name of the logger, the severity of the log message, and the message itself.

.. code-block:: python

    from loggingpython.handler.sqlhandler import SQLHandler
    
    sql_handler = SQLHandler(name="my_log", path="logs", logformat_string="%(asctime)s: [%(loggername)s]: [%(loglevel)s]: %(message)s")

Variables
---------

- `name`: The name of the log file.
- `path`: The path in which the log files are saved.
- `file`: The path to the current log file.
- `_current_date`: The current date in the format "YYYY-MM-DD", used for file rotation.

Methods
-------

- `emit(self, record: dict) -> None`: Writes a log data record to the database.
- `_creat_db(self) -> None`: Creates the necessary database structure if it does not exist.
- `_update_file(self) -> None`: Updates the log file if the current date has changed.
- `_close_file(self) -> None`: Closes the current log file.
- `_mk_logdir(self, logpath: str) -> None`: Creates the log directory if it does not exist.
- `_mk_logfile(self, file: str) -> None`: Creates the log file if it does not exist.
- `_get_datestemp(self) -> str`: Returns the current date in the format "YYYY-MM-DD".

Example
-------

Here is a simple example of how to create a `SQLHandler`, log a message, and close the log file.

.. code-block:: python

    from loggingpython.handler.sqlhandler import SQLHandler
    
    # Create a SQLHandler
    sql_handler = SQLHandler(name="my_log", path="logs")
    
    # Log a message
    sql_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})
    
    # Close the log file
    sql_handler._close_file()

Summary
-------

The `SQLHandler` class in `SQLHandler.py` provides a robust and flexible way to store log messages in SQL databases. By supporting the creation of new log databases based on the current date and the customization of the log format string, the logging system can be adapted to the specific requirements of each application. The inclusion of automatic file rotation based on the date ensures that log data is organized and easily accessible for analysis or review.

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