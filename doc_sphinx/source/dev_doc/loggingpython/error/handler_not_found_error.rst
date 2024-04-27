HandlerNotFoundError Documentation
==================================

The `HandlerNotFoundError` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `HandlerNotFoundError` exception class defined in this file.

Overview
--------

The `HandlerNotFoundError` exception class is responsible for indicating when a handler is not found in the logger's handlers. This error is raised to signal that the specified handler was not added to the logger, and therefore cannot be removed or manipulated further.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   init
   client_method_call_error
   invalid_handler_method_error
   invalid_log_level_error
   server_method_call_error
   server_unreachable_error

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `HandlerNotFoundError` class and its members within the `loggingpython.error` module.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.error.HandlerNotFoundError
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

The `HandlerNotFoundError` exception class is initialized with a default message indicating that the handler was not found in the logger's handlers. However, it can be customized with a specific message when the exception is raised.

.. code-block:: python

    class HandlerNotFoundError(ValueError):
        """
        Raised when a handler is not found in the logger's handlers.
        This error indicates that the specified handler was not added to the
        logger, and therefore cannot be removed.
        """
        def __init__(self,
                     message="Handler not found in logger's handlers.") -> None:
            super().__init__(message)

Usage
-----

The `HandlerNotFoundError` exception class can be used to handle scenarios where an attempt is made to remove or manipulate a handler that does not exist in the logger's handlers. This is particularly useful in scenarios where the application logic involves dynamic addition and removal of handlers, and it's crucial to ensure that handlers are correctly managed.

.. code-block:: python

    try:
        # Attempt to remove a handler that does not exist
        logger.removeHandler(non_existent_handler)
    except HandlerNotFoundError as e:
        print(f"Error: {e}")

Example
-------

Here is a simple example of how to use the `HandlerNotFoundError` exception class to handle a scenario where an attempt is made to remove a handler that does not exist in the logger's handlers.

.. code-block:: python

    from loggingpython.error.handler_not_found_error import HandlerNotFoundError
    
    def remove_handler(logger, handler):
        try:
            logger.removeHandler(handler)
        except HandlerNotFoundError as e:
            print(f"Error: {e}")
    
    # Example usage
    try:
        remove_handler(logger, non_existent_handler)
    except HandlerNotFoundError as e:
        print(f"Error: {e}")

Summary
-------

The `HandlerNotFoundError` exception class in `handler_not_found_error.py` provides a standardized way to indicate and handle errors related to the incorrect management of handlers in the logging system. By raising this exception, the application can ensure that handlers are correctly added, removed, and manipulated, thereby preventing incorrect behavior and enhancing the robustness of the application's logging functionality.

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