from enum import Enum
import socket


class SysProtocolls(Enum):
    TCP = socket.SOCK_STREAM
    UDP = socket.SOCK_DGRAM
