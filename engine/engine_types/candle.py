from datetime import datetime
import pandas as pd
from enum import Enum

class Direction(Enum):
    """
    Enum object that refers to the direction of a `Candle` object.
    """
    EVEN = 0
    DOWN = 1
    UP = 2

class Candle:
    """
    Data type with attributes for OHLCV properties and `datetime`. Also
    derives other properties from OHLCV ie. `movement` and `direction`.

    Attributes:
        datetime (datetime): Datetime object of `Candle`.
        open (float): Starting price.
        high (float): Highest price.
        low (float): Lowest price.
        close (float): Closing price.
        volume (float): Amount of shares traded.
        is_first (bool): Whether or not it is the first `Candle` in the
            dataset.
        is_last (bool): Whether or not it is the last 'Candle' in the
            dataset.
    """

    def __init__(self, candle: pd.Series) -> None:
        """
        Assigns the instance variables to the data in the `candle`
        series data argument passed in.

        Args:
            candle (pandas.Series): Data that contains the OHLCV and
                datetime values for the properties.
        """

        self.datetime: datetime = candle.name

        self.open: float = candle.open

        self.high: float = candle.high

        self.low: float = candle.low

        self.close: float = candle.close

        self.volume: float = candle.volume

        self.is_first: bool = False

        self.is_last: bool = False

    @property
    def movement(self) -> float:
        """
        Refers to the difference between the `close` price and the
        `open` price of the `Candle` object`.

        Returns:
            float: `Candle.close` - `Candle.open`
        """
        return self.close - self.open

    @property
    def direction(self) -> Direction:
        """
        Refers to the direction of `Candle.movement`, can be
        `Direction.UP` `Direction.DOWN` or `Direction.EVEN`.

        Returns:
            Direction: the direction of candle
        """
        if self.movement > 0:

            return Direction.UP

        elif self.movement < 0:

            return Direction.DOWN

        else: # movement is 0

            return Direction.EVEN
        
    def __eq__(self, other):
        """
        Compares two Candle objects for equality based on their
        attributes. This method is used to determine if two Candle
        objects are the same.

        Args:
            other (Candle): the other Candle object to compare with.

        Returns:
            bool: True if the Candle objects are equal, False otherwise.
        """
        if not isinstance(other, Candle):
            return False

        return vars(self) == vars(other)
    

