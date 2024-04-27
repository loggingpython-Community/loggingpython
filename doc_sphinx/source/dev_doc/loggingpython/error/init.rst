Error Module Documentation
==========================

The `__init__.py` file within the `loggingpython` package serves as an entry point for the package. It imports and exposes the various error classes available within the `loggingpython` package, providing a convenient way for users to access and utilize these errors for handling exceptions in their applications. This documentation provides a detailed insight into the functionalities and use of the classes and functions defined in this file.

Overview
--------

The `__init__.py` file is a crucial component of the `loggingpython` package, acting as a central hub for importing and exposing the various error classes. This simplifies the process of handling exceptions in applications, allowing developers to easily integrate error handling functionality into their projects.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   client_method_cll_error
   handler_not_found_error
   invalid_handler_method_error
   invalid_log_level_error
   server_method_call_error
   server_unreachable_error

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the error classes and functions defined in the `error` module of the `loggingpython` package.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Imported Modules and Classes
----------------------------

The `__init__.py` file imports and exposes the following error classes:

- `ServerUnreachableError`: Raised when the server is unreachable.
- `ServerMethodCallError`: Raised when there is an error calling a method on the server.
- `ClientMethodCallError`: Raised when there is an error calling a method on the client.
- `InvalidLogLevelError`: Raised when an invalid log level is specified.
- `InvalidHandlerMethodError`: Raised when an invalid handler method is called.
- `HandlerNotFoundError`: Raised when a specified handler is not found.

Functions
---------

The `__init__.py` file does not define any functions. Instead, it focuses on importing and exposing the error classes for use by other parts of the `loggingpython` package or by applications using the package.

Example
-------

To use an error from the `error` module, you first need to import the specific error class you wish to use. Here's an example of how to import and use the `InvalidLogLevelError`:

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

The `__init__.py` file within the `error` folder plays a crucial role in the `loggingpython` package by providing a centralized location for importing and exposing the various error classes. This simplifies the process of handling exceptions in applications, allowing developers to easily integrate error handling functionality into their projects.

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