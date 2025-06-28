import pandas as pd

def prep_data(path: str) -> pd.DataFrame:
    """
    This method uses a csv file `path` to create a `pandas` `dataframe`
    it then converts the datetime `string` column to `datetime` objects
    and sets the `datetime` column to the index of the dataframe.

    Args:
        path (str): The file path to the data being prep. for `Engine`.

    Returns:
        pd.DataFrame: Properly formatted dataframe compatable with the
            `Engine` class.
    """

    data = pd.read_csv(path)
    
    data['datetime'] = pd.to_datetime(data['datetime'])

    data = data.set_index("datetime")

    return data

def validate_data(data: pd.DataFrame) -> bool:
    pass
