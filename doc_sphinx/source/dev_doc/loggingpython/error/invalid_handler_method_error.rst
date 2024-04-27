InvalidHandlerMethodError Documentation
=======================================

The `InvalidHandlerMethodError` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `InvalidHandlerMethodError` exception class defined in this file.

Overview
--------

The `InvalidHandlerMethodError` exception class is responsible for indicating when a handler does not have the required 'emit' method. This error is raised to signal that the handler object passed to the logger does not implement the 'emit' method, which is necessary for processing log messages.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `InvalidHandlerMethodError` class and its members within the `loggingpython.error` module.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.error.InvalidHandlerMethodError
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

The `InvalidHandlerMethodError` exception class is initialized with a default message indicating that the handler must have an 'emit' method. However, it can be customized with a specific message when the exception is raised.

.. code-block:: python

    from ..handler.handler import Handler
    
    class InvalidHandlerMethodError(TypeError):
        """
        Raised when a handler does not have the required 'emit' method.
        This error indicates that the handler object passed to the logger does not
        implement the 'emit' method, which is necessary for processing log
        messages.
        """
        def __init__(self, handler: Handler):
            message: str = f"Handler '{handler.__class__.__name__}' must have an 'emit' method"
            super().__init__(message)

Usage
-----

The `InvalidHandlerMethodError` exception class can be used to handle scenarios where a handler that does not implement the required 'emit' method is passed to the logger. This is particularly useful to ensure that all handlers passed to the logger implement the necessary 'emit' method to process log messages correctly.

.. code-block:: python

    from ..handler.handler import Handler
    from .invalid_handler_method_error import InvalidHandlerMethodError
    try:
        # Attempt to pass a handler without an 'emit' method to the logger
        some_handler = Handler() # Assuming this class does not implement 'emit'
        logger.addHandler(some_handler)
    except InvalidHandlerMethodError as e:
        print(f"Error: {e}")

Example
-------

Here is a simple example of how the `InvalidHandlerMethodError` exception class can be used to signal and handle an error when a handler is passed to the logger without the required 'emit' method.

.. code-block:: python

    from ..handler.handler import Handler
    from .invalid_handler_method_error import InvalidHandlerMethodError
    class MyHandler(Handler):
        # This class does not implement 'emit'
        pass
    def add_handler_to_logger(logger, handler):
        if not hasattr(handler, 'emit'):
            raise InvalidHandlerMethodError(handler)
        logger.addHandler(handler)
    try:
        my_handler = MyHandler()
        add_handler_to_logger(logger, my_handler)
    except InvalidHandlerMethodError as e:
        print(f"Error: {e}")

Summary
-------

The `InvalidHandlerMethodError` exception class in `invalid_handler_method_error.py` provides a standardized way to signal and handle errors related to the missing implementation of the 'emit' method in handlers. By throwing this exception, the application can ensure that all handlers passed to the logger implement the necessary 'emit' method to process log messages correctly. This helps to improve the robustness of the application logic and avoid unexpected behavior.

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