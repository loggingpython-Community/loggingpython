class ServerMethodCallError(Exception):
    """
    Raised when a method intended for the server is called on the client.
    This error indicates that a method that should only be executed by the
    server was mistakenly called by the client, which could lead to incorrect
    behavior.
    """
    def __init__(self,
                 message="This method can only be called by the server."):
        super().__init__(message)
