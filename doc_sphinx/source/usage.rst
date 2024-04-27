Usage of `loggingpython`
=======================

This section will guide you on how to use `loggingpython` in your project.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   index
   installation
   contribute
   api_reference
   lib_list
   changelog
   license

Simple Example
--------------

First, import the package and create a logger:

.. code-block:: python

    import loggingpython as lp
    
    # Create a simple logger with a file handler and a console handler
    logger = lp.getBasicLogger()

Adding Handlers
---------------

You can add various handlers to your logger to customize how log messages are handled. Here's how to add a `FileHandler`, `ConsoleHandler`, `JSONHandler`, `SQLHandler`, and `CSVHandler`:

.. code-block:: python

    # Create a logger
    logger = lp.getLogger()
    
    # Add a FileHandler
    filehandler = lp.FileHandler(logger.name)
    logger.addHandler(filehandler)
    
    # Add a ConsoleHandler
    consolehandler = lp.ConsoleHandler()
    logger.addHandler(consolehandler)
    
    # Create a JSONHandler
    jsonhandler = lp.JSONHandler(logger.name)
    logger.addHandler(jsonhandler)
    
    # Create a SQLHandler
    sqlhandler = lp.SQLHandler(logger.name)
    logger.addHandler(sqlhandler)
    
    # Create a CSVHandler
    csvhandler = lp.CSVHandler(logger.name)
    logger.addHandler(csvhandler)
    
    # Create a SysHandler for a TCP client
    sys_handler = SysHandler()
    logger.addHandler(sys_handler)
    
    # Create a SysHandler for a TCP server
    server_handler = SysHandler(client=False)

Logging Messages
----------------

Now you can use the logger to generate different types of log messages:

.. code-block:: python

    # Log messages at different levels
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")
    logger.critical("This is a critical error.")

Handling Exceptions
--------------------

The `loggingpython` package also provides error classes for handling exceptions. Here's an example of how to use the `InvalidLogLevelError`:

.. code-block:: python

    from loggingpython.error.invalid_log_level_error import InvalidLogLevelError
    
    # Example usage
    try:
        # Code that might raise an InvalidLogLevelError
        pass
    except InvalidLogLevelError as e:
        print(f"An error occurred: {e}")

Summary
-------

The `loggingpython` package offers a flexible and extensible logging system for Python applications. By providing a variety of handlers and error classes, it allows developers to easily integrate logging functionality into their projects, tailoring the logging system to meet specific requirements.

Further Examples
----------------

Further examples and instructions for using `loggingpython` can be found in the `API reference <api_reference.md>`_.

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