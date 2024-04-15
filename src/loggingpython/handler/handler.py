class Handler:
    """
    Base class for all handlers.

    This class defines the interface for all handler classes. Handlers are
    responsible for processing log messages. Subclasses must implement the
    emit method to provide specific handling behavior.
    """

    def emit(self, record: dict) -> None:
        """
        Emits a log message.

        This method is intended to be overridden by subclasses to provide
        specific handling behavior for log messages. The base class raises
        a NotImplementedError to indicate that subclasses must implement this
        method.

        Parameters:
        - message (str): The log message to be processed.

        Raises:
        - NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this!")

    def _format_message(self, record: dict) -> str:
        """
        Formats a log message based on the transferred log data set.

        Args:
            record (dict): A dictionary with the details of the log message.

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
        return "Handler()"

    def __str__(self) -> str:
        return "Handler with: None"
