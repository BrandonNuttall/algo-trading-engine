from collections import UserList
from candle import Candle

class CandleList(UserList):
    """
    A list that only accepts Candle objects. It inherits from UserList to
    provide a list-like interface while enforcing type constraints.
    """
    def __init__(self) -> None:
        super().__init__()

    def current(self) -> Candle:
        """
        Returns the current candle in the list.
        """
        if not self.data:
            raise IndexError("CandleList is empty")
        return self.data[0]

    def append(self, item: Candle) -> None:
        self._validate(item)
        super().append(item)

    def extend(self, other: list[Candle]) -> None:
        for item in other:
            self._validate(item)
        super().extend(other)

    def insert(self, index: int, item: Candle) -> None:
        self._validate(item)
        super().insert(index, item)

    def __setitem__(self, index: int, item: Candle) -> None:
        if isinstance(index, slice):
            for x in item: self._validate(x)
        else:
            self._validate(item)
        super().__setitem__(index, item)

    def _validate(self, item: Candle) -> None:
        if not isinstance(item, Candle):
            raise TypeError(f"Must be instance(s) of Candle, got {type(item)}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"