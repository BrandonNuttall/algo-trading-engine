from handler_base import DataHandler
from broker import Broker

class StrategyBase(DataHandler):
    """
    Interface for all user defined Strategies, child of DataHandler,
    only difference being the addition of broker field that handles
    any buying or selling decisions.

    Args:
        broker (Broker): The broker handles everything regarding buying
            and selling.
    """
    def __init__(self) -> None:
        super().__init__()
        self._broker: Broker = None

    def long(self) -> None:
        """
        Responsible for long positions.
        """
        pass

    def short(self) -> None:
        """
        Responsible for short positions.
        """
        pass

    def close(self) -> None:
        """
        Responsible for closing positions.
        """
        pass

    @property
    def broker(self) -> Broker:
        """
        Refers to the broker field stored by strategy.

        Returns:
            Broker: The broker object stored by strategy.
        """
        return self._broker
    
    @broker.setter
    def broker(self, broker: Broker) -> None:
        """
        Ensures that the broker is a Broker object.

        Args:
            broker (Broker): broker to be loaded into engine.

        Raises:
            TypeError: broker is not a Broker object.
        """
        if not isinstance(broker, Broker):
            raise TypeError("Broker must be a Broker object")

        self._broker = broker