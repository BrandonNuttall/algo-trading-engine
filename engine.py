from finance_types import Candle
import pandas as pd
from handlers import StrategyBase, IndicatorBase, DataHandler, Broker
from data import validate_data, get_frequency

class Engine:
    """
    The Engine class is responsible for running the strategy and 
    handling the data. It manages the data loading, strategy loading,
    and the execution of the strategy on the data as well as the 
    execution of data on indicators.
    """

    def __init__(self) -> None:
        
        self._data: pd.DataFrame = None
        self._strategy: StrategyBase = None
        self._broker: Broker = Broker()
    
    def run(self, handler: DataHandler=None) -> None:
        """
        By default the engine will run the strategy on the data stored
        in the engine. 
        
        If an DataHandler is passed in, it will run the data
        stored by the DataHandler.
        
        Before running the data, it will run any indicators that may be
        stored in the indicator or strategy.

        Args:
            handler (DataHandler, optional): The current handler being
                ran. Defaults to None.

        Raises:
            NullDataException: If the handler has no data to run
            NullStrategyException: If there is no strategy to run
            TypeError: If handler is not a DataHandler object
        """
        if not handler:
            handler = self.strategy
            data = self.data
        elif isinstance(handler, StrategyBase): 
            data = self.data
        elif isinstance(handler, IndicatorBase):
            data = handler.data

        if data is None or data.empty:
            raise ValueError("No data to run")
        if not handler:
            raise ValueError("No handler to run")
        
        if handler.indicators:
            self._run_indicators(handler)

        self._iter_data(data, handler)

    def load_data(self, data: pd.DataFrame) -> None:
        """ 
        Loads the data being passed in for the strategy to be tested on

        Args:
            data (pd.DataFrame): Data to be tested on.
        """
        self.data = data

    def load_strategy(self, strategy: StrategyBase) -> None:
        """
        Loads the strategy to be tested and takes its broker.

        Args:
            strategy (StrategyBase): Strategy to be tested.
        """
        self.strategy = strategy
        strategy.broker = self.broker

    def _run_indicators(self, handler: DataHandler) -> None:
        """
        For each indicator in the handler, it will check if there
        is data stored by the indicator.
        
        If there is, it will call run(indicator) on that indicator. 
        
        If there isnt, it will recursively call run_indicators() on
        that indicator.

        Args:
            handler (DataHandler): The handler which contains the 
                indicators

        Raises:
            TypeError: The handler is not a DataHandler object
        """
    
        for i in handler.indicators:

            if i.data is not None and not i.data.empty:
                self.run(i)
            elif i.indicators:
                self._run_indicators(i)

    def _iter_data(self, data: pd.DataFrame, handler: DataHandler) -> None:
        """
        Assigns the handler the frequency of the data. And identifies
        the first and last candles in the dataset.
        
        It then iterates through the data and creates a candle 
        object for each row in the data, determining if it is the first
        or last candle before passing it to the handler.

        Args:
            data (pd.DataFrame): data to be passed to handler
            handler (DataHandler): handler to be passsed the data

        Raises:
            TypeError: data or handler is not the correct type
            InvalidDataException: data is improperly formatted
        """

        handler.frequency = self.get_frequency(data)

        first_dt = data.iloc[0].name
        last_dt = data.iloc[-1].name

        for dt, row in data.iterrows():
            
            candle = Candle(row)
    
            candle.is_first = dt == first_dt
            candle.is_last = dt == last_dt

            handler.update(candle)
    
    @property
    def data(self) -> pd.DataFrame:
        return self._data
    
    @data.setter
    def data(self, data: pd.DataFrame) -> None:
        """
        Ensures that the data is formatted correctly and is a 
        pandas dataframe.

        Args:
            data (pd.DataFrame): data to be loaded into engine

        Raises:
            TypeError: data is not a pandas dataframe
            InvalidDataException: data is improperly formatted
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas.DataFrame")
        
        if not validate_data(data):
            raise ValueError("Data is improperly formatted")

        self._data = data

    @property
    def strategy(self) -> StrategyBase:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: StrategyBase) -> None:
        """
        Ensures that the strategy is a StrategyBase object.

        Args:
            strategy (StrategyBase): strategy to be loaded into engine

        Raises:
            TypeError: strategy is not a StrategyBase object
        """
        if not isinstance(strategy, StrategyBase):
            raise TypeError("Strategy must be a StrategyBase object")

        self._strategy = strategy

    @property
    def broker(self) -> Broker:
        return self._broker

    @broker.setter
    def broker(self, broker: Broker) -> None:
        """
        Ensures that the broker is a Broker object.

        Args:
            broker (Broker): broker to be loaded into engine

        Raises:
            TypeError: beoker is not a Broker object
        """
        if not isinstance(broker, Broker):
            raise TypeError("Broker must be a Broker object")

        self._broker = broker
        if self.strategy: self.strategy.broker = self.broker
