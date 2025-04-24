from typing import Type
import pandas as pd

def assert_exc_equality(
    exc: Exception,
    expected_exc: Type[Exception],
    expected_msg: str,
    test_name: str = "",
) -> None:
    """
    Assert that the exception message is as expected.
    
    Args:
        exc (Exception): The exception to check.
        exception (Exception): The expected exception.
        excmessage (str): The expected exception message.
    """
    assert isinstance(exc, expected_exc)
    assert str(exc) == str(expected_msg)

def assert_equality(
    obj1: object,
    obj2: object,
    test_name: str = "",
) -> None:

    if isinstance(obj1, pd.DataFrame):
        assert isinstance(obj2, pd.DataFrame)
        assert obj1.equals(obj2)
    elif isinstance(obj1, list):
        assert isinstance(obj2, list)
        assert len(obj1) == len(obj2)
        for i, (actual, expected) in enumerate(zip(obj1, obj2)):
            assert actual == expected
    else:
        assert obj1 == obj2

def fail(name, expected, actual, i=None):
    pass
