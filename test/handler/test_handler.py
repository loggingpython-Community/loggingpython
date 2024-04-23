import unittest

from loggingpython.handler.handler import Handler


class TestHandler(unittest.TestCase):
    def test_emit_not_implemented(self):
        handler = Handler()
        with self.assertRaises(NotImplementedError):
            handler.emit({})


if __name__ == '__main__':
    unittest.main()
