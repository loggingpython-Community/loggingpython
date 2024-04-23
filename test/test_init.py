import unittest

from loggingpython import getLogger, getBasicLogger, get_all_handlers
from loggingpython.logger import Logger
from loggingpython.handler import ConsoleHandler, FileHandler


class TestInit(unittest.TestCase):

    def test_getLogger(self):
        logger = getLogger(name="test_logger")
        self.assertIsInstance(logger, Logger)
        self.assertEqual(logger.name, "test_logger")

    def test_getBasicLogger(self):
        basic_logger = getBasicLogger()

        # Assert that the basic_logger is an instance of Logger
        self.assertIsInstance(basic_logger, Logger)

    def test_get_all_handlers(self):
        handlers = get_all_handlers()
        self.assertIsInstance(handlers, dict)
        self.assertIn('FileHandler', handlers)
        self.assertIn('ConsoleHandler', handlers)
        self.assertIs(handlers['FileHandler'], FileHandler)
        self.assertIs(handlers['ConsoleHandler'], ConsoleHandler)


if __name__ == '__main__':
    unittest.main()
