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
    def __init__(self, client: bool = True,
                 protocoll: SysProtocolls = SysProtocolls.TCP,
                 server_name: str = "localhost", port: int = 8080) -> None:
        self.client = client
        self.protocoll = protocoll
        self.server_name = server_name
        self.port = port
        self.syssocket = socket.socket(socket.AF_INET,
                                       self.protocoll.value)
        self.server_addr = (self.server_name, self.port)

        if self.protocoll == SysProtocolls.TCP:
            self.connect_client = partial(self.connect_client_tcp)
            self.start_server = partial(self.start_server_tcp)
            self.handle_client_connection = partial(
                self.handle_client_connection_tcp)
            self.emit = partial(self.emit_tcp)
        elif self.protocoll == SysProtocolls.UDP:
            self.connect_client = partial(self.connect_client_tcp)
            self.start_server = partial(self.start_server_udp)
            self.handle_client_connection = partial(
                self.handle_client_connection_udp)
            self.emit = partial(self.emit_udp)

        if self.client:
            self.connect_client()
        else:
            self.start_server()

    @staticmethod
    def client_only(func):
        def wrapper(self, *args, **kwargs):
            if self.client:
                return func(self, *args, **kwargs)
            else:
                raise ClientMethodCallError("This method can only be called \
by the client.")
        return wrapper

    @staticmethod
    def server_only(func):
        def wrapper(self, *args, **kwargs):
            if not self.client:
                return func(self, *args, **kwargs)
            else:
                raise ServerMethodCallError("This method can only be called \
by the server.")
        return wrapper

    @client_only
    def connect_client_tcp(self) -> None:
        try:
            self.syssocket.connect(self.server_addr)
        except ConnectionRefusedError:
            raise ServerUnreachableError(f"Connection to the server \
{self.server_name}:{self.port} could not be established. Please \
check the server address and port.")
        except TimeoutError:
            raise ServerUnreachableError(f"Connection to the server \
{self.server_name}:{self.port} could not be established. Please \
check the server address and port.")

    @client_only
    def connect_client_udp(self) -> None:
        ...

    @server_only
    def start_server_tcp(self) -> None:
        self.syssocket.bind(self.server_addr)
        self.syssocket.listen(1)
        print(f"TCP-Server lauscht auf {self.server_addr}")

    @server_only
    def start_server_udp(self) -> None:
        self.syssocket.bind(self.server_addr)
        print(f"UCP-Server lauscht auf {self.server_addr}")

    @client_only
    def emit_tcp(self, record: dict) -> None:
        formatted_message = self._format_message(record)

        # Serialisieren Sie das Dictionary in einen String
        message_str = json.dumps(formatted_message)

        # Konvertieren Sie den String in Bytes
        message_bytes = message_str.encode('utf-8')

        # Senden Sie die Bytes
        self.syssocket.sendall(message_bytes)

        # Antwort vom Server empfangen
        data = self.syssocket.recv(1024)
        print(f"Empfangene Antwort: {data} vom Server")

    @client_only
    def emit_udp(self, record: dict) -> None:
        formatted_message = self._format_message(record)

        # Serialisieren Sie das Dictionary in einen String
        message_str = json.dumps(formatted_message)

        # Konvertieren Sie den String in Bytes
        message_bytes = message_str.encode('utf-8')
        self.syssocket.sendto(message_bytes, self.server_addr)

    @server_only
    def handle_client_connection_tcp(self) -> None:
        while True:
            # Akzeptieren Sie eine Verbindung von einem Client
            client_socket, addr = self.syssocket.accept()
            print(f"Verbindung von {addr} akzeptiert")

            while True:
                # Daten vom Client empfangen
                data = client_socket.recv(1024)
                if not data:
                    print(f"Verbindung von {addr} wurde geschlossen.")
                    break  # Verbindung wurde geschlossen
                received_str = data.decode('utf-8')
                received_dict = json.loads(received_str)

                print(f"Empfangene Nachricht: '{received_dict}' von {addr}")

                # Antwort an den Client senden
                client_socket.sendall(b"Nachricht empfangen")

            # Schließen Sie die Verbindung
            client_socket.close()

    @server_only
    def handle_client_connection_udp(self) -> None:
        while True:
            data, addr = self.syssocket.recvfrom(1024)
            received_str = data.decode('utf-8')
            received_dict = json.loads(received_str)

            print(f"Empfangene Nachricht: '{received_dict}' von {addr}")

            # Für UDP senden wir die Antwort direkt an die Quelladresse
            self.syssocket.sendto(b"Nachricht empfangen", addr)

    def _format_message(self, record: dict) -> dict:
        """
        Formats a log message based on the provided log data.

        Args:
            record (dict): A dictionary containing the log message details.

        Returns:
            str: The formatted log message.
        """
        values = {
            "loggername": record.get("loggername", ""),
            "iso_8601_time": record.get("iso_8601_time", ""),
            "asctime": record.get("asctime", ""),
            "loglevel": record.get("loglevel", ""),
            "message": record.get("message", ""),
        }

        return values

    def __repr__(self) -> str:
        return f"SysHandler: {self.client}, {self.protocoll}, \
{self.server_name}, {self.port}"

    def __str__(self) -> str:
        return f"SysHandler: {self.client}, {self.protocoll}, \
{self.server_name}, {self.port}"
