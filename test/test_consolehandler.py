from loggingpython.consolehandler import ConsoleHandler
from colorama import Fore


def test_emit():
    handler = ConsoleHandler()
    record = {
        "message": "Testnachricht",
        "loglevel": "INFO",
        "asctime": "2023-04-01 12:00:00",
        "iso_8601_time": "2023-04-01T12:00:00",
        "loggername": "testlogger"
    }
    handler.emit(record)
    # Überprüfen, ob die write Methode aufgerufen wurde


def test_format_message():
    handler = ConsoleHandler()
    record = {
        "message": "Testnachricht",
        "loglevel": "INFO",
        "asctime": "2023-04-01 12:00:00",
        "iso_8601_time": "2023-04-01T12:00:00",
        "loggername": "testlogger"
    }
    expected_msg = "2023-04-01 12:00:00: [testlogger]: [INFO]: Testnachricht"
    assert handler._format_message(record) == expected_msg


def test_set_logformat():
    handler = ConsoleHandler()
    new_format = "%(asctime)s - %(loggername)s - %(message)s"
    handler.set_logformat(new_format)
    assert handler.logformat_string == new_format


def test_set_colors_for_levels():
    handler = ConsoleHandler()
    new_colors = {
        "DEBUG": Fore.GREEN,
        "INFO": Fore.BLUE,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA
    }
    handler.set_colors_for_levels(new_colors)
    for level, color in new_colors.items():
        assert handler.color_map[level] == color
