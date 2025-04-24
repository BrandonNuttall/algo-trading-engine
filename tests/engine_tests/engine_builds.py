import pandas as pd
from engine import StrategyBase, IndicatorBase

valid_data_three_candles = pd.DataFrame({
    'name': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'open': [100, 105, 110],
    'high': [110, 115, 120],
    'low': [90, 95, 100],
    'close': [105, 110, 115],
    'volume': [1000, 1500, 1300]
})

valid_data_two_candles = pd.DataFrame({
    'name': pd.to_datetime(['2022-12-29', '2022-12-30']),
    'open': [95, 97],
    'high': [100, 102],
    'low': [90, 92],
    'close': [98, 100],
    'volume': [800, 850]
})

valid_data_one_candle = pd.DataFrame({
    'name': pd.to_datetime(['2022-12-29']),
    'open': [95],
    'high': [100],
    'low': [90],
    'close': [98],
    'volume': [800]
})

# ------------------------
#    Indicator Builders
# ------------------------

# ---------------------------
#    Non-nested Indicators
# ---------------------------

def ind_w_data_not_nested():
    return IndicatorBase(data=valid_data_three_candles)

def ind_no_data_not_nested():
    return IndicatorBase()

# ------------------------------
#    Indicators w/ One Nested
# ------------------------------

def ind_w_data_one_nested_with_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    return indicator

def ind_w_data_one_nested_no_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_no_data_not_nested())
    return indicator

def ind_no_data_one_nested_with_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    return indicator

def ind_no_data_one_nested_no_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_no_data_not_nested())
    return indicator

# ------------------------------
#    Indicators w/ Two Nested
# ------------------------------

def ind_w_data_two_nested_with_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_w_data_not_nested())
    return indicator

def ind_w_data_two_nested_no_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_no_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    return indicator

def ind_w_data_two_nested_one_with_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    return indicator

def ind_no_data_two_nested_with_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_w_data_not_nested())
    return indicator

def ind_no_data_two_nested_no_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_no_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    return indicator

def ind_no_data_two_nested_one_with_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    return indicator

# --------------------------------
#    Indicators w/ Three Nested
# --------------------------------

def ind_w_data_three_nested_with_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_w_data_not_nested())
    indicator.add_indicator("ind3", ind_w_data_not_nested())
    return indicator

def ind_w_data_three_nested_no_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_no_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    indicator.add_indicator("ind3", ind_no_data_not_nested())
    return indicator

def ind_w_data_three_nested_one_with_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    indicator.add_indicator("ind3", ind_no_data_not_nested())
    return indicator

def ind_w_data_three_nested_two_with_data():
    indicator = IndicatorBase(data=valid_data_three_candles)
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_w_data_not_nested())
    indicator.add_indicator("ind3", ind_no_data_not_nested())
    return indicator

def ind_no_data_three_nested_with_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_w_data_not_nested())
    indicator.add_indicator("ind3", ind_w_data_not_nested())
    return indicator

def ind_no_data_three_nested_no_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_no_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    indicator.add_indicator("ind3", ind_no_data_not_nested())
    return indicator

def ind_no_data_three_nested_one_with_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_no_data_not_nested())
    indicator.add_indicator("ind3", ind_no_data_not_nested())
    return indicator

def ind_no_data_three_nested_two_with_data():
    indicator = IndicatorBase()
    indicator.add_indicator("ind1", ind_w_data_not_nested())
    indicator.add_indicator("ind2", ind_w_data_not_nested())
    indicator.add_indicator("ind3", ind_no_data_not_nested())
    return indicator

# -----------------------
#    Strategy Builders
# -----------------------

# -------------------------------
#    Strategy w/ no indicators
# -------------------------------

def strat_no_ind():
    strategy = StrategyBase()
    return strategy

# ---------------------------------
#    Strategies w/ one indicator
# ---------------------------------

# --- Non-Nested ---
def strat_one_ind_no_data_not_nested():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    return strategy

def strat_one_ind_w_data_not_nested():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    return strategy

# --- One-Nested ---
def strat_one_ind_w_data_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    return strategy

def strat_one_ind_w_data_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    return strategy

def strat_one_ind_no_data_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    return strategy

def strat_one_ind_no_data_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    return strategy

# --- Two-Nested ---
def strat_one_ind_w_data_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    return strategy

def strat_one_ind_w_data_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_no_data())
    return strategy

def strat_one_ind_w_data_two_nested_one_with_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_one_ind_no_data_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_with_data())
    return strategy

def strat_one_ind_no_data_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_no_data())
    return strategy

def strat_one_ind_no_data_two_nested_one_with_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_one_with_data())
    return strategy

# --- Three-Nested ---
def strat_one_ind_w_data_three_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_three_nested_with_data())
    return strategy

def strat_one_ind_w_data_three_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_three_nested_no_data())
    return strategy

def strat_one_ind_w_data_three_nested_one_with_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_three_nested_one_with_data())
    return strategy

def strat_one_ind_w_data_three_nested_two_with_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_three_nested_two_with_data())
    return strategy

def strat_one_ind_no_data_three_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_three_nested_with_data())
    return strategy

def strat_one_ind_no_data_three_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_three_nested_no_data())
    return strategy

def strat_one_ind_no_data_three_nested_one_with_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_three_nested_one_with_data())
    return strategy

def strat_one_ind_no_data_three_nested_two_with_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_three_nested_two_with_data())
    return strategy

# ----------------------------------
#    Strategies w/ Two Indicators
# ----------------------------------

# --- Both Non-Nested ---
def strat_two_inds_w_data_non_nested():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_not_nested())
    return strategy

def strat_two_inds_no_data_non_nested():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_not_nested())
    return strategy

def strat_two_inds_one_w_data_non_nested():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_not_nested())
    return strategy

# --- One One-Nested ---
def strat_two_inds_w_data_one_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_one_nested_with_data())
    return strategy
  
def strat_two_inds_w_data_one_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_one_nested_no_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_one_nested_with_data())
    return strategy
  
def strat_two_inds_no_data_one_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_one_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_one_nested_with_data())
    return strategy
  
def strat_two_inds_one_w_data_one_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_one_nested_no_data())
    return strategy

# --- Both One-Nested ---
def strat_two_inds_w_data_both_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_one_nested_with_data())
    return strategy
  
def strat_two_inds_w_data_both_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_one_nested_no_data())
    return strategy

def strat_two_inds_no_data_both_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_with_data())
    return strategy
  
def strat_two_inds_no_data_both_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_both_one_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_with_data())
    return strategy
  
def strat_two_inds_one_w_data_both_one_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_no_data())
    return strategy
  
def strat_two_inds_w_data_both_one_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_with_data())
    return strategy

def strat_two_inds_no_data_both_one_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_both_one_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_one_nested_no_data())
    return strategy

# --- Both Two-Nested - Both Identical Nested Indicators ---
def strat_two_inds_w_data_both_two_nested_both_both_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_both_two_nested_one_both_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_one_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_both_two_nested_both_both_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_both_two_nested_both_both_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_both_two_nested_one_both_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_one_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_both_two_nested_both_both_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_both_two_nested_both_both_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_both_two_nested_one_both_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_one_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_both_two_nested_both_both_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

# --- Both Two-Nested - Both Differing Nested Indicators ---
def strat_two_inds_w_data_both_two_nested_both_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_both_two_nested_one_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_one_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_both_two_nested_both_one_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_both_two_nested_both_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_both_two_nested_one_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_one_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_both_two_nested_both_one_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_both_two_nested_both_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_both_two_nested_one_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_one_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_both_two_nested_both_one_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_two_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

# --- One Non-Nested, One Two-Nested ---
def strat_two_inds_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_not_nested())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_not_nested())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

# --- Two Inds w/ Data, One One-Nested w/ Data, One Two-Nested --
def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

# --- Two Inds w/ Data, One One-Nested no Data, One Two-Nested --
def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_w_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

# --- Two Inds no Data, One One-Nested w/ Data, One Two-Nested --
def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

# --- Two Inds no Data, One One-Nested no Data, One Two-Nested --
def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_no_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_no_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_w_data_two_nested_no_data())
    return strategy
  
# --- Two Inds One w/ Data, One One-Nested w/ Data, One Two-Nested --
def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_w_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_with_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

# --- Two Inds One w/ Data, One One-Nested no Data, One Two-Nested --
def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_one_w_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_one_with_data())
    return strategy

def strat_two_inds_one_w_data_one_one_nested_no_data_one_two_nested_no_data():
    strategy = StrategyBase()
    strategy.add_indicator("ind1", ind_w_data_one_nested_no_data())
    strategy.add_indicator("ind2", ind_no_data_two_nested_no_data())
    return strategy

data_handlers = [
    (
        "ind_w_data_not_nested",
        ind_w_data_not_nested()
    ),
    (
        "ind_no_data_not_nested",
        ind_no_data_not_nested()
    ),
    (
        "ind_w_data_one_nested_with_data",
        ind_w_data_one_nested_with_data()
    ),
    (
        "ind_w_data_one_nested_no_data",
        ind_w_data_one_nested_no_data()
    ),
    (
        "ind_no_data_one_nested_with_data",
        ind_no_data_one_nested_with_data()
    ),
    (
        "ind_no_data_one_nested_no_data",
        ind_no_data_one_nested_no_data()
    ),
    (
        "ind_w_data_two_nested_with_data",
        ind_w_data_two_nested_with_data()
    ),
    (
        "ind_w_data_two_nested_no_data",
        ind_w_data_two_nested_no_data()
    ),
    (
        "ind_w_data_two_nested_one_with_data",
        ind_w_data_two_nested_one_with_data()
    ),
    (
        "ind_no_data_two_nested_with_data",
        ind_no_data_two_nested_with_data()
    ),
    (
        "ind_no_data_two_nested_no_data",
        ind_no_data_two_nested_no_data()
    ),
    (
        "ind_no_data_two_nested_one_with_data",
        ind_no_data_two_nested_one_with_data()
    ),
    (
        "ind_w_data_three_nested_with_data",
        ind_w_data_three_nested_with_data()
    ),
    (
        "ind_w_data_three_nested_no_data",
        ind_w_data_three_nested_no_data()
    ),
    (
        "ind_w_data_three_nested_one_with_data",
        ind_w_data_three_nested_one_with_data()
    ),
    (
        "ind_w_data_three_nested_two_with_data",
        ind_w_data_three_nested_two_with_data()
    ),
    (
        "ind_no_data_three_nested_with_data",
        ind_no_data_three_nested_with_data()
    ),
    (
        "ind_no_data_three_nested_no_data",
        ind_no_data_three_nested_no_data()
    ),
    (
        "ind_no_data_three_nested_one_with_data",
        ind_no_data_three_nested_one_with_data()
    ),
    (
        "ind_no_data_three_nested_two_with_data",
        ind_no_data_three_nested_two_with_data()
    ),
    (
        "strat_no_ind",
        strat_no_ind()
    ),
    (
        "strat_one_ind_no_data_not_nested",
        strat_one_ind_no_data_not_nested()
    ),
    (
        "strat_one_ind_w_data_not_nested",
        strat_one_ind_w_data_not_nested()
    ),
    (
        "strat_one_ind_w_data_one_nested_w_data",
        strat_one_ind_w_data_one_nested_w_data()
    ),
    (
        "strat_one_ind_w_data_one_nested_no_data",
        strat_one_ind_w_data_one_nested_no_data()
    ),
    (
        "strat_one_ind_no_data_one_nested_w_data",
        strat_one_ind_no_data_one_nested_w_data()
    ),
    (
        "strat_one_ind_no_data_one_nested_no_data",
        strat_one_ind_no_data_one_nested_no_data()
    ),
    (
        "strat_one_ind_w_data_two_nested_w_data",
        strat_one_ind_w_data_two_nested_w_data()
    ),
    (
        "strat_one_ind_w_data_two_nested_no_data",
        strat_one_ind_w_data_two_nested_no_data()
    ),
    (
        "strat_one_ind_w_data_two_nested_one_with_data",
        strat_one_ind_w_data_two_nested_one_with_data()
    ),
    (
        "strat_one_ind_no_data_two_nested_w_data",
        strat_one_ind_no_data_two_nested_w_data()
    ),
    (
        "strat_one_ind_no_data_two_nested_no_data",
        strat_one_ind_no_data_two_nested_no_data()
    ),
    (
        "strat_one_ind_no_data_two_nested_one_with_data",
        strat_one_ind_no_data_two_nested_one_with_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_w_data",
        strat_one_ind_w_data_three_nested_w_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_no_data",
        strat_one_ind_w_data_three_nested_no_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_one_with_data",
        strat_one_ind_w_data_three_nested_one_with_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_two_with_data",
        strat_one_ind_w_data_three_nested_two_with_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_w_data",
        strat_one_ind_no_data_three_nested_w_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_no_data",
        strat_one_ind_no_data_three_nested_no_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_one_with_data",
        strat_one_ind_no_data_three_nested_one_with_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_two_with_data",
        strat_one_ind_no_data_three_nested_two_with_data()
    ),
    (
        "strat_two_inds_w_data_non_nested",
        strat_two_inds_w_data_non_nested()
    ),
    (
        "strat_two_inds_no_data_non_nested",
        strat_two_inds_no_data_non_nested()
    ),
    (
        "strat_two_inds_one_w_data_non_nested",
        strat_two_inds_one_w_data_non_nested()
    ),
    (
        "strat_two_inds_w_data_one_one_nested_w_data",
        strat_two_inds_w_data_one_one_nested_w_data()
    ),
    (
        "strat_two_inds_w_data_one_one_nested_no_data",
        strat_two_inds_w_data_one_one_nested_no_data()
    ),
    (
        "strat_two_inds_no_data_one_one_nested_w_data",
        strat_two_inds_no_data_one_one_nested_w_data()
    ),
    (
        "strat_two_inds_no_data_one_one_nested_no_data",
        strat_two_inds_no_data_one_one_nested_no_data()
    ),
    (
        "strat_two_inds_one_w_data_one_one_nested_w_data",
        strat_two_inds_one_w_data_one_one_nested_w_data()
    ),
    (
        "strat_two_inds_one_w_data_one_one_nested_no_data",
        strat_two_inds_one_w_data_one_one_nested_no_data()
    ),
    (
        "strat_two_inds_w_data_both_one_nested_w_data",
        strat_two_inds_w_data_both_one_nested_w_data()
    ),
    (
        "strat_two_inds_w_data_both_one_nested_no_data",
        strat_two_inds_w_data_both_one_nested_no_data()
    ),
    (
        "strat_two_inds_no_data_both_one_nested_w_data",
        strat_two_inds_no_data_both_one_nested_w_data()
    ),
    (
        "strat_two_inds_no_data_both_one_nested_no_data",
        strat_two_inds_no_data_both_one_nested_no_data()
    ),
    (
        "strat_two_inds_one_w_data_both_one_nested_w_data",
        strat_two_inds_one_w_data_both_one_nested_w_data()
    ),
    (
        "strat_two_inds_one_w_data_both_one_nested_no_data",
        strat_two_inds_one_w_data_both_one_nested_no_data()
    ),
    (
        "strat_two_inds_w_data_both_two_nested_both_both_w_data",
        strat_two_inds_w_data_both_two_nested_both_both_w_data()
    ),
    (
        "strat_two_inds_w_data_both_two_nested_one_both_w_data",
        strat_two_inds_w_data_both_two_nested_one_both_w_data()
    ),
    (
        "strat_two_inds_w_data_both_two_nested_both_both_no_data",
        strat_two_inds_w_data_both_two_nested_both_both_no_data()
    ),
    (
        "strat_two_inds_no_data_both_two_nested_both_both_w_data",
        strat_two_inds_no_data_both_two_nested_both_both_w_data()
    ),
    (
        "strat_two_inds_no_data_both_two_nested_one_both_w_data",
        strat_two_inds_no_data_both_two_nested_one_both_w_data()
    ),
    (
        "strat_two_inds_no_data_both_two_nested_both_both_no_data",
        strat_two_inds_no_data_both_two_nested_both_both_no_data()
    ),
    (
        "strat_two_inds_one_w_data_both_two_nested_both_both_w_data",
        strat_two_inds_one_w_data_both_two_nested_both_both_w_data()
    ),
    (
        "strat_two_inds_one_w_data_both_two_nested_one_both_w_data",
        strat_two_inds_one_w_data_both_two_nested_one_both_w_data()
    ),
    (
        "strat_two_inds_one_w_data_both_two_nested_both_both_no_data",
        strat_two_inds_one_w_data_both_two_nested_both_both_no_data()
    ),
    (
        "strat_two_inds_w_data_one_two_nested_w_data",
        strat_two_inds_w_data_one_two_nested_w_data()
    ),
    (
        "strat_two_inds_w_data_one_two_nested_one_w_data",
        strat_two_inds_w_data_one_two_nested_one_w_data()
    ),
    (
        "strat_two_inds_w_data_one_two_nested_no_data",
        strat_two_inds_w_data_one_two_nested_no_data()
    ),
    (
        "strat_two_inds_no_data_one_two_nested_w_data",
        strat_two_inds_no_data_one_two_nested_w_data()
    ),
    (
        "strat_two_inds_no_data_one_two_nested_one_w_data",
        strat_two_inds_no_data_one_two_nested_one_w_data()
    ),
    (
        "strat_two_inds_no_data_one_two_nested_no_data",
        strat_two_inds_no_data_one_two_nested_no_data()
    ),
    (
        "strat_two_inds_one_w_data_one_two_nested_w_data",
        strat_two_inds_one_w_data_one_two_nested_w_data()
    ),
    (
        "strat_two_inds_one_w_data_one_two_nested_one_w_data",
        strat_two_inds_one_w_data_one_two_nested_one_w_data()
    ),
    (
        "strat_two_inds_one_w_data_one_two_nested_no_data",
        strat_two_inds_one_w_data_one_two_nested_no_data()
    )
]

indicators = [
    (
        "ind_w_data_not_nested",
        ind_w_data_not_nested()
    ),
    (
        "ind_no_data_not_nested",
        ind_no_data_not_nested()
    ),
    (
        "ind_w_data_one_nested_with_data",
        ind_w_data_one_nested_with_data()
    ),
    (
        "ind_w_data_one_nested_no_data",
        ind_w_data_one_nested_no_data()
    ),
    (
        "ind_no_data_one_nested_with_data",
        ind_no_data_one_nested_with_data()
    ),
    (
        "ind_no_data_one_nested_no_data",
        ind_no_data_one_nested_no_data()
    ),
    (
        "ind_w_data_two_nested_with_data",
        ind_w_data_two_nested_with_data()
    ),
    (
        "ind_w_data_two_nested_no_data",
        ind_w_data_two_nested_no_data()
    ),
    (
        "ind_w_data_two_nested_one_with_data",
        ind_w_data_two_nested_one_with_data()
    ),
    (
        "ind_no_data_two_nested_with_data",
        ind_no_data_two_nested_with_data()
    ),
    (
        "ind_no_data_two_nested_no_data",
        ind_no_data_two_nested_no_data()
    ),
    (
        "ind_no_data_two_nested_one_with_data",
        ind_no_data_two_nested_one_with_data()
    ),
    (
        "ind_w_data_three_nested_with_data",
        ind_w_data_three_nested_with_data()
    ),
    (
        "ind_w_data_three_nested_no_data",
        ind_w_data_three_nested_no_data()
    ),
    (
        "ind_w_data_three_nested_one_with_data",
        ind_w_data_three_nested_one_with_data()
    ),
    (
        "ind_w_data_three_nested_two_with_data",
        ind_w_data_three_nested_two_with_data()
    ),
    (
        "ind_no_data_three_nested_with_data",
        ind_no_data_three_nested_with_data()
    ),
    (
        "ind_no_data_three_nested_no_data",
        ind_no_data_three_nested_no_data()
    ),
    (
        "ind_no_data_three_nested_one_with_data",
        ind_no_data_three_nested_one_with_data()
    ),
    (
        "ind_no_data_three_nested_two_with_data",
        ind_no_data_three_nested_two_with_data()
    )
]

strategies = [
    (
        "strat_no_ind",
        strat_no_ind()
    ),
    (
        "strat_one_ind_no_data_not_nested",
        strat_one_ind_no_data_not_nested()
    ),
    (
        "strat_one_ind_w_data_not_nested",
        strat_one_ind_w_data_not_nested()
    ),
    (
        "strat_one_ind_w_data_one_nested_w_data",
        strat_one_ind_w_data_one_nested_w_data()
    ),
    (
        "strat_one_ind_w_data_one_nested_no_data",
        strat_one_ind_w_data_one_nested_no_data()
    ),
    (
        "strat_one_ind_no_data_one_nested_w_data",
        strat_one_ind_no_data_one_nested_w_data()
    ),
    (
        "strat_one_ind_no_data_one_nested_no_data",
        strat_one_ind_no_data_one_nested_no_data()
    ),
    (
        "strat_one_ind_w_data_two_nested_w_data",
        strat_one_ind_w_data_two_nested_w_data()
    ),
    (
        "strat_one_ind_w_data_two_nested_no_data",
        strat_one_ind_w_data_two_nested_no_data()
    ),
    (
        "strat_one_ind_w_data_two_nested_one_with_data",
        strat_one_ind_w_data_two_nested_one_with_data()
    ),
    (
        "strat_one_ind_no_data_two_nested_w_data",
        strat_one_ind_no_data_two_nested_w_data()
    ),
    (
        "strat_one_ind_no_data_two_nested_no_data",
        strat_one_ind_no_data_two_nested_no_data()
    ),
    (
        "strat_one_ind_no_data_two_nested_one_with_data",
        strat_one_ind_no_data_two_nested_one_with_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_w_data",
        strat_one_ind_w_data_three_nested_w_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_no_data",
        strat_one_ind_w_data_three_nested_no_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_one_with_data",
        strat_one_ind_w_data_three_nested_one_with_data()
    ),
    (
        "strat_one_ind_w_data_three_nested_two_with_data",
        strat_one_ind_w_data_three_nested_two_with_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_w_data",
        strat_one_ind_no_data_three_nested_w_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_no_data",
        strat_one_ind_no_data_three_nested_no_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_one_with_data",
        strat_one_ind_no_data_three_nested_one_with_data()
    ),
    (
        "strat_one_ind_no_data_three_nested_two_with_data",
        strat_one_ind_no_data_three_nested_two_with_data()
    ),
    (
        "strat_two_inds_w_data_non_nested",
        strat_two_inds_w_data_non_nested()
    ),
    (
        "strat_two_inds_no_data_non_nested",
        strat_two_inds_no_data_non_nested()
    ),
    (
        "strat_two_inds_one_w_data_non_nested",
        strat_two_inds_one_w_data_non_nested()
    ),
    (
        "strat_two_inds_w_data_one_one_nested_w_data",
        strat_two_inds_w_data_one_one_nested_w_data()
    ),
    (
        "strat_two_inds_w_data_one_one_nested_no_data",
        strat_two_inds_w_data_one_one_nested_no_data()
    ),
    (
        "strat_two_inds_no_data_one_one_nested_w_data",
        strat_two_inds_no_data_one_one_nested_w_data()
    ),
    (
        "strat_two_inds_no_data_one_one_nested_no_data",
        strat_two_inds_no_data_one_one_nested_no_data()
    ),
    (
        "strat_two_inds_one_w_data_one_one_nested_w_data",
        strat_two_inds_one_w_data_one_one_nested_w_data()
    ),
    (
        "strat_two_inds_one_w_data_one_one_nested_no_data",
        strat_two_inds_one_w_data_one_one_nested_no_data()
    ),
    (
        "strat_two_inds_w_data_both_one_nested_w_data",
        strat_two_inds_w_data_both_one_nested_w_data()
    ),
    (
        "strat_two_inds_w_data_both_one_nested_no_data",
        strat_two_inds_w_data_both_one_nested_no_data()
    ),
    (
        "strat_two_inds_no_data_both_one_nested_w_data",
        strat_two_inds_no_data_both_one_nested_w_data()
    ),
    (
        "strat_two_inds_no_data_both_one_nested_no_data",
        strat_two_inds_no_data_both_one_nested_no_data()
    ),
    (
        "strat_two_inds_one_w_data_both_one_nested_w_data",
        strat_two_inds_one_w_data_both_one_nested_w_data()
    ),
    (
        "strat_two_inds_one_w_data_both_one_nested_no_data",
        strat_two_inds_one_w_data_both_one_nested_no_data()
    ),
    (
        "strat_two_inds_w_data_both_two_nested_both_both_w_data",
        strat_two_inds_w_data_both_two_nested_both_both_w_data()
    ),
    (
        "strat_two_inds_w_data_both_two_nested_one_both_w_data",
        strat_two_inds_w_data_both_two_nested_one_both_w_data()
    ),
    (
        "strat_two_inds_w_data_both_two_nested_both_both_no_data",
        strat_two_inds_w_data_both_two_nested_both_both_no_data()
    ),
    (
        "strat_two_inds_no_data_both_two_nested_both_both_w_data",
        strat_two_inds_no_data_both_two_nested_both_both_w_data()
    ),
    (
        "strat_two_inds_no_data_both_two_nested_one_both_w_data",
        strat_two_inds_no_data_both_two_nested_one_both_w_data()
    ),
    (
        "strat_two_inds_no_data_both_two_nested_both_both_no_data",
        strat_two_inds_no_data_both_two_nested_both_both_no_data()
    ),
    (
        "strat_two_inds_one_w_data_both_two_nested_both_both_w_data",
        strat_two_inds_one_w_data_both_two_nested_both_both_w_data()
    ),
    (
        "strat_two_inds_one_w_data_both_two_nested_one_both_w_data",
        strat_two_inds_one_w_data_both_two_nested_one_both_w_data()
    ),
    (
        "strat_two_inds_one_w_data_both_two_nested_both_both_no_data",
        strat_two_inds_one_w_data_both_two_nested_both_both_no_data()
    ),
    (
        "strat_two_inds_w_data_one_two_nested_w_data",
        strat_two_inds_w_data_one_two_nested_w_data()
    ),
    (
        "strat_two_inds_w_data_one_two_nested_one_w_data",
        strat_two_inds_w_data_one_two_nested_one_w_data()
    ),
    (
        "strat_two_inds_w_data_one_two_nested_no_data",
        strat_two_inds_w_data_one_two_nested_no_data()
    ),
    (
        "strat_two_inds_no_data_one_two_nested_w_data",
        strat_two_inds_no_data_one_two_nested_w_data()
    ),
    (
        "strat_two_inds_no_data_one_two_nested_one_w_data",
        strat_two_inds_no_data_one_two_nested_one_w_data()
    ),
    (
        "strat_two_inds_no_data_one_two_nested_no_data",
        strat_two_inds_no_data_one_two_nested_no_data()
    ),
    (
        "strat_two_inds_one_w_data_one_two_nested_w_data",
        strat_two_inds_one_w_data_one_two_nested_w_data()
    ),
    (
        "strat_two_inds_one_w_data_one_two_nested_one_w_data",
        strat_two_inds_one_w_data_one_two_nested_one_w_data()
    ),
    (
        "strat_two_inds_one_w_data_one_two_nested_no_data",
        strat_two_inds_one_w_data_one_two_nested_no_data()
    )
]

data = [
    (
        "valid_data_one_candle",
        valid_data_one_candle
    ),
    (
        "valid_data_two_candles",
        valid_data_two_candles
    ),
    (
        "valid_data_three_candles",
        valid_data_three_candles
    )
]