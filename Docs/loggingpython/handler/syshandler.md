# Documentation for `syshandler.py`
## Overview
The `syshandler.py` file is a part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `SysHandler` class defined in this file.

## `SysHandler` Class
The `SysHandler` class is responsible for handling log messages over a network connection. It inherits from the `Handler` class and implements specific methods for sending and receiving log messages over a network connection. It supports both client and server modes, allowing for the establishment of connections, sending log messages, and handling incoming messages. The class provides decorators to ensure that certain methods can only be called by the client or server, enforcing the correct usage of the handler. It also includes error handling for scenarios such as server unreachability and incorrect method calls.

## Initialization
A `SysHandler` object is initialized with several parameters, including the name, whether it's a client or server, the protocol to use (TCP or UDP), the server name, and the port number. The initialization process also sets up the socket and binds it to the specified server address.
```python
from loggingpython.handler.syshandler import SysHandler
from loggingpython.sys_protocolls import SysProtocolls

# Create a SysHandler for a TCP client
client_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)

# Create a SysHandler for a TCP server
server_handler = SysHandler(name="server", client=False, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)
```

## Methods
The `SysHandler` class includes several methods for handling network communication, dynamically set based on the protocol specified during the initialization of the `SysHandler` instance. These methods allow for the establishment of connections, sending log messages, and handling incoming messages.

`_connect_client`
This method is dynamically set to either `_connect_client_tcp` or `_connect_client_udp` based on the protocol specified during the initialization of the `SysHandler` instance. It is responsible for establishing a connection to the server as a client.
 - TCP: The `_connect_client_tcp` method connects the client socket to the server's address and port using TCP. It handles `ConnectionRefusedError` and `TimeoutError` exceptions, raising a `ServerUnreachableError` if the server is unreachable.
 - UDP: The `_connect_client_udp` method connects the client socket to the server's address and port using UDP.

`_start_server`
This method is dynamically set to either `_start_server_tcp` or `_start_server_udp` based on the protocol specified during the initialization of the `SysHandler` instance. It is responsible for starting a server that listens for incoming connections.
 - TCP: The `_start_server_tcp` method binds the server socket to the specified address and port, listens for incoming TCP connections, and accepts them.
 - UDP: The `_start_server_udp` method binds the server socket to the specified address and port, and listens for incoming UDP messages.

`emit`
This method is dynamically set to either `_emit_tcp` or `_emit_udp` based on the protocol specified during the initialization of the SysHandler instance. It is responsible for sending a log message to the server.
 - TCP: The `_emit_tcp` method formats the log message, encodes it into bytes, and sends it to the server using TCP. It also listens for a response from the server.
 - UDP: The `_emit_udp` method formats the log message, encodes it into bytes, and sends it to the server using UDP. It does not listen for a response from the server.

`_handle_client_connection`
This method is dynamically set to either `_handle_client_connection_tcp` or `_handle_client_connection_udp` based on the protocol specified during the initialization of the `SysHandler` instance. It is responsible for handling incoming connections from clients.
 - TCP: The `_handle_client_connection_tcp `method accepts incoming TCP connections, receives log messages, decodes them, and logs the received log messages using `self.logger` if available. It also sends a confirmation message back to the client.
 - UDP: The `_handle_client_connection_udp` method listens for incoming UDP messages, decodes them, and logs the received log messages using `self.logger` if available. It also sends a confirmation message back to the client.
`_format_message(self, record: dict[str]) -> str`

This method formats a log message based on the provided log data. It includes `self.name` in the formatted message, ensuring that the log message is uniquely identifiable by the client's name. The formatted message is returned as a string, ready to be sent over the network.

## Decorators
The class uses decorators to enforce the correct usage of methods based on whether the handler is a client or server:

 - `@_client_only`: Ensures that a method can only be called by a client.
 - `@_server_only`: Ensures that a method can only be called by a server.

## Error Handling
The class includes error handling for scenarios such as server unreachability and incorrect method calls, raising custom exceptions when these errors occur.

## Example
Here is a simple example of how to use the `SysHandler` class to send a log message from a client to a server.
```python
from loggingpython.handler.syshandler import SysHandler
from loggingpython.sys_protocolls import SysProtocolls

# Create a SysHandler for a TCP client
client_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)

# Create a SysHandler for a TCP server
server_handler = SysHandler(name="server", client=False, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)

# Send a log message from the client to the server
client_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})
```
This example demonstrates how the `SysHandler` class can be used to establish a network connection, send a log message, and handle incoming messages, providing a flexible and powerful way to integrate logging into networked applications.

## Summary
The `SysHandler` class in `syshandler.py` provides a robust and flexible way to handle log messages over a network connection. By supporting both client and server modes, it allows for the establishment of connections, sending log messages, and handling incoming messages, ensuring that network communication is configured appropriately based on the chosen protocol. The inclusion of decorators and error handling ensures that the handler is used correctly and that errors are handled gracefully.

---

## License

`loggingpython` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Further resources

- [GitHub Repository](https://github.com/loggingpython-Community/loggingpython)
- [Issue Tracker](https://github.com/loggingpython-Community/loggingpython/issues)
- [Changelog](https://github.com/loggingpython-Community/loggingpython/blob/main/CHANGELOG.md)
- [PyPi](https://pypi.org/project/loggingpython/)

## Social media

- [GitHub](https://github.com/loggingpython-Community)

---