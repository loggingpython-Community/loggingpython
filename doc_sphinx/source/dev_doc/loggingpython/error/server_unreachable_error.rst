ServerUnreachableError Documentation
====================================

The `ServerUnreachableError` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `ServerUnreachableError` exception class defined in this file.

Overview
--------

The `ServerUnreachableError` exception class is designed to indicate when a client fails to establish a connection to the server. This error signifies that the server might be unreachable due to network issues, incorrect server address or port, or the server not being active.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `ServerUnreachableError` class and its members within the `loggingpython.error` module.

.. automodule:: loggingpython.error
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: loggingpython.error.ServerUnreachableError
   :members:
   :undoc-members:
   :show-inheritance:

Initialization
--------------

The `ServerUnreachableError` exception class is initialized with a default message indicating that the connection to the server failed. However, it can be customized with a specific message when the exception is raised.

.. code-block:: python

    class ServerUnreachableError(Exception):
        """ Raised when the client fails to establish a connection to the server. This error indicates that the server might be unreachable due to network issues, incorrect server address or port, or the server not being active. """
        def __init__(self, servername: str, port: int):
            message: str = f"Failed to connect to the server: {servername}:{port}"
            super().__init__(message)

Usage
-----

The `ServerUnreachableError` exception class can be used to handle scenarios where a client fails to connect to a server. This is particularly useful in scenarios where the application logic relies on establishing a connection to a server, and it is crucial to ensure that the connection is successful.

.. code-block:: python

    try: # Attempt to connect to a server
        connect_to_server("example.com", 8080)
    except ServerUnreachableError as e:
        print(f"Error: {e}")

Example
-------

Here's a simple example of how the `ServerUnreachableError` exception class can be used to handle a scenario where a client fails to connect to a server.

.. code-block:: python

    def connect_to_server(servername: str, port: int): # Simulate a failed connection attempt
        raise ServerUnreachableError(servername, port)
    
    try: # Attempt to connect to a server
        connect_to_server("example.com", 8080)
    except ServerUnreachableError as e:
        print(f"Error: {e}")

Summary
-------

The `ServerUnreachableError` exception class in `server_unreachable_error.py` provides a standardized way to indicate and handle errors related to failed server connections. By raising this exception, the application can ensure that connection attempts are successful, thereby preventing incorrect behavior and enhancing the robustness of the application logic.

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