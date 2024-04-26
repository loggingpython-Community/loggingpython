# Documentation for `sys_protocolls.py`
## Overview
The `sys_protocolls.py` file is a part of the `loggingpython` package, which provides a simple and extensible way to integrate logging into Python applications. This documentation offers a detailed insight into the functionality and usage of the `SysProtocolls` enum class defined in this file.

## `SysProtocolls` Enum Class
The `SysProtocolls` enum class is responsible for defining the various system protocols that can be used within the logging system. It inherits from Python's built-in `Enum` class, which allows for the creation of enumerations with a set of symbolic names bound to unique, constant values. The `SysProtocolls` enum class defines two protocols, each representing a different type of network communication.

## Enum Values
The `SysProtocolls` enum class includes the following protocols:

 - `TCP`: Represents the Transmission Control Protocol (TCP), a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating via an IP network.
 - `UDP`: Represents the User Datagram Protocol (UDP), a connectionless protocol that allows applications to send messages, or datagrams, to other hosts on an Internet Protocol (IP) network without requiring prior communications to set up special transmission channels or data paths.

## Initialization
The `SysProtocolls` enum class is initialized with the two protocols mentioned above. Each protocol is assigned a value from the `socket` module that corresponds to its type.
```python
from enum import Enum
import socket

class SysProtocolls(Enum):
    TCP = socket.SOCK_STREAM
    UDP = socket.SOCK_DGRAM
```

## Usage
The `SysProtocolls` enum class can be used to specify the protocol for network communication in the logging system. For example, when configuring a `SysHandler`, the protocol can be set to one of the defined protocols to indicate the type of network communication to be used.
```python
from loggingpython.handler.syshandler import SysHandler
from loggingpython.sys_protocolls import SysProtocolls

# Create a SysHandler with TCP protocol
tcp_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)

# Create a SysHandler with UDP protocol
udp_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.UDP, server_name="localhost", port=8080)
```

## Example
Here is a simple example of how to use the `SysProtocolls` enum class to specify the protocol for a network handler.
```python
from loggingpython.handler.syshandler import SysHandler
from loggingpython.sys_protocolls import SysProtocolls

# Create a SysHandler with TCP protocol
tcp_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.TCP, server_name="localhost", port=8080)

# Send a log message using TCP
tcp_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})

# Create a SysHandler with UDP protocol
udp_handler = SysHandler(name="client", client=True, protocoll=SysProtocolls.UDP, server_name="localhost", port=8080)

# Send a log message using UDP
udp_handler.emit({"loggername": "my_logger", "loglevel": "INFO", "message": "This is an information message."})
```
This example demonstrates how the `SysProtocolls` enum class can be used to specify the protocol for network communication, allowing for a clear and consistent configuration of `SysHandler` instances in the logging system.

## Summary
The `SysProtocoll`s enum class in `sys_protocolls.py` provides a standardized way to represent and use system protocols within the `loggingpython` package. By defining a set of predefined protocols, the logging system can be easily adapted to the specific requirements of each application, ensuring that network communication is configured appropriately based on the chosen protocol.

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