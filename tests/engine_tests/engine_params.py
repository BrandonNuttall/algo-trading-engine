from .engine_builds import data_handlers, data, strategies

# TODO:
# 1. Add tests for the test engine for failure cases

valid_run_params = [
    (
        ("Test Run w/ valid_data1: " + handler_name, data_name, data, handler)
        for handler_name, handler in data_handlers.items()
    ) for data_name, data in data.items()
]

valid_run_indicators_params = [
    (
        ("Test Run Indicators: " + name, handler)
        for name, handler in data_handlers.items()
    )
]

valid_iterdata_params = [
    (
        ("Test iter_data w/ valid_data1: " + handler_name, data_name, data, handler)
        for handler_name, handler in data_handlers.items()
    ) for data_name, data in data.items()
]

valid_load_data_params = [
    (
        ("Test load_data: " + name, data)
        for name, data in data.items()
    )
]

valid_load_strategy_params = [
    (
        ("Test load_strategy: " + name, strategy)
        for name, strategy in strategies.items()
    )
]

