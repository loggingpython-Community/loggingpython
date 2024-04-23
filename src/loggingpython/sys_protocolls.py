from enum import Enum
from socket import SOCK_STREAM, SOCK_DGRAM


class SysProtocolls(Enum):
    TCP = SOCK_STREAM
    UDP = SOCK_DGRAM
