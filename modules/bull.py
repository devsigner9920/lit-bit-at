import pyupbit
from modules import market


def get_bull(market=""):
    ohlcv = pyupbit.get_ohlcv(market)
    ma5 = ohlcv['close'].rolling(window=5).mean()
    last_ma5 = ma5[-2]

    price = pyupbit.get_current_price(market)

    if price > last_ma5:
        return True
    else:
        return False


