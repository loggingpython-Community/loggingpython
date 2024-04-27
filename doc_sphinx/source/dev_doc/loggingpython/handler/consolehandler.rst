ConsoleHandler Documentation
============================

The `ConsoleHandler` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `ConsoleHandler` class defined in this file.

Overview
--------

The `ConsoleHandler` class is responsible for handling log messages in the console. It inherits from the `Handler` class and implements specific methods for formatting and outputting log messages in the console. It supports the coloring of log messages based on their severity and allows customization of the formatting string. The `ConsoleHandler` ensures that log messages are displayed in real-time, making it suitable for debugging and monitoring applications during development or runtime.

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

The following sections automatically generate documentation for the `ConsoleHandler` class and its members within the `loggingpython.handler` module.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.handler.ConsoleHandler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

A `ConsoleHandler` object is initialized with an optional stream and an optional formatting string for log messages. By default, `sys.stdout` is used as the stream and the formatting string contains the timestamp, the name of the logger, the severity of the log message, and the message itself.

.. code-block:: python

    from loggingpython.handler.consolehandler import ConsoleHandler
    
    console_handler = ConsoleHandler(stream=sys.stdout, logformat_string="%(asctime)s: [%(loggername)s]: [%(loglevel)s]: %(message)s")

Variables
---------

- `stream`: The stream in which the log messages are written. By default `sys.stdout`.
- `logformat_string`: The formatting string for the log messages.
- `color_map`: A mapping of log levels to colors from colorama to color the log messages based on their severity.

Methods
-------

- `emit(self, record: dict) -> None`: Outputs a formatted log message based on the passed log record.
- `set_colors_for_levels(self, color_map: dict) -> None`: Sets colors for the different log levels.
- `_get_color_for_level(self, loglevel: str) -> str`: Returns the color for a specific log level.
- `_format_message(self, record: dict[str]) -> str`: Formats a log message based on the transferred log data record.

Example
-------

Here is a simple example of how to create a `ConsoleHandler`, add it to a logger, and log messages at different severity levels.

.. code-block:: python

    from loggingpython.logger import Logger
    from loggingpython.handler.consolehandler import ConsoleHandler
    
    # Create a ConsoleHandler
    console_handler = ConsoleHandler()
    
    # Log a message
    console_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})

Summary
-------

The `ConsoleHandler` class in `ConsoleHandler.py` provides a robust and flexible way to display log messages in the console. By supporting different log levels and colors, the logging system can be adapted to the specific requirements of each application, making it suitable for both development and production environments.

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