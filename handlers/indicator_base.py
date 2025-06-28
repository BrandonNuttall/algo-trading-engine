from typing import TYPE_CHECKING
from data import validate_data
import pandas as pd

if TYPE_CHECKING:
    from handler_base import DataHandler

class IndicatorBase(DataHandler):
    """
    Interface for all user defined Indicators, child of DataHandler,
    only difference being the addition of optional stored data that
    will run before any other handler that uses this indicator.

    Stored data frequency must be divisible by the frequency of the
    handler that uses it.

    Args:
        data (pd.Dataframe, optional): Backdata stored by indicator.
    """
    def __init__(self, data: pd.DataFrame = None) -> None:
        super().__init__()
        self._data: pd.DataFrame = data

    @property
    def data(self) -> pd.DataFrame:
        """
        The backdata stored by the indicator.

        Returns:
            pd.DataFrame: The backdata stored by indicator. 
        """
        return self._data

    @data.setter
    def data(self, data: pd.DataFrame) -> None:
        """
        Ensures data being stored by self.data is a pd.Dataframe obj.

        Args:
            data (pd.DataFrame): The backdata to be stored.

        Raises:
            InvalidDataException: Data argument is not a pd.DataFrame.
        """
        validate_data(data)
        
        self._data = data