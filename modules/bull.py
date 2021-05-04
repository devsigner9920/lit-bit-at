import pyupbit
from modules import market


def get_bull(market_name=""):
    ohlcv = pyupbit.get_ohlcv(market_name)
    ma5 = ohlcv['close'].rolling(window=5).mean()
    last_ma5 = ma5[-2]

    price = pyupbit.get_current_price(market_name)

    if price > last_ma5:
        return True
    else:
        return False


