class ClientMethodCallError(Exception):
    """
    `loggingpython`
    Raised when a method intended for the client is called on the server.
    This error indicates that a method that should only be executed by the
    client was mistakenly called by the server, which could lead to incorrect
    behavior.
    """
    def __init__(self,
                 message="This method can only be called by the client."):
        super().__init__(message)
