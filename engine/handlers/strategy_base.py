from handler_base import DataHandler

class StrategyBase(DataHandler):

    def __init__(self) -> None:
        super().__init__()
        self._broker = None

    def long(self) -> None:
        pass

    def short(self) -> None:
        pass

    def close(self) -> None:
        pass

    @property
    def broker(self) -> None:
        return self._broker
    
    @broker.setter
    def broker(self, broker: None) -> None:
        """
        Ensures that the broker is a Broker object.

        Args:
            broker (Broker): broker to be loaded into engine

        Raises:
            TypeError: broker is not a Broker object
        """
        if not isinstance(broker, None):
            raise TypeError("Broker must be a Broker object")

        self._broker = broker