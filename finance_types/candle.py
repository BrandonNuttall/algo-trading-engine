from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass
from numbers import Number
import pandas as pd
from enum import Enum

class Direction(Enum):
    """
    Enum object that refers to the direction of a `Candle` object.
    """
    EVEN = 0
    DOWN = 1
    UP = 2

@dataclass(frozen=True)
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
        pandas series data argument passed in.

        index: `datetime`
        columns: `open`, `high`, `low`, `close`, `volume`

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
            Direction: The direction of the candle
        """
        if self.movement > 0:
            return Direction.UP

        elif self.movement < 0:
            return Direction.DOWN

        else: # movement is 0
            return Direction.EVEN
        
    @property
    def datetime(self) -> datetime:
        """
        Returns the datetime of the `Candle` object.

        Returns:
            datetime: The datetime of the candle.
        """
        return self._datetime
    
    @datetime.setter
    def datetime(self, datetime: datetime) -> None:
        """
        Sets the datetime of the `Candle` object.

        Args:
            datetime (datetime): The datetime to set for the candle.
        """
        if not isinstance(datetime, datetime):
            raise TypeError(
                f"Expected datetime type: datetime | "
                f"Actual: {type(datetime)}"
            )
        self._datetime = datetime

    @property
    def open(self) -> float:
        """
        Returns the open price of the `Candle` object.

        Returns:
            float: The open price of the candle.
        """
        return self._open
    
    @open.setter
    def open(self, open: float) -> None:
        """
        Sets the open price of the `Candle` object.

        Args:
            open (float): The open price to set for the candle.
        """
        if not isinstance(open, Number):
            raise TypeError(
                f"Expected open type: Number | "
                f"Actual: {type(open)}"
            )
        self._open = open

    @property
    def high(self) -> float:
        """
        Returns the high price of the `Candle` object.

        Returns:
            float: The high price of the candle.
        """
        return self._high  
    
    @high.setter
    def high(self, high: float) -> None:
        """
        Sets the high price of the `Candle` object.

        Args:
            high (float): The high price to set for the candle.
        """
        if not isinstance(high, Number):
            raise TypeError(
                f"Expected high type: Number | "
                f"Actual: {type(high)}"
            )
        self._high = high
    
    @property
    def low(self) -> float:
        """
        Returns the low price of the `Candle` object.

        Returns:
            float: The low price of the candle.
        """
        return self._low
    
    @low.setter
    def low(self, low: float) -> None:
        """
        Sets the low price of the `Candle` object.

        Args:
            low (float): The low price to set for the candle.
        """
        if not isinstance(low, Number):
            raise TypeError(
                f"Expected low type: Number | "
                f"Actual: {type(low)}"
            )
        self._low = low

    @property
    def close(self) -> float:
        """
        Returns the close price of the `Candle` object.

        Returns:
            float: The close price of the candle.
        """
        return self._close
    
    @close.setter
    def close(self, close: float) -> None:
        """
        Sets the close price of the `Candle` object.

        Args:
            close (float): The close price to set for the candle.
        """
        if not isinstance(close, Number):
            raise TypeError(
                f"Expected close type: Number | "
                f"Actual: {type(close)}"
            )
        self._close = close

    @property
    def volume(self) -> float:
        """
        Returns the volume of the `Candle` object.

        Returns:
            float: The volume of the candle.
        """
        return self._volume
    
    @volume.setter
    def volume(self, volume: float) -> None:
        """
        Sets the volume of the `Candle` object.

        Args:
            volume (float): The volume to set for the candle.
        """
        if not isinstance(volume, Number):
            raise TypeError(
                f"Expected volume type: Number | "
                f"Actual: {type(volume)}"
            )
        self._volume = volume
        
    def __eq__(self, other: Candle) -> bool:
        """
        Compares two Candle objects for equality based on their
        attributes.

        Args:
            other (Candle): The other Candle object to compare with.

        Returns:
            bool: True if Candle objects are equal, False otherwise.
        """
        if not isinstance(other, Candle):
            return False

        return vars(self) == vars(other)
    

