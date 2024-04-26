Handler Module Documentation
============================

The `__init__.py` file within the `handler` folder of the `loggingpython` package serves as an entry point for the handler module. It imports and exposes the various handler classes available within the `loggingpython` package, providing a convenient way for users to access and utilize these handlers for logging purposes. This documentation provides a detailed insight into the functionalities and use of the classes and functions defined in this file.

Overview
--------

The `__init__.py` file is a crucial component of the `loggingpython` package, acting as a central hub for importing and exposing the various handler classes. This simplifies the process of using different handlers for logging in applications, allowing developers to easily integrate logging functionality into their projects.

Automatic Documentation
-------------------------

The following sections automatically generate documentation for the error classes and functions defined in the `handler` module of the `loggingpython` package.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:

Imported Modules and Classes
-------------------------------

The `__init__.py` file imports and exposes the following handler classes:

- `Handler`: The base class for all handlers in the `loggingpython` package.
- `FileHandler`: Handles log messages by writing them to files.
- `ConsoleHandler`: Handles log messages by outputting them to the console.
- `JSONHandler`: Handles log messages by formatting them in JSON and writing them to files.
- `SQLHandler`: Handles log messages by storing them in a SQL database.
- `CSVHandler`: Handles log messages by formatting them in CSV and writing them to files.
- `SysHandler`: Handles log messages by sending them to the system's logging facility.

Functions
---------

The `__init__.py` file does not define any functions. Instead, it focuses on importing and exposing the handler classes for use by other parts of the `loggingpython` package or by applications using the package.

Example
-------

To use a handler from the `handler` module, you first need to import the specific handler class you wish to use. Here's an example of how to import and use the `ConsoleHandler`:

.. code-block:: python

    from loggingpython.handler.consolehandler import ConsoleHandler
    
    # Create a ConsoleHandler instance
    console_handler = ConsoleHandler()
    
    # Use the handler as needed

Summary
-------

The `__init__.py` file within the `handler` folder plays a crucial role in the `loggingpython` package by providing a centralized location for importing and exposing the various handler classes. This simplifies the process of using different handlers for logging in applications, allowing developers to easily integrate logging functionality into their projects.

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