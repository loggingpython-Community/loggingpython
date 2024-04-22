class HandlerNotFoundErrorr_from_loggingpython(ValueError):
    """
    Raised when a handler is not found in the logger's handlers.
    This error indicates that the specified handler was not added to the
    logger, and therefore cannot be removed.
    """
    def __init__(self,
                 message="Handler not found in logger's handlers.") -> None:
        super().__init__(message)
