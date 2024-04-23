import unittest
import os

from datetime import datetime
from loggingpython.handler.filehandler import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.handler = FileHandler("test_log", "test_logs")

    def tearDown(self):
        if os.path.exists(self.handler.file.name):
            os.remove(self.handler.file.name)

    def test_file_creation(self):
        # Überprüfen Sie, ob die Log-Datei existiert
        self.assertTrue(os.path.exists(self.handler.file.name))

    def test_message_writing(self):
        test_message = {"asctime": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"),
                        "loggername": "test_logger",
                        "loglevel": "INFO",
                        "message": "This is a test message"}
        self.handler.emit(test_message)
        with open(self.handler.file.name, "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 1)
            self.assertIn("This is a test message", lines[0])

    def test_file_closing(self):
        test_message = {"asctime": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"),
                        "loggername": "test_logger",
                        "loglevel": "INFO",
                        "message": "This is a test message"}
        self.handler.emit(test_message)
        # Schließen Sie die Datei explizit
        self.handler._close_file()
        with self.assertRaises(ValueError):
            self.handler.file.write("Another test message\n")


if __name__ == '__main__':
    unittest.main()
