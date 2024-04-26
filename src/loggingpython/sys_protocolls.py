# MIT License
#
# Copyright (c) 2024 Mr-Major-K
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This module defines the `SysProtocolls` class, an enumeration of the system
protocols used within the `loggingpython` package for network communication.
The `SysProtocolls` class includes two members: TCP and UDP, representing the
Transmission Control Protocol and the User Datagram Protocol, respectively.

TCP is used for connection-oriented services, ensuring reliable, ordered, and
error-checked delivery of a stream of bytes between applications running on
hosts communicating via an IP network. UDP, on the other hand, is used for
connectionless services, allowing for the transmission of datagrams without
establishing a connection.

The `SysProtocolls` class is designed to provide a clear and consistent way to
specify the protocol type for network communication within the application,
ensuring that the correct protocol is used based on the requirements of the
communication task.

Example usage:

    from loggingpython.sys_protocolls import SysProtocolls

    # Specify the protocol for a network operation
    protocol = SysProtocolls.TCP

    # Use the protocol in a network operation
    # (Assuming a function that takes a protocol as an argument)
    perform_network_operation(protocol)

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
The focus here is on defining and using system protocols to ensure clear and
effective network communication practices.
"""

from enum import Enum
from socket import SOCK_STREAM, SOCK_DGRAM


class SysProtocolls(Enum):
    """
    `loggingpython`

    Enum class that represents the TCP and UDP system protocols.

    This class defines two enum members: TCP and UDP, which represent the
    corresponding values from the socket module. TCP stands for Transmission
    Control Protocol and is used for connection-oriented services, while UDP
    stands for User Datagram Protocol and is used for connectionless services.
    """

    TCP = SOCK_STREAM
    UDP = SOCK_DGRAM
