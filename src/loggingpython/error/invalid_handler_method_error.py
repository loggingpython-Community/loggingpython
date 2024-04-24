from ..handler.handler import Handler


class InvalidHandlerMethodErrorr(TypeError):
    """
    `loggingpython`
    Raised when a handler does not have the required 'emit' method.
    This error indicates that the handler object passed to the logger does not
    implement the 'emit' method, which is necessary for processing log
    messages.
    """
    def __init__(self, handler: Handler):
        message: str = f"Handler '{handler.__class__.__name__}' must have an \
'emit' method"
        super().__init__(message)
