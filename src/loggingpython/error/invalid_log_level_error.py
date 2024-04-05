class InvalidLogLevelError(Exception):
    """
    Raised when an invalid log level is specified.
    This error indicates that the provided log level does not match any of the
    supported log levels.
    """
    def __init__(self,
                 message="Invalid log level specified") -> None:
        super().__init__(message)
