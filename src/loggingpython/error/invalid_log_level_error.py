class InvalidLogLevelErrorr_from_loggingpython(Exception):
    """
    Raised when an invalid log level is specified.
    This error indicates that the provided log level does not match any of the
    supported log levels.
    """
    def __init__(self, log_level: str) -> None:
        message: str = f"Invalid log level specified: {log_level}"
        super().__init__(message)
