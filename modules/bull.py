import pyupbit
from modules import market

def get_bull(markets=[]):
    result = []
    print(type(markets))
    if not markets == None:
        for market in markets:
            print(market)
            ohlcv = pyupbit.get_ohlcv(market)
            result.append(ohlcv['close'].rolling(5).mean())
        
        return result
    else:
        print("ASdasda")

