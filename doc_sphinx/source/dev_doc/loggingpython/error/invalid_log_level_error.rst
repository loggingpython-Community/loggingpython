InvalidLogLevelError Documentation
==================================

The `InvalidLogLevelError` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `InvalidLogLevelError` exception class defined in this file.

Overview
--------

The `InvalidLogLevelError` exception class is responsible for indicating when an invalid log level is specified. This error is raised to signal that the log level provided does not match any of the supported log levels.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `InvalidLogLevelError` class and its members within the `loggingpython.error` module.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: loggingpython.error.InvalidLogLevelError
   :members:
   :undoc-members:
   :show-inheritance:

Usage
-----

The `InvalidLogLevelError` exception class can be used to handle scenarios where an invalid log level is specified. This is particularly useful to ensure that only supported log levels are used to ensure consistency and accuracy of log messages.

.. code-block:: python

    try:
        # Attempt to set an invalid log level
        set_log_level("invalid_level")
    except InvalidLogLevelError as e:
        print(f"Error: {e}")

Example
-------

Here is a simple example of how the `InvalidLogLevelError` exception class can be used to signal an error when an invalid log level is specified.

.. code-block:: python

    def set_log_level(level: str):
        if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise InvalidLogLevelError(level)
    try:
        # Attempt to set an invalid log level
        set_log_level("invalid_level")
    except InvalidLogLevelError as e:
        print(f"Error: {e}")

Summary
-------

The `InvalidLogLevelError` exception class in `invalid_log_level_error.py` provides a standardized way to signal and handle errors related to invalid log levels. By raising this exception, the application can ensure that only supported log levels are used, ensuring the consistency and accuracy of log messages.

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