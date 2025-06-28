from collections import UserDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import IndicatorBase

class IndicatorDict(UserDict):
    """
    A dictionary that only accepts IndicatorBase objects as values. The
    keys must be strings, and the values must be instances of 
    IndicatorBase. If a key already exists, it cannot be overridden.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.update(*args, **kwargs)

    def __setitem__(self, key: str, value: IndicatorBase) -> None:
        """
        Takes a key as a string and an indicator value to store in the
        IndicatorDict dictionary.

        Args:
            key (str): The identifier for the Indicator.
            value (IndicatorBase): The indicator being stored.

        Raises:
            TypeError: The key is not a str value.
            TypeError: The value is not a IndicatorBase object.
            KeyError: The key is already taken by another indicator.
        """
        if not isinstance(key, str):
            raise TypeError(f"Expected key type: str | Actual: {type(key)}")
        if not isinstance(value, IndicatorBase):
            raise TypeError(
                f"Expected value type: IndicatorBase | Actual: {type(value)}"
            )
        if key in self.data:
            raise KeyError(
                f"Indicator key {key} already exists and cannot be overridden"
            )
        super().__setitem__(key, value)

    def update(self, *args, **kwargs) -> None:
        """
        Takes dictionary key value pairs and updates this dictionary to
        include them.
        """
        items = dict(*args, **kwargs)
        for key, value in items.items():
            self[key] = value

    def setdefault(self, key, default=None) -> None:
        """
        This method is not allowed for a IndicatorDict object, use
        explicit assignment instead.

        Raises:
            RuntimeError: This method is not allowed.
        """
        raise RuntimeError("Use explicit assignment instead of setdefault()")

    def add(self, key: str, value: IndicatorBase) -> None:
        """
        Takes a single key and value, then adds the pair to the
        IndicatorDict dictionary.

        Args:
            key (str): The identifier for the Indicator.
            value (IndicatorBase): The indicator being stored.
        """
        self[key] = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({dict(self.items())})"