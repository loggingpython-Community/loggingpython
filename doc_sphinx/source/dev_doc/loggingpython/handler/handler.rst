Handler Documentation
=====================

The `Handler` class is a core component of the `loggingpython` package, providing a foundational class for all handlers within the logging system. This documentation offers a detailed explanation of the `Handler` class defined in this file, including its purpose, initialization, variables, and methods.

Overview
--------

The `Handler` class serves as the base class for all handlers in the `loggingpython` package. Handlers are responsible for processing and outputting log messages. This class defines the interface that all handler classes must adhere to, ensuring consistency across different types of handlers.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `Handler` class and its members within the `loggingpython.handler` module.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.handler.Handler
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

The `Handler` class does not require any initialization parameters. It serves as an abstract base class, meaning it cannot be instantiated directly. Instead, it provides a blueprint for other handler classes to inherit from.

Variables
---------

The `Handler` class does not define any instance variables. It is designed to be subclassed, with subclasses implementing their own variables as needed.

Methods
-------

- `emit(self, record: dict) -> None`: This method is intended to be overridden by subclasses to provide specific handling behavior for log messages. The base class raises a `NotImplementedError` to indicate that subclasses must implement this method.

.. code-block:: python

    def emit(self, record: dict) -> None:
        raise NotImplementedError("Subclasses must implement this!")

- `__repr__(self) -> str`: Returns a string representation of the handler object. This method can be overridden by subclasses to provide a more informative representation.

.. code-block:: python

    def __repr__(self) -> str:
        return "Handler()"

- `__str__(self) -> str`: Returns a string representation of the handler object. This method can be overridden by subclasses to provide a more informative representation.

.. code-block:: python

    def __str__(self) -> str:
        return "Handler with: None"

Example
-------

Since the `Handler` class is an abstract base class, it cannot be instantiated directly. Instead, let's consider an example of a subclass that inherits from `Handler`:

.. code-block:: python

    class ConsoleHandler(Handler):
        def emit(self, record: dict) -> None:
            # Implementation for emitting log messages to the console
            pass
    
        def __repr__(self) -> str:
            return "ConsoleHandler()"
    
        def __str__(self) -> str:
            return "ConsoleHandler()"

In this example, `ConsoleHandler` inherits from Handler and provides its own implementation of the `emit` method, along with `__repr__` and `__str__` methods for a custom string representation.

Summary
-------

The `Handler` class in `handler.py` serves as the foundation for all handlers in the `loggingpython` package. By defining a common interface, it ensures that all handlers can be used interchangeably, providing flexibility and consistency in the logging system. Subclasses of `Handler` must implement the `emit` method to provide specific handling behavior for log messages.

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