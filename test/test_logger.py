import unittest
from unittest.mock import MagicMock
from loggingpython.logger import Logger
from loggingpython.log_levels import LogLevel
from loggingpython.handler.consolehandler import ConsoleHandler
from loggingpython.error.invalid_log_level_error import InvalidLogLevelError


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger(name="test_logger")
        self.handler = ConsoleHandler()

    def test_add_handler(self):
        self.logger.addHandler(self.handler)
        self.assertIn(self.handler, self.logger.handlers)

    def test_remove_handler(self):
        self.logger.addHandler(self.handler)
        self.logger.removeHandler(self.handler)
        self.assertNotIn(self.handler, self.logger.handlers)

    def test_log_message(self):
        # Mock the emit method of the handler to check if it's called
        self.handler.emit = MagicMock()
        self.logger.addHandler(self.handler)
        self.logger.info("Test message")
        self.handler.emit.assert_called_once()

    def test_log_levels(self):
        # This is a basic test to ensure that log levels are correctly set
        self.assertEqual(self.logger.min_loglevel, LogLevel.INFO)
        self.assertEqual(self.logger.max_loglevel, LogLevel.CRITICAL)

    def test_invalid_log_level(self):
        # This test ensures that an exception is raised for an invalid log
        # level
        with self.assertRaises(InvalidLogLevelError):
            self.logger._validate_loglevel("INVALID_LEVEL")


if __name__ == '__main__':
    unittest.main()
