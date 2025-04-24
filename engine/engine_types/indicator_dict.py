from collections import UserDict
from handlers import IndicatorBase

class IndicatorDict(UserDict):
    """
    A dictionary that only accepts IndicatorBase objects as values. It inherits
    from UserDict to provide a dictionary-like interface while enforcing type
    constraints. The keys must be strings, and the values must be instances of
    IndicatorBase. If a key already exists, it cannot be overwritten.
    """
    def __init__(self):
        super().__init__()

    def __setitem__(self, key: str, value: IndicatorBase) -> None:
        if not isinstance(key, str):
            raise TypeError("Indicator key must be a string")
        if not isinstance(value, IndicatorBase):
            raise TypeError("Indicator value must be an IndicatorBase object")
        if key in self.data:
            raise KeyError("Indicator key already exists and cannot be overwritten")
        super().__setitem__(key, value)

    def update(self, *args, **kwargs) -> None:
        items = dict(*args, **kwargs)
        for key, value in items.items():
            self[key] = value

    def setdefault(self, key, default=None) -> None:
        raise RuntimeError("Use explicit assignment instead of setdefault()")

    def add(self, key: str, value: IndicatorBase) -> None:
        self[key] = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({dict(self.items())})"