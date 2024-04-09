class ServerUnreachableError(Exception):
    """
    Raised when the client fails to establish a connection to the server.
    This error indicates that the server might be unreachable due to network
    issues, incorrect server address or port, or the server not being active.
    """
    def __init__(self, servername: str, port: int):
        message: str = f"Failed to connect to the server: {servername}:{port}"
        super().__init__(message)
