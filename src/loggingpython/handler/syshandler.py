from .handler import Handler
from ..sys_procolls import SysProtocolls
import socket


class SysHandler(Handler):
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

        print(self.client, self.protocoll, self.server_name, self.port)
        if client:
            self.connect_client()
        else:
            self.start_server()

    @staticmethod
    def client_only(func):
        def wrapper(self, *args, **kwargs):
            if self.client:
                return func(self, *args, **kwargs)
            else:
                print("Diese Methode kann nur vom Client aufgerufen werden.")
                # Alternativ können Sie hier eine Exception werfen:
                # raise RuntimeError("Diese Methode kann nur vom Client aufgerufen werden.")
        return wrapper

    @staticmethod
    def server_only(func):
        def wrapper(self, *args, **kwargs):
            if not self.client:
                return func(self, *args, **kwargs)
            else:
                print("Diese Methode kann nur vom Server aufgerufen werden.")
                # Alternativ können Sie hier eine Exception werfen:
                # raise RuntimeError("Diese Methode kann nur vom Server aufgerufen werden.")
        return wrapper

    @client_only
    def connect_client(self):
        try:
            self.syssocket.connect(self.server_addr)
        except ConnectionRefusedError:
            # raise ValueError("Server kann nicht ereicht werden")
            ...

    @server_only
    def start_server(self):
        self.syssocket.bind(self.server_addr)
        self.syssocket.listen(1)
        print(f"TCP-Server lauscht auf {self.server_addr}")

    @client_only
    def emit(self, record: dict) -> None:
        """
        Emits a log message.

        This method is intended to be overridden by subclasses to provide
        specific handling behavior for log messages. The base class raises
        a NotImplementedError to indicate that subclasses must implement this
        method.

        Parameters:
        - message (dict): The log message to be processed.

        Raises:
        - NotImplementedError: If the method is not implemented by a subclass.
        """
        # raise NotImplementedError("Subclasses must implement this!")
        ...

    @server_only
    def handle_client_connection(self):
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
                decoded_data = data.decode('utf-8')
                print(f"Empfangene Nachricht: '{decoded_data}' von {addr}")

                # Antwort an den Client senden
                client_socket.sendall(b"Nachricht empfangen")

                # Schließen Sie die Verbindung
                client_socket.close()

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


server = SysHandler(client=False)
handler = SysHandler(client=True)
dictenary = {"Test": "test"}
handler.emit(dictenary)
print(handler)
