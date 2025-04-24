from __future__ import annotations
from abc import ABC, abstractmethod
from engine_types import Candle, CandleList, IndicatorDict
from indicator_base import IndicatorBase
from exceptions import InvalidDataException
import pandas as pd


class DataHandler(ABC):
    """
    The DataHandler abstract class is the parent class for both
    StrategyBase and IndicatorBase. It contains the methods for
    end users to implement their own data handlers.
    """

    def __init__(self) -> None:

        self._candles: CandleList = []
        self._indicators: IndicatorDict = {}
        self._frequency: int = None

    @abstractmethod
    def on_candle(self) -> None:
        pass

    def on_start(self) -> None:
        pass

    def on_first(self) -> None:
        self.on_candle()

    def on_last(self) -> None:
        self.on_candle()

    def on_end(self) -> None:
        pass

    def add_indicator(self, key: str, ind: IndicatorBase) -> None:

        if not isinstance(ind, IndicatorBase):
            raise TypeError("indicator must be an instance of IndicatorBase")
    
        self.indicators[key] = ind

    def update(self, candle: Candle) -> None:
        """
        Updates the data handler with a new candle. This method is
        responsible for adding the candle to the list of candles,
        updating the indicators, and processing the candle.

        Args:
            candle (Candle): new candle to be added

        Raises:
            TypeError: if the candle is not a Candle object
        """

        if not isinstance(candle, Candle):
            raise TypeError("candle must be an instance of Candle")

        self._add_candle(candle)
        self._update_indicators()
        self._process_candle()

    def _add_candle(self, candle: Candle, index: int=0) -> None:
        """
        Candle list is an index 0 list, so the current candle is at index 0.
        By default, the candle is added to the front of the list.

        Args:
            candle (Candle): Candle to be added
            index (int, optional): Place in candle list. Defaults to 0.

        Raises:
            TypeError: candle or index is not the correct type
            IndexError: index is out of range
        """

        if not isinstance(candle, Candle):
            raise TypeError("candle must be an instance of Candle")
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index < 0 or index > len(self.candles):
            raise IndexError("index out of range")
        
        self.candles.insert(index, candle)

    def _update_indicators(self) -> None:
        """
        Updates the indicators with the current candle. This method
        is responsible for checking the frequency of the indicators
        data and compressing the data if necessary.

        Raises:
            InvalidDataException: the indicator frequency is not compatible
        """

        for i in self.indicators.values():

            # if indicator had no back data, the frequency is not set
            if not i.frequency:
                i.frequency = self.frequency

            # if the indicator has the same frequency as the data, just update
            if i.frequency == self.frequency:
                i.update(self.candles.current)
            # if the indicator has a different frequency, try to compress
            elif i.frequency % self.frequency == 0:
                self._attempt_compress(i)
            else:
                raise InvalidDataException("Indicator frequency is not " \
                "compatible with data frequency")

    def _process_candle(self) -> None:
        """
        This method is responsible for calling the appropriate handling
        method based on the current candle's position in the full data list.
        """
        if self.candles.current.is_first:
            self.on_start()
            self.on_first()
        elif self.candles.current.is_last:
            self.on_last()
        else: # if its not the first or last
            self.on_candle()
        if self.candles.current.is_last:
            self.on_end

    def _attempt_compress(self, indicator: IndicatorBase):
        """
        Attempts to compress the data for the indicator. This method
        will check if the indicator has enough new data to compress.
        If it does, it will compress the data and update the indicator.
        If it does not, it will do nothing.

        Args:
            indicator (IndicatorBase): indicator to pass the compressed data

        Raises:
            TypeError: the indicator is not an instance of IndicatorBase
        """
        if not isinstance(indicator, IndicatorBase):
            raise TypeError("indicator must be an instance of IndicatorBase")

        n = indicator.frequency / self.frequency
        nframe = self.candles[0:n]

        full_frame = len(nframe) == n
        frame_is_new = (nframe[-1].datetime > 
                        indicator.candles.current.datetime)

        if (full_frame and (not indicator.candles or frame_is_new)):
            candle = self._compress(nframe)
            indicator.update(candle)

    def _compress(self, candles: list[Candle]) -> Candle:
        """
        Compresses a list of candles into a single candle.

        Args:
            candles (list[Candle]): candles to be compressed

        Raises:
            TypeError: candles is not a list of Candle objects

        Returns:
            Candle: compressed candle
        """
        if not all(isinstance(c, Candle) for c in candles):
            raise TypeError("All elements in candles must be " \
            "instances of Candle")

        data = {
            'name': candles[0].datetime,
            'open': candles[-1].open,
            'high': max(c.high for c in candles),
            'low': min(c.low for c in candles),
            'close': candles[0].close,
            'volume': sum(c.volume for c in candles)
        }

        candle = Candle(pd.Series(data))

        if candles[-1].is_first:
            candle.is_first = True
        if candles[0].is_last:
            candle.is_last = True

        return candle

    @property
    def candles(self) -> CandleList:
        return self._candles
    
    @property
    def indicators(self) -> IndicatorDict:
        return self._indicators
    
    @property
    def frequency(self) -> int:
        return self._frequency

    @candles.setter
    def candles(self, candles: CandleList) -> None:

        if not isinstance(candles, CandleList):
            raise TypeError("candles must be an instance of CandleList")
        
        self._candles = candles

    @indicators.setter
    def indicators(self, indicators: IndicatorDict) -> None:
        if not isinstance(indicators, IndicatorDict):
            raise TypeError("indicators must be an instance of IndicatorDict")
        
        self._indicators = indicators

    @frequency.setter
    def frequency(self, freq: int) -> None:

        if not isinstance(freq, int):
            raise TypeError("data_frequency must be an integer")
        
        self._frequency = freq

    def __eq__(self, other):
        if not isinstance(other, DataHandler):
            return False

        return vars(self) == vars(other)
