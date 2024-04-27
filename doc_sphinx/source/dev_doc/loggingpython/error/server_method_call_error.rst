ServerMethodCallError Documentation
===================================

The `ServerMethodCallError` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `ServerMethodCallError` exception class defined in this file.

Overview
--------

The `ServerMethodCallError` exception class is responsible for indicating when a method intended for the server is mistakenly called on the client. This error is raised to signal that a method that should only be executed by the server was incorrectly called by the client, which could lead to incorrect behavior.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `ServerMethodCallError` class and its members within the `loggingpython.error` module.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.error.ServerMethodCallError
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

The `ServerMethodCallError` exception class is initialized with a default message indicating that the method can only be called by the server. However, it can be customized with a specific message when the exception is raised.

.. code-block:: python

    class ServerMethodCallError(Exception):
        """
        Raised when a method intended for the server is called on the client.
        This error indicates that a method that should only be executed by the
        server was mistakenly called by the client, which could lead to incorrect
        behavior.
        """
        def __init__(self,
                     message="This method can only be called by the server."):
            super().__init__(message)

Usage
-----

The `ServerMethodCallError` exception class can be used to handle scenarios where a method intended for the server is mistakenly called on the client. This is particularly useful in scenarios where the application logic is designed to differentiate between client and server roles, and it is critical to ensure that methods are called in the correct context.

.. code-block:: python

    try:
        # Attempt to call a server-specific method on the client
        some_server_only_method()
    except ServerMethodCallError as e:
        print(f"Error: {e}")

Example
-------

Here is a simple example of how the `ServerMethodCallError` exception class can be used to handle a scenario where a server-only method is mistakenly called on the client.

.. code-block:: python

    def some_server_only_method():
        raise ServerMethodCallError("This method should only be called by the server.")
    
    try:
        # Attempt to call a server-specific method on the client
        some_server_only_method()
    except ServerMethodCallError as e:
        print(f"Error: {e}")

Summary
-------

The `ServerMethodCallError` exception class in `server_method_call_error.py` provides a standardized way to indicate and handle errors related to the incorrect invocation of server-specific methods on the client. By throwing this exception, the application can ensure that methods are called in the correct context, thereby preventing incorrect behavior and enhancing the robustness of the application's logic.

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