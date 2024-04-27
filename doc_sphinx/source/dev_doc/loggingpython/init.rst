loggingpython Module
====================

Overview
--------

The `loggingpython` module is a Python package that provides a simple and extensible way to integrate logging into your applications. The package starts with a basic logger and can be extended with additional functions to meet the requirements of your application.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the classes and functions defined in the `loggingpython` package.

.. automodule:: loggingpython
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autofunction:: loggingpython.hello_from_loggingpython
.. autofunction:: loggingpython.getLogger
.. autofunction:: loggingpython.getBasicLogger
.. autofunction:: loggingpython.get_all_handlers

Imported Modules and Classes
-----------------------------

The `__init__.py` file imports various modules and classes that are required for the logging system. These include:

- `Logger`: The main class for the logging system.
- Various handler classes (`FileHandler`, `ConsoleHandler`, `JSONHandler`, `SQLHandler`, `CSVHandler`, `SysHandler`), which are responsible for processing and outputting log messages.
- `LogLevel`: An enum class that defines the various log levels.
- `SysProtocolls`: A class that defines system logs.
- Error classes (`ServerUnreachableError`, `ServerMethodCallError`, `ClientMethodCallError`) that represent specific error types.

Functions
---------

- `hello_from_loggingpython()`: Outputs a welcome message containing information about the loggingpython community.
- `getLogger(name: str = "Root-Logger") -> Logger`: Creates and returns an instance of the logger.
- `getBasicLogger() -> Logger`: Creates a logger with predefined handlers for file and console output.
- `get_all_handlers() -> dict[str]`: Returns a dictionary of all available handler classes.

Examples
--------

### Creating a logger

To create a logger, use the `getLogger` function. You can optionally specify a name for the logger.

.. code-block:: python

   from loggingpython import getLogger

   logger = getLogger(name="my_logger")

### Adding a handler

To add a handler to the logger, use the `addHandler` method of the logger object.

.. code-block:: python

   from loggingpython.handler.consolehandler import ConsoleHandler

   logger.addHandler(ConsoleHandler())

### Logging a message

To log a message, use one of the methods of the logger object that correspond to the desired log level (`debug`, `info`, `warning`, `error`, `critical`).

.. code-block:: python

   logger.info("This is an information message.")

Summary
-------

The `__init__.py` file of the `loggingpython` package provides a robust and flexible way to implement logging in Python applications. By supporting different log levels and handlers, the logging system can be adapted to the specific requirements of each application.

License
-------

`loggingpython` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Further resources
-----------------

- [GitHub Repository](https://github.com/loggingpython-Community/loggingpython)
- [Issue Tracker](https://github.com/loggingpython-Community/loggingpython/issues)
- [Changelog](https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md)
- [PyPi](https://pypi.org/project/loggingpython/)

Social media
------------

- [GitHub](https://github.com/loggingpython-Community)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   error/init
   handler/init
   logger
   log_levels
   sys_protocolls