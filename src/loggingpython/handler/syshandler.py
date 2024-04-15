import socket
import json
from functools import partial

from .handler import Handler
from ..sys_procolls import SysProtocolls
from ..error.server_unreachable_error import ServerUnreachableError
from ..error.server_method_call_error import ServerMethodCallError
from ..error.client_method_call_error import ClientMethodCallError


class SysHandler(Handler):
    """
    A class for handling log messages over a network connection.

    This class inherits from the Handler class and implements specific methods
    for sending and receiving log messages over a network connection. It
    supports both client and server modes, allowing for the establishment of
    connections, sending log messages, and handling incoming messages. The
    class provides decorators to ensure that certain methods can only be
    called by the client or server, enforcing the correct usage of the handler.
    It also includes error handling for scenarios such as server
    unreachability and incorrect method calls.
    """
    def __init__(self,
                 name: str = "client",
                 client: bool = True,
                 protocoll: SysProtocolls = SysProtocolls.TCP,
                 server_name: str = "localhost",
                 port: int = 8080,
                 logformat_string: str = "%(asctime)s: [%(client_name)s] \
[%(client_addr)i] [%(loggername)s] [%(loglevel)s]: %(message)s",
                 logger=None) -> None:
        """
        Initializes a SysHandler instance.

        Args:
            name (str): The name of the handler. Default is "client".
            client (bool): Whether the handler is a client. Default is True.
            protocoll (SysProtocolls): The protocol to use (TCP or UDP).
                Default is TCP.
            server_name (str): The name of the server. Default is "localhost".
            port (int): The port number. Default is 8080.
            logformat_string (str, optional): The format string for the log
                messages from the clients. Defaults to "%(asctime)s:
                    [%(client_name)s] [%(client_addr)i] [%(loggername)s]
                    [%(loglevel)s]: %(message)s".
            logger (Logger): A Logger object to log received messages when the
                SysHandler is in server mode. If not provided, logging will be
                disabled.

        This method sets up the socket, binds it to the specified server
        address, and initializes the handler based on the provided parameters.
        """
        self.name = name
        self.client = client
        self.protocoll = protocoll
        self.server_name = server_name
        self.port = port
        self._syssocket = socket.socket(socket.AF_INET,
                                        self.protocoll.value)
        self.server_addr = (self.server_name, self.port)
        self.logformat_string = logformat_string

        if self.protocoll == SysProtocolls.TCP:
            self._connect_client = partial(self._connect_client_tcp)
            self._run_server = partial(self._run_server_tcp)
            self.handle_client_connection = partial(
                self._handle_client_connection_tcp)
            self.emit = partial(self._emit_tcp)
        elif self.protocoll == SysProtocolls.UDP:
            self._connect_client = partial(self._connect_client_udp)
            self._run_server = partial(self._run_server_udp)
            self.handle_client_connection = partial(
                self._handle_client_connection_udp)
            self.emit = partial(self._emit_udp)

        if self.client:
            self._connect_client()
        else:
            self._logger = logger
            self._run_server()

    @staticmethod
    def _client_only(func):
        """
        Decorator to ensure a method can only be called by a client.

        This decorator checks if the handler is in client mode before allowing
        the method to be called. If the handler is in server mode, it raises a
        ClientMethodCallError.
        """
        def wrapper(self, *args, **kwargs):
            if self.client:
                return func(self, *args, **kwargs)
            else:
                raise ClientMethodCallError()
        return wrapper

    @staticmethod
    def _server_only(func):
        """
        Decorator to ensure a method can only be called by a server.

        This decorator checks if the handler is in server mode before allowing
        the method to be called. If the handler is in client mode, it raises a
        ServerMethodCallError.
        """
        def wrapper(self, *args, **kwargs):
            if not self.client:
                return func(self, *args, **kwargs)
            else:
                raise ServerMethodCallError()
        return wrapper

    @_client_only
    def _connect_client(self) -> None:
        """
        Establishes a connection to the server as a client.

        This method is dynamically set to either `_connect_client_tcp` or
        `_connect_client_udp` based on the protocol specified during the
        initialization of the SysHandler instance.
        """
        ...

    @_client_only
    def _connect_client_tcp(self) -> None:
        """
        Establishes a TCP connection to the server as a client.

        This method connects the client socket to the server's address and port
        using TCP.
        """
        try:
            self._syssocket.connect(self.server_addr)
        except ConnectionRefusedError:
            raise ServerUnreachableError(servername=self.server_name,
                                         port=self.port)
        except TimeoutError:
            raise ServerUnreachableError(servername=self.server_name,
                                         port=self.port)

    @_client_only
    def _connect_client_udp(self) -> None:
        """
        Establishes a UDP connection to the server as a client.

        This method connects the client socket to the server's address and port
        using UDP.
        """
        ...

    @_client_only
    def _run_server(self) -> None:
        """
        Starts a server that listens for incoming connections.

        This method is dynamically set to either `_run_server_tcp` or
        `_run_server_udp` based on the protocol specified during the
        initialization of the SysHandler instance.
        """
        ...

    @_server_only
    def _run_server_tcp(self) -> None:
        """
        Starts a TCP server that listens for incoming connections.

        This method binds the server socket to the specified address and port,
        listens for incoming TCP connections, and accepts them.
        """
        self._logger.info("Server is running")
        self._syssocket.bind(self.server_addr)
        self._syssocket.listen(1)
        print(f"TCP server listens to {self.server_addr}")

    @_server_only
    def _run_server_udp(self) -> None:
        """
        Starts a UDP server that listens for incoming connections.

        This method binds the server socket to the specified address and port,
        and listens for incoming UDP messages.
        """
        self._logger.info("Server is running")
        self._syssocket.bind(self.server_addr)
        print(f"UDP server listens to {self.server_addr}")

    @_client_only
    def emit(self, record: dict[str]) -> None:
        """
        Sends a log message to the server.

        This method is dynamically set to either `_emit_tcp` or `_emit_udp`
        based on the protocol specified during the initialization of the
        SysHandler instance.

        Parameters:
            record (dict): A dictionary containing the log message details.
        """
        ...

    @_client_only
    def _emit_tcp(self, record: dict[str]) -> None:
        """
        Sends a log message to the server over TCP.

        This method formats the log message, encodes it into bytes, and sends
        it to the server using TCP. It also listens for a response from the
        server.

        Args:
            record (dict): A dictionary containing the log message details.
        """
        formatted_message = self._format_message(record)
        formatted_message["client_name"] = self.name

        message_str = json.dumps(formatted_message)

        message_bytes = message_str.encode('utf-8')

        self._syssocket.sendall(message_bytes)

        data = self._syssocket.recv(1024)
        print(f"Received response: {data} from server")

    @_client_only
    def _emit_udp(self, record: dict[str]) -> None:
        """
        Sends a log message to the server over UDP.

        This method formats the log message, encodes it into bytes, and sends
        it to the server using UDP. It also listens for a response from the
        server.

        Args:
            record (dict): A dictionary containing the log message details.
        """
        formatted_message = self._format_message(record)
        formatted_message["client_name"] = self.name

        message_str = json.dumps(formatted_message)

        message_bytes = message_str.encode('utf-8')
        self._syssocket.sendto(message_bytes, self.server_addr)

    @_server_only
    def _handle_client_connection(self) -> None:
        """
        Handles incoming connections from clients.

        This method is dynamically set to either
        `_handle_client_connection_tcp` or `_handle_client_connection_udp`
        based on the protocol specified during the initialization of the
        SysHandler instance.
        """
        ...

    @_server_only
    def _handle_client_connection_tcp(self) -> None:
        """
        Handles incoming TCP connections from clients.

        This method accepts incoming TCP connections, receives log messages,
        decodes them, and logs the received log messages using `self._logger`
        if available. It also sends a confirmation message back to the client.
        """
        while True:
            client_socket, addr = self._syssocket.accept()
            print(f"Connection from {addr} accepted")

            while True:
                data = client_socket.recv(1024)
                if not data:
                    print(f"Connection from {addr} was closed.")
                    break
                received_str = data.decode('utf-8')
                received_dict = json.loads(received_str)

                print(f"Received message: '{received_dict}' from {addr}")
                received_dict["client_addr"] = addr
                logformat_string = self.logformat_string
                log_message = logformat_string % received_dict

                self._logger.info(log_message)

                client_socket.sendall(b"Receive message")

    @_server_only
    def _handle_client_connection_udp(self) -> None:
        """
        Handles incoming UDP connections from clients.

        This method listens for incoming UDP messages, decodes them, and logs
        the received log messages using `self._logger` if available. It also
        sends a confirmation message back to the client.
        """
        while True:
            data, addr = self._syssocket.recvfrom(1024)
            received_str = data.decode('utf-8')
            received_dict = json.loads(received_str)

            print(f"Received message: '{received_dict}' from {addr}")

            received_dict["client_addr"] = addr
            logformat_string = self.logformat_string
            log_message = logformat_string % received_dict

            self._logger.info(log_message)

            self._syssocket.sendto(b"Receive message", addr)

    def __repr__(self) -> str:
        return f"SysHandler({self.client}, {self.protocoll}, \
{self.server_name}, {self.port})"

    def __str__(self) -> str:
        return f"SysHandler with: {self.client}, {self.protocoll}, \
{self.server_name} and {self.port}"
