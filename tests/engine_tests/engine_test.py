import pytest
import pandas as pd
from unittest.mock import call
from pytest_mock import MockerFixture
from engine import Engine, DataHandler, StrategyBase, Candle
from tests.test_assertions import *
from typing import Type

# TODO: 
# 1. Add support for pytest parameterization
# 2. Add documentation for each test case

@pytest.fixture
def engine() -> Engine:
    """Fixture for the Engine class."""
    return Engine()

@pytest.fixture
def patch_run(mocker):
    return mocker.patch("engine.Engine.run")

@pytest.fixture
def patch_run_indicators(mocker):
    return mocker.patch("engine.Engine._run_indicators")

@pytest.fixture
def patch_iter_data(mocker):
    return mocker.patch("engine.Engine._iter_data")

@pytest.fixture
def patch_handler_update(mocker):
    return mocker.patch("data_handlers.DataHandler.update")

def test_run_success(
    engine: Engine,
    test_name: str,
    data: pd.DataFrame,
    handler: DataHandler,
    patch_run_indicators: MockerFixture,
    patch_iter_data: MockerFixture,
) -> None:
    """
    Testing Engine.run() method for success.

    If the handler has indicators,
        ASSERT that _run_indicators() is called once 
        with the handler.
    If the handler has no indicators,
        ASSERT that _run_indicators() is not called.

    ASSERT that _iter_data() is called once with the 
    data and handler.
    """
    engine.run(data, handler)

    if handler.indicators:
        patch_run_indicators.assert_called_once_with(handler)
    else:
        patch_run_indicators.assert_not_called()
        
    args, _ = patch_iter_data.call_args
    assert_equality(args[0], data, test_name)
    assert_equality(args[1], handler, test_name)

def test_run_failure(
    engine: Engine,
    test_name: str,
    data: pd.DataFrame,
    handler: DataHandler,
    expected_exc: Type[Exception],
    expected_msg: str,
) -> None:
    """
    Testing Engine.run() method for failure.

    ASSERT that the correct exception is raised.
    ASSERT that the exception message is as expected.
    """
    with pytest.raises(expected_exc) as exc:
        engine.run(data, handler)

    assert_exc_equality(
        exc.value, expected_exc, expected_msg, test_name
    )

def test_run_indicators_success(
    engine: Engine,
    test_name: str,
    handler: DataHandler,
    patch_run: MockerFixture,
    patch_run_ind: MockerFixture,
) -> None:
    """
    Testing Engine._run_indicators() method for success.

    for indicators with data,
        ASSERT that run() is called once for 
        each indicator with backdata.
    for indicators without data,
        ASSERT that _run_indicators() is called 
        once for each indicator.
    """
    engine._run_indicators(handler)

    expected_run_calls = [
        call(i) for i in handler.indicators if i.data
    ]
    expected_run_ind_calls = [
        call(i) for i in handler.indicators if not i.data
    ]

    assert_equality(
        patch_run.mock_calls, expected_run_calls, test_name
    )
    assert_equality(
        patch_run_ind.mock_calls, expected_run_ind_calls, test_name
    )

def test_run_indicators_failure(
    engine: Engine,
    test_name: str,
    handler: DataHandler,
    expected_exc: Type[Exception],
    expected_msg: str
) -> None:
    """
    Testing Engine._run_indicators() method 
    for failure.

    ASSERT that the correct exception is raised.
    ASSERT that the exception message is as expected.
    """
    with pytest.raises(expected_exc) as exc:
        engine._run_indicators(handler)

    assert_exc_equality(
        exc.value, expected_exc, expected_msg, test_name
    )

def test_iter_data_success(
    engine: Engine,
    test_name: str,
    data: pd.DataFrame,
    handler: DataHandler,
    expected_candles: list[Candle],
    patch_handler_update: MockerFixture,
) -> None:
    """
    Testing Engine._iter_data() method for success.

    ASSERT that update() is called once with the 
    expected candles.
    """
    engine._iter_data(data, handler)

    expected_calls = [call(c) for c in expected_candles]

    assert_equality(
        patch_handler_update.mock_calls, expected_calls, test_name
    )

def test_iter_data_failure(
    engine: Engine,
    test_name: str,
    data: pd.DataFrame,
    handler: DataHandler,
    expected_exc: Type[Exception],
    expected_msg: str,
) -> None:
    """
    Testing Engine._iter_data() method for failure.

    ASSERT that the method raises an exception.
    ASSERT that the exception message is as expected.
    """
    with pytest.raises(expected_exc) as exc:
        engine._iter_data(data, handler)

    assert_equality(
        exc.value, expected_exc, expected_msg, test_name
    )

def test_load_data_success(
    engine: Engine, 
    test_name: str,
    data: pd.DataFrame
) -> None:
    """
    Testing Engine.load_testdata() method for success.

    ASSERT that the testdata is added to the engine.
    """
    engine.load_data(data)
    assert_equality(engine.data, data, test_name)

def test_load_data_failure(
    engine: Engine,
    test_name: str,
    data: pd.DataFrame,
    expected_exc: Type[Exception],
    expected_msg: str,
) -> None:
    """
    Testing Engine.load_testdata() method for failure.

    ASSERT that the method raises an exception.
    ASSERT that the exception message is as expected.
    """
    with pytest.raises(expected_exc) as exc:
        engine.load_data(data)

    assert_exc_equality(
        exc.value, expected_exc, expected_msg, test_name
    )

def test_load_strategy_success(
    engine: Engine,
    test_name: str,
    strategy: StrategyBase
) -> None:
    """
    Testing Engine.load_strategy() method for success.

    Assert that the broker is set to strategy.broker.
    ASSERT that the strategy is set in the engine.
    """
    engine.load_strategy(strategy)
    assert_equality(engine.broker, strategy.broker, test_name)
    assert_equality(engine.strategy, strategy, test_name)

def test_load_strategy_failure(
    engine: Engine,
    test_name: str,
    strategy: StrategyBase,
    expected_exc: Type[Exception],
    expected_msg: str,
) -> None:
    """
    Testing Engine.load_strategy() method for failure.

    ASSERT that the method raises an exception.
    ASSERT that the exception message is as expected.
    """
    with pytest.raises(expected_exc) as exc:
        engine.load_strategy(strategy)
    
    assert_exc_equality(
        exc.value, expected_exc, expected_msg, test_name
    )
    
