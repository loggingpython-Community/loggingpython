FileHandler Documentation
=========================

The `FileHandler` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `FileHandler` class defined in this file.

Overview
--------

The `FileHandler` class is responsible for handling log messages by writing them to files. It inherits from the `Handler` class and implements specific methods for formatting and outputting log messages in files. It supports the creation of new log files based on the current date and allows the log format string to be customized. The `FileHandler` ensures that log messages are stored in a structured and easily accessible format, making them suitable for further analysis or review.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   init
   handler
   consolehandler
   csvhandler
   filehandler
   jsonhandler
   sqlhandler
   syshandler

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `FileHandler` class and its members within the `loggingpython.handler` module.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.handler.FileHandler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

A `FileHandler` object is initialized with a given name, a log path, and a log format string. By default, the path "logs" is used and the format string contains the timestamp, the name of the logger, the severity of the log message, and the message itself.

.. code-block:: python

    from loggingpython.handler.filehandler import FileHandler
    
    file_handler = FileHandler(name="my_log", path="logs", logformat_string="%(asctime)s: [%(loggername)s]: [%(loglevel)s]: %(message)s")

Variables
---------

- `name`: The name of the log file.
- `path`: The path in which the log files are saved.
- `logformat_string`: The format string for the log messages.
- `file`: The path to the current log file.

Methods
-------

- `emit(self, record: dict) -> None`: Writes a log data record to the file.
- `_update_file(self)`: Updates the log file if the current date has been changed.
- `_close_file(self)`: Closes the current log file.
- `_mk_logdir(self, logpath: str) -> None`: Creates the log directory if it does not exist.
- `_mk_logfile(self, file: str) -> None`: Creates the log file if it does not exist.
- `_get_datestemp(self) -> str`: Returns the current date in the format "YYYY-MM-DD".
- `_format_message(self, record: dict[str]) -> str`: Formats a log message based on the log data provided.

Example
-------

Here is a simple example of how to create a `FileHandler`, log a message, and close the log file.

.. code-block:: python

    from loggingpython.handler.filehandler import FileHandler
    
    # Create a FileHandler
    file_handler = FileHandler(name="my_log", path="logs")
    
    # Log a message
    file_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})
    
    # Close the log file
    file_handler._close_file()

Summary
-------

The `FileHandler` class in `FileHandler.py` provides a robust and flexible way to store log messages in files. By supporting the creation of new log files based on the current date and the customization of the log format string, the logging system can be adapted to the specific requirements of each application.

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