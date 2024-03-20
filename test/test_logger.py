from loggingpython.logger import Logger
from loggingpython.filehandler import FileHandler


def test_create_logger():
    logger = Logger("TestLogger")
    assert logger.name == "TestLogger"


def test_add_remove_handler():
    logger = Logger("TestLogger")
    # Hier müssten Sie eine Handler-Instanz erstellen, z.B. FileHandler
    handler = FileHandler(logger.name)
    logger.addHandler(handler)
    assert handler in logger.handlers
    logger.removeHandler(handler)
    assert handler not in logger.handlers


def test_log_levels():
    logger = Logger("TestLogger")
    # Hier müssten Sie eine Handler-Instanz erstellen, z.B. FileHandler
    handler = FileHandler(logger.name)
    logger.addHandler(handler)
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    # Überprüfen Sie, ob die Nachrichten korrekt geloggt wurden.
    # Dies kann komplex sein, da es von der Implementierung des Handlers hängt.
