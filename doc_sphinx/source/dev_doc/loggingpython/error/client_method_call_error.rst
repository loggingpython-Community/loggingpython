ClientMethodCallError Documentation
===================================

The `ClientMethodCallError` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `ClientMethodCallError` exception class defined in this file.

Overview
--------

The `ClientMethodCallError` exception class is responsible for indicating when a method intended for the client is mistakenly called on the server. This error is raised to signal that a method that should only be executed by the client was incorrectly called by the server, which could lead to incorrect behavior.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   init
   handler_not_found_error
   invalid_handler_method_error
   invalid_log_level_error
   server_method_call_error
   server_unreachable_error

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `ClientMethodCallError` class and its members within the `loggingpython.error` module.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. autoclass:: loggingpython.error.ClientMethodCallError
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Initialization
--------------

The `ClientMethodCallError` exception class is initialized with a default message indicating that the method can only be called by the client. However, it can be customized with a specific message when the exception is raised.

.. code-block:: python

    class ClientMethodCallError(Exception):
        """
        Raised when a method intended for the client is called on the server.
        This error indicates that a method that should only be executed by the
        client was mistakenly called by the server, which could lead to incorrect
        behavior.
        """
        def __init__(self,
                     message="This method can only be called by the client."):
            super().__init__(message)

Example
-------

Here is a simple example of how to use the `ClientMethodCallError` exception class to handle a scenario where a client-only method is mistakenly called on the server.

.. code-block:: python

    def some_client_only_method():
        raise ClientMethodCallError("This method should only be called by the client.")
    
    try:
        # Attempt to call a client-only method on the server
        some_client_only_method()
    except ClientMethodCallError as e:
        print(f"Error: {e}")

Summary
-------

The `ClientMethodCallError` exception class in `client_method_call_error.py` provides a standardized way to indicate and handle errors related to the incorrect calling of client-only methods on the server. By raising this exception, the application can ensure that methods are called in the appropriate context, thereby preventing incorrect behavior and enhancing the robustness of the application's logic.

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