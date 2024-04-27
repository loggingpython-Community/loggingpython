SysHandler Documentation
========================

The `SysHandler` class is part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation provides a detailed insight into the functionality and usage of the `SysHandler` class defined in this file.

Overview
--------

The `SysHandler` class is responsible for handling log messages over a network connection. It inherits from the `Handler` class and implements specific methods for sending and receiving log messages over a network connection. It supports both client and server modes, allowing for the establishment of connections, sending log messages, and handling incoming messages. The class provides decorators to ensure that certain methods can only be called by the client or server, enforcing the correct usage of the handler. It also includes error handling for scenarios such as server unreachability and incorrect method calls.

Automatic Documentation
-----------------------

The following sections automatically generate documentation for the `SysHandler` class and its members within the `loggingpython.handler` module.

.. automodule:: loggingpython.handler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: loggingpython.handler.SysHandler
   :members:
   :undoc-members:
   :show-inheritance:

Initialization
--------------

A `SysHandler` object is initialized with several parameters, including the name, whether it's a client or server, the protocol to use (TCP or UDP), the server name, and the port number. The initialization process also sets up the socket and binds it to the specified server address.

.. code-block:: python

    from loggingpython.handler.syshandler import SysHandler
    from loggingpython.sys_protocolls import SysProtocolls
    
    # Create a SysHandler for a TCP client
    client_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)
    
    # Create a SysHandler for a TCP server
    server_handler = SysHandler(name="server", client=False, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)

Variables
---------

- `name`: The name of the handler.
- `client`: Whether the handler is a client.
- `protocoll`: The protocol to use (TCP or UDP).
- `server_name`: The name of the server.
- `port`: The port number.
- `logformat_string`: The format string for the log messages.
- `logger`: A Logger object to log received messages when the SysHandler is in server mode.

Methods
-------

- `emit(self, record: dict) -> None`: Sends a log message to the server.
- `_connect_client(self) -> None`: Establishes a connection to the server as a client.
- `_run_server(self) -> None`: Starts a server that listens for incoming connections.
- `_handle_client_connection(self) -> None`: Handles incoming connections from clients.

Example
-------

Here is a simple example of how to use the `SysHandler` class to send a log message from a client to a server.

.. code-block:: python

    from loggingpython.handler.syshandler import SysHandler
    from loggingpython.sys_protocolls import SysProtocolls
    
    # Create a SysHandler for a TCP client
    client_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)
    
    # Send a log message from the client to the server
    client_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})

Summary
-------

The `SysHandler` class in `syshandler.py` provides a robust and flexible way to handle log messages over a network connection. By supporting both client and server modes, it allows for the establishment of connections, sending log messages, and handling incoming messages, ensuring that network communication is configured appropriately based on the chosen protocol. The inclusion of decorators and error handling ensures that the handler is used correctly and that errors are handled gracefully.

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