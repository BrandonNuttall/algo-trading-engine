from handler_base import DataHandler
import pandas as pd
from exceptions import InvalidDataException
from data_validation import validate_data

class IndicatorBase(DataHandler):

    def __init__(self, data: pd.DataFrame = None) -> None:
        super().__init__()

        if data: self.data = data

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, data: pd.DataFrame) -> None:

        if not validate_data(data):
            raise InvalidDataException("Invalid data format")
        
        self._data = data