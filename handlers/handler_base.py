from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import timedelta
from finance_types import Candle, CandleList, IndicatorDict

if TYPE_CHECKING:
    from indicator_base import IndicatorBase

class DataHandler(ABC):
    """
    The DataHandler abstract class is the parent class for StrategyBase
    and IndicatorBase. It contains the methods for users to implement 
    their own data handlers.
    """
    def __init__(self) -> None:

        self._candles: CandleList = []
        self._indicators: IndicatorDict = {}
        self._frequency: timedelta = None

    @abstractmethod
    def on_candle(self) -> None:
        """
        The default method that is called when a new candle is added to
        the handler.
        """
        pass

    def on_start(self) -> None:
        """
        This is called before the first candle is added to the handler.
        By default, this does nothing.
        """
        pass

    def on_first(self) -> None:
        """
        This is called on the first candle in the data set and then 
        never again. By default, defers to on_candle().
        """
        self.on_candle()

    def on_last(self) -> None:
        """
        This is called on the last candle in the data set and then
        never again. By default, defers to on_candle().
        """
        self.on_candle()

    def on_end(self) -> None:
        """
        This is called after the last candle is added to the handler.
        By default, this does nothing.
        """
        pass

    def update(self, candle: Candle) -> None:
        """
        Updates the data handler with a new candle, adding it to the
        list before updating the stored indicators first, then itself.

        Args:
            candle (Candle): New candle to be added.

        Raises:
            TypeError: The candle argument is not a Candle object.
        """
        if not isinstance(candle, Candle):
            raise TypeError(
                f"Expected argument type: IndicatorBase | "
                f"Actual: {type(indicator)}"
            )

        self.candles.add(candle)
        self._update_indicators()
        self._process_candle()

    def _update_indicators(self) -> None:
        """
        Updates the indicators with current candle after new candles
        are added to the list. If the frequencies are different, it
        will attempt to compress the candles before passing.

        Raises:
            ValueError: The indicator frequency is not compatible.
        """

        for i in self.indicators.values():

            # if indicator has no back data, the frequency is not set
            if not i.frequency:
                i.frequency = self.frequency

            # if indicator has the same frequency as the data, update
            if i.frequency == self.frequency:
                i.update(self.candles.current)

            # if indicator has a different frequency, try to compress
            elif i.frequency % self.frequency == timedelta(0):
                self._attempt_compress(i)

            else: # indicator frequency is not divisible by this freq.
                raise ValueError(
                    f"Indicator frequency, {i.frequency}, must be divisible "
                    f"by it's parent handlers frequency, {self.frequency}."
                )

    def _process_candle(self) -> None:
        """
        Incoming candles are processed differently based on where they
        are in the overall dataset.
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
        Attempts to compress candle data for the indicator by checking
        if there is a enough new data to fulfill the indicators candle.
        
        If there is enough new data, the candles are combined and the
        new candle is passed to indicator, if not, it does nothing.

        Args:
            indicator (IndicatorBase): Indicator to pass the compressed
                the data if fulfilled.

        Raises:
            TypeError: Indicator is not an instance of IndicatorBase
        """
        if not isinstance(indicator, IndicatorBase):
            raise TypeError(
                f"Expected argument type: IndicatorBase | "
                f"Actual: {type(indicator)}"
            )

        # number of candles needed to fulfill the indicator's candle
        n = int(indicator.frequency / self.frequency)

        # grab a slice of n candles from this handler's candles
        nframe = self.candles[0:n]

        # if there are enough candles in the slice
        is_full_frame = len(nframe) == n

        # if the slice's oldest candle is newer than indicators current
        frame_is_new = (
            not indicator.candles or 
            nframe.initial.datetime > indicator.candles.current.datetime
        )

        if is_full_frame and frame_is_new:
            # compress and update the indicator
            candle = nframe.compress()
            indicator.update(candle)

    @property
    def candles(self) -> CandleList:
        """
        This CandleList container of its Candle objects.

        Returns:
            CandleList: The candles contained by handler.
        """
        return self._candles
    
    @property
    def indicators(self) -> IndicatorDict:
        """
        This IndicatorDict container of its Indicator objects.

        Returns:
            IndicatorDict: The indicators that have been stored.
        """
        return self._indicators
    
    @property
    def frequency(self) -> timedelta:
        """
        Frequency of the Candles that have been added to this handler.

        Returns:
            timedelta: The frequency of candles as a timedelta object
        """
        return self._frequency

    @candles.setter
    def candles(self, candles: CandleList) -> None:
        """
        Ensures that the candles argument is a CandleList object.

        Args:
            candles (CandleList): The new CandleList to be stored by
                self.candles.

        Raises:
            TypeError: The candles argument is not the correct type.
        """
        
        if not isinstance(candles, CandleList):
            raise TypeError(
                f"Expected argument type: CandleList | "
                f"Actual: {type(candles)}"
            )
        
        self._candles = candles

    @indicators.setter
    def indicators(self, indicators: IndicatorDict) -> None:
        """
        Ensures the indicators argument is an IndicatorDict object.

        Args:
            indicators (IndicatorDict): The new IndicatorDict to be
                stored by self.indicators.

        Raises:
            TypeError: The indicators argument is not the correct type.
        """
        if not isinstance(indicators, IndicatorDict):
            raise TypeError(
                f"Expected argument type: IndicatorDict | "
                f"Actual: {type(indicators)}"
            )
        
        self._indicators = indicators

    @frequency.setter
    def frequency(self, frequency: timedelta) -> None:
        """
        Ensures the frequency argument is a timedelta object.

        Args:
            frequency (timedelta): The frequency in which candles are
                added to this handler.

        Raises:
            TypeError: The frequency argument is not the correct type.
        """
        if not isinstance(frequency, timedelta):
            raise TypeError(
                f"Expected argument type: timedelta | "
                f"Actual: {type(frequency)}"
            )
        
        self._frequency = frequency

    def __eq__(self, other):

        if not isinstance(other, DataHandler):
            return False

        return vars(self) == vars(other)
