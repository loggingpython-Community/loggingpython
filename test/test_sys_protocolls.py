import unittest
from socket import SOCK_STREAM, SOCK_DGRAM

from loggingpython.sys_procolls import SysProtocolls


class TestSysProtocolls(unittest.TestCase):

    def test_log_level_values(self):
        self.assertEqual(SysProtocolls.TCP.value, SOCK_STREAM)
        self.assertEqual(SysProtocolls.UDP.value, SOCK_DGRAM)


if __name__ == '__main__':
    unittest.main()
