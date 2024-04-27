API Reference for `loggingpython`
=================================

The `loggingpython` package provides a simple and extensible way to integrate logging into Python applications. This documentation serves as an API reference, detailing the main components and their functionalities.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   contribute
   api_reference
   changelog
   license

Package Structure
-----------------

The package is structured into several modules, each serving a specific purpose within the logging system. The main components include:

- `__init__.py`: The entry point for the package, exposing the main logger class and various handler classes.
- `handler/`: Contains handler classes for different types of logging, such as `FileHandler`, `ConsoleHandler`, `JSONHandler`, `SQLHandler`, `CSVHandler`, and `SysHandler`.
- `error/`: Contains error classes for handling exceptions, such as `ServerUnreachableError`, `ServerMethodCallError`, `ClientMethodCallError`, `InvalidLogLevelError`, `InvalidHandlerMethodError`, and `HandlerNotFoundError`.

Main Components
---------------

`__init__.py`

The `__init__.py` file within the `loggingpython` package serves as an entry point for the package. It imports and exposes the various handler classes available within the `loggingpython` package, providing a convenient way for users to access and utilize these handlers for logging purposes.

### Imported Modules and Classes

- `Logger`: The main class for the logging system.
- Various handler classes (`FileHandler`, `ConsoleHandler`, `JSONHandler`, `SQLHandler`, `CSVHandler`, `SysHandler`), which are responsible for processing and outputting log messages.
- `LogLevel`: An enum class that defines the various log levels.
- `SysProtocolls`: A class that defines system logs.
- Error classes (`ServerUnreachableError`, `ServerMethodCallError`, `ClientMethodCallError`) that represent specific error types.

### Functions

- `getLogger(name: str = "Root-Logger") -> Logger`: Creates and returns an instance of the logger.
- `getBasicLogger() -> Logger`: Creates a logger with predefined handlers for file and console output.
- `get_all_handlers() -> dict[str]`: Returns a dictionary of all available handler classes.

`handler/__init__.py`

The `__init__.py` file within the `handler` folder of the `loggingpython` package serves as an entry point for the handler module. It imports and exposes the various handler classes available within the `loggingpython` package, providing a convenient way for users to access and utilize these handlers for logging purposes.

### Imported Modules and Classes

- `Handler`: The base class for all handlers in the loggingpython package.
- `FileHandler`: Handles log messages by writing them to files.
- `ConsoleHandler`: Handles log messages by outputting them to the console.
- `JSONHandler`: Handles log messages by formatting them in JSON and writing them to files.
- `SQLHandler`: Handles log messages by storing them in a SQL database.
- `CSVHandler`: Handles log messages by formatting them in CSV and writing them to files.
- `SysHandler`: Handles log messages by sending them to the system's logging facility.

`error/__init__.py`

The `__init__.py` file within the `error` folder of the `loggingpython` package serves as an entry point for the error module. It imports and exposes the various error classes available within the `loggingpython` package, providing a convenient way for users to access and utilize these errors for handling exceptions in their applications.

### Imported Modules and Classes

- `ServerUnreachableError`: Raised when the server is unreachable.
- `ServerMethodCallError`: Raised when there is an error calling a method on the server.
- `ClientMethodCallError`: Raised when there is an error calling a method on the client.
- `InvalidLogLevelError`: Raised when an invalid log level is specified.
- `InvalidHandlerMethodError`: Raised when an invalid handler method is called.
- `HandlerNotFoundError`: Raised when a specified handler is not found.

Example Usage
-------------

To use the `loggingpython` package, you first need to import the specific components you wish to use. Here's an example of how to import and use the `Logger` and `ConsoleHandler`:

.. code-block:: python

    from loggingpython import getLogger
    from loggingpython.handler.consolehandler import ConsoleHandler
    
    # Create a logger instance
    logger = getLogger(name="my_logger")
    
    # Add a ConsoleHandler to the logger
    logger.addHandler(ConsoleHandler())
    
    # Log a message
    logger.info("This is an information message.")

Summary
-------

The `loggingpython` package is designed to simplify the integration of logging into Python applications, offering a straightforward and extensible logging system. The package is structured around three main components: the `__init__.py` file, which serves as the entry point and exposes the core logging functionalities; the `handler/` module, which contains various handler classes for different types of logging; and the `error/` module, which includes error classes for exception handling.

The `__init__.py` file is crucial as it imports and exposes the `Logger` class and various handler classes, allowing users to easily access and utilize these components for logging purposes. This includes the ability to create logger instances, add handlers to loggers, and log messages at different levels.

The `handler/` module provides a range of handler classes, such as `FileHandler`, `ConsoleHandler`, `JSONHandler`, `SQLHandler`, `CSVHandler`, and `SysHandler`, each designed to handle log messages in a specific manner, whether by writing them to files, outputting them to the console, or storing them in databases.

The `error/` module contains error classes that represent specific error types, such as `ServerUnreachableError`, `ServerMethodCallError`, `ClientMethodCallError`, `InvalidLogLevelError`, `InvalidHandlerMethodError`, and `HandlerNotFoundError`. These classes are essential for handling exceptions within the logging system, ensuring that errors are caught and managed appropriately.

Through the use of these components, developers can easily integrate a robust logging system into their Python applications, tailoring the logging functionality to meet the specific requirements of their projects. The package's modular design and clear documentation make it a versatile and user-friendly solution for logging needs in Python applications.

Further information
-------------------

For detailed information on the classes and functions of `loggingpython`, please visit the `Documentation <https://github.com/loggingpython-Community/loggingpython/wiki>`_.

License
-------

`loggingpython` is licensed under the `MIT License <https://opensource.org/licenses/MIT>`_.

Further resources
-----------------

- `GitHub Repository <https://github.com/loggingpython-Community/loggingpython>`_
- `Issue Tracker <https://github.com/loggingpython-Community/loggingpython/issues>`_
- `Changelog <https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md>`_
- `PyPi <https://pypi.org/project/loggingpython/>`_

Social media
-------------

- `GitHub <https://github.com/loggingpython-Community>`_