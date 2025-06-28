from __future__ import annotations
from typing import TYPE_CHECKING
from collections import UserList
from collections.abc import Iterable
from datetime import timedelta
import pandas as pd

if TYPE_CHECKING:
    from candle import Candle

class CandleList(UserList):
    """
    A list that only accepts Candle or other CandleList objects. It
    inherits from UserList to provide a list-like interface while 
    enforcing type constraints.

    A CandleList also ensures that the timeline is maintained for each
    new candle that is added.

    Attributes:
        frequency (timedelta): The frequency of the Candle objects in
            this CandleList.
    """
    def __init__(self, initlist: CandleList=None) -> None:

        super().__init__()
        self.frequency: timedelta = None

        self._validate_candle_list(initlist)

        if initlist is not None:
            self.add(initlist)

    @property
    def data(self):
        raise AttributeError("Direct access to internal data is not allowed.")

    @property
    def current(self) -> Candle:
        """
        Refers to the most recent candle in the list.
        """
        if not self.data:
            raise IndexError("CandleList is empty")
        return self.data[0]
    
    @property
    def initial(self) -> Candle:
        """
        Refers to the oldest candle in the list.
        """
        if not self.data:
            raise IndexError("CandleList is empty")
        return self.data[-1]
    
    def add(self, candle: Candle | CandleList) -> None:
        """
        Adds either a Candle or a CandleList to the front of the list.

        Args:
            candle (Candle | CandleList): Candle or CandleList to be
                added to the list.
        """
        if isinstance(candle, CandleList):
            self.data[:0] = candle
        else:
            self._validate_candle(candle)
            self.insert(0, candle)

    def compress(self) -> Candle:
        """
        Compresses the data stored by the entire list into a single
        candle and returns it.

        Returns:
            Candle: The combined candle data of the list.
        """
        from candle import Candle

        data = {
            'name': self.current.datetime,
            'open': self.initial.open,
            'high': max(c.high for c in self.data),
            'low': min(c.low for c in self.data),
            'close': self.current.close,
            'volume': sum(c.volume for c in self.data)
        }

        candle = Candle(pd.Series(data))

        if self.initial.is_first:
            candle.is_first = True
        if self.current.is_last:
            candle.is_last = True

        return candle

    def append(self, candle: Candle) -> None:
        """
        Adds a Candle object to the end of the list.

        Args:
            candle (Candle): Candle to be added to the last index.
        """
        self._validate_candle(candle)

        if len(self) > 0: 
            self._validate_older(candle, -1)

        super().append(candle)

        self._set_frequency()

    def extend(self, candle_list: CandleList) -> None:
        """
        Adds a CandleList to the end of this candle list.

        Args:
            candle_list (CandleList): Candle list to be put at the end
                of this candle list.

        Raises:
            TypeError: candle_list argument isnt a CandleList.
        """
        self._validate_candle_list(candle_list)

        # If this list only contains 1 item, we need to check
        # against the new lists frequency to ensure consistency.
        if not self.frequency and candle_list.frequency:
            self.frequency = candle_list.frequency
        
        if len(self) > 0:
            self._validate_older(candle_list.current, -1)

        super().extend(candle_list)

        self._set_frequency()

    def insert(self, index: int, candle: Candle) -> None:
        """
        Adds a Candle object to the list at a specified index.

        Args:
            index (int): Index to place the new candle.
            candle (Candle): Candle to be added to the list.
        """
        self._validate_candle(candle)

        if index < 0:
            index += len(self)

        if 0 < index <= len(self):
            self._validate_older(candle, index - 1)

        if 0 <= index < len(self):
            self._validate_newer(candle, index)

        super().insert(index, candle)

        self._set_frequency()

    def pop(self, index: int=-1) -> Candle:
        """
        Remove a Candle object from the front or rear of the list.

        Args:
            index (int, optional): Index to remove. Defaults to -1.

        Raises:
            TypeError: Index is not 0 or last.

        Returns:
            Candle: Candle object being removed.
        """
        if index < 0:
            index += len(self)
        if index != 0 and index != len(self) - 1:
            raise IndexError("Can only remove candles from the front/rear")
        
        self._set_frequency()
        return super().pop(index)
    
    def clear(self) -> None:
        """
        Ensures the frequency goes back to None upon clearing the list.
        """
        self._set_frequency()
        super().clear()

    def remove(self, candle: Candle) -> None:
        """
        Remove the first Candle object matching the candle argument,
        this must be either the first or last candle in the list.

        Args:
            candle (Candle): Candle to be removed.

        Raises:
            TypeError: The first matching Candle is not the first or
                last Candle in the list.
        """
        self._validate_candle(candle)
        index, match = next(
            ((i, c) for i, c in enumerate(self.data) if c == candle),
            (None, None)
        )
        if index != 0 and index != len(self) - 1:
            raise IndexError("Can only remove candles from the front/rear")

        self._set_frequency()
        super().remove(candle)

    def __setitem__(
        self, index: int | slice, item: Candle | CandleList
    ) -> None:
        """
        Ensures the timeline is maintained for modifications using a
        slice or an index (steps are not allowed).
        
        ie. ls[x:y] = ls or ls[x] = y

        Args:
            index (int | slice): Where the new item will be placed
            item (Candle | CandleList): The new item to be placed
        """
        if isinstance(index, slice) and isinstance(item, Iterable):

            self._validate_candle_list(item)

            if index.step is not None:
                raise TypeError("Slicing with a step is not allowed")
            
            # If this list only contains 1 item, we need to check
            # against the new lists frequency to ensure consistency.
            if not self.frequency and item.frequency:
                self.frequency = item.frequency

            # Normalize start & stop ensure within [0, len(self)]
            start, stop, _ = index.indices(len(self))

            if start > 0:
                self._validate_older(item.current, start - 1)

            if start <= stop and stop < len(self):
                self._validate_newer(item.initial, stop)
            elif start > stop and start < len(self):
                self._validate_newer(item.initial, start)
            
            super().__setitem__(index, item)

            self._set_frequency()

        elif isinstance(index, int) and not isinstance(item, Iterable):

            self._validate_candle(item)
            
            # Normalize index to be within [0, len(self)) (if in range)
            if index < 0:
                index += len(self)
            
            if 0 < index < len(self):
                self._validate_older(item, index - 1)

            if 0 < index + 1 < len(self):
                self._validate_newer(item, index + 1)
            
            super().__setitem__(index, item)

            self._set_frequency()
        
        else: super().__setitem__(index, item)

    def __delitem__(self, index: int | slice) -> None:
        """
        Removes the Candle in either the first or last index, or
        removes a slice from the front or rear of the list.

        Args:
            index (int | slice): The index or slice to be removed

        Raises:
            TypeError: Attempted to slice with a step.
            TypeError: Attempted to remove a candle from the middle.
        """
        if isinstance(index, slice):
            if index.step is not None:
                raise TypeError("Slicing with a step is not allowed")
            
            # Normalize start & stop ensure within [0, len(self)]
            start, stop, _ = index.indices(len(self))

            if start != 0 and stop != len(self):
                raise IndexError(
                    "Can only remove candles from the front/rear"
                )
        else:
            # Normalize index
            if index < 0:
                index += len(self)

            if index != 0 and index != len(self) - 1:
                raise IndexError(
                    "Can only remove candles from the front/rear"
                )
        self._set_frequency()
        super().__delitem__(index)

    def __iadd__(self, candle_list: CandleList) -> CandleList:
        """
        Ensures the timeline is maintained for in-place addition via +=

        Args:
            candle_list (CandleList): The new CandleList to be added.

        Raises:
            TypeError: Item being added isnt a CandleList.
            TypeError: CandleList being added has an invalid frequency.

        Returns:
            CandleList: The new CandleList after modification.
        """

        self._validate_candle_list(candle_list)

        # If this list only contains 1 item, we need to check
        # against the new lists frequency to ensure consistency.
        if not self.frequency and candle_list.frequency:
            self.frequency = candle_list.frequency
        
        if len(self) > 0:
            self._validate_older(candle_list.current, -1)
            
        new_list = super().__iadd__(candle_list)

        self._set_frequency()

        return new_list
    
    def __add__(self, candle_list: CandleList) -> CandleList:
        """
        Ensures the timeline is maintained upon addition via +

        Args:
            candle_list (CandleList): The new CandleList to be added.

        Raises:
            TypeError: candle_list argument isnt a CandleList object

        Returns:
            CandleList: The new CandleList after modification.
        """

        self._validate_candle_list(candle_list)
        
        # If this list only contains 1 item, we need to check
        # against the new lists frequency to ensure consistency.
        if not self.frequency and candle_list.frequency:
            self.frequency = candle_list.frequency

        if len(self) > 0:
            self._validate_older(candle_list.current, -1)
            
        new_list = super().__add__(candle_list)

        self._set_frequency()

        return new_list

    def __imul__(self, n: int) -> None:
        """
        In-place multiplication of a CandleList is not allowed.

        Args:
            n (int): Typically the number of copies to be added.

        Raises:
            TypeError: Any attempt to call this method.
        """
        raise TypeError("In-place multiplication is not allowed.")
    
    def __mul__(self, n: int) -> None:
        """
        Multiplication of a CandleList is not allowed.

        Args:
            n (int): Typically the number of copies to be added.

        Raises:
            TypeError: Any attempt to call this method.
        """
        raise TypeError("List multiplication is not allowed.")
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"

    def _validate_candle(self, candle: Candle) -> None:
        """
        Ensures that the candle argument is a properly formatted Candle
        object.

        Args:
            candle (Candle): Candle to be validated.

        Raises:
            TypeError: The candle argument is not a valid Candle object
        """
        if not isinstance(candle, Candle):
            raise TypeError(
                f"Expected argument: Candle | Actual: {type(candle)}"
            )
        
    def _validate_candle_list(self, candle_list: CandleList) -> None:
        """
        Ensures that the candle_list argument is a CandleList object
        and has the same frequency as this CandleList object.
        
        It also ensures the timeline of the candle_list argument.

        Args:
            candle_list (CandleList): CandleList to check frequency.

        Raises:
            TypeError: candle_list argument is not a CandleList object.
            TypeError: candle_list argument has a differing frequency
                as this CandleList object.
        """
        if isinstance(candle_list, CandleList):
            raise TypeError(
                f"Expected argument: CandleList | Actual: {type(candle_list)}"
            )

        if (
            (self.frequency and candle_list.frequency) and 
            (self.frequency != candle_list.frequency)
        ):
            raise ValueError(
                f"Argument has an unequal frequency with this CandleList. "
                f"Expected: {self.frequency} Actual: {candle_list.freq}"
            )
        
        for i in range(len(candle_list) - 1):
            candle_list._validate_newer(candle_list[i], i + 1)
        
    def _validate_older(self, candle: Candle, index: int) -> None:
        """
        Ensures the candle argument is older than the candle at the 
        index by the frequency of the CandleList.

        Args:
            candle (Candle): The candle being added to the list.
            index (int): The index for the candle to be compared to.

        Raises:
            TypeError: The candle argument is not older by frequency.
        """
        previous_dt = (self.data[index].datetime + self.frequency
                       if self.frequency else None)

        if candle.datetime != previous_dt:
            raise ValueError(
                f"Expected datetime before index {index} is {previous_dt}. "
                f"The candle argument is at {candle.datetime}."
            )
        elif ( # If there's no frequency -> self.data has only 1 candle
            not self.frequency and self.data[index].datetime < candle.datetime
        ):
            raise ValueError(
                f"Cannot add a newer datetime to an older index."
            )

    def _validate_newer(self, candle, index) -> None:
        """
        Ensures the candle argument is newer than the candle at the
        index by the frequency of the CandleList.

        Args:
            candle (Candle): The candle being added to the list.
            index (int): The index for the candle to be compared to.

        Raises:
            TypeError: The candle argument is not newer by frequency.
        """
        next_dt = (self.data[index].datetime - self.frequency 
                   if self.frequency else None)

        if candle.datetime != next_dt:
            raise ValueError(
                f"Expected datetime after index {index} is {next_dt}. The "
                f"candle argument is at {candle.datetime}."
            )
        elif ( # If there's no frequency -> self.data has only 1 candle
            not self.frequency and self.data[index].datetime > candle.datetime
        ):
            raise ValueError(
                f"Cannot add an older datetime to a newer index."
            )

    def _set_frequency(self) -> None:
        """
        If the frequency is not set and the length is 2, it can then be
        set. Otherwise, we will set the frequency to none if the length
        is less than 2 and it was previously set.
        """
        if not self.frequency and len(self) > 1:
            self.frequency = self.data[0].datetime - self.data[1].datetime
        elif self.frequency and len(self) < 2:
            self.frequency = None
