import unittest

from loggingpython.log_levels import LogLevel


class TestLogLevel(unittest.TestCase):

    def test_log_level_values(self):
        self.assertEqual(LogLevel.DEBUG.value, "DEBUG")
        self.assertEqual(LogLevel.INFO.value, "INFO")
        self.assertEqual(LogLevel.WARNING.value, "WARNING")
        self.assertEqual(LogLevel.ERROR.value, "ERROR")
        self.assertEqual(LogLevel.CRITICAL.value, "CRITICAL")


if __name__ == '__main__':
    unittest.main()
