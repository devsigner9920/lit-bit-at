import json

#from server import database
import requests


def get_market():
    '''
    db = database.db()
    db.delete(
        """
        DELETE
          FROM m_market
        """
    )
    '''
    url = "https://api.upbit.com/v1/market/all"

    querystring = {"isDetails": "true"}

    response = requests.request("GET", url, params=querystring)

    market_dict = json.loads(response.text)

    return market_dict

    # for mk in market_dict:
    #     db.insert("INSERT INTO 'm_market' "
    #               "('market', 'korean_name', 'english_name', 'market_warning') "
    #               "VALUES "
    #               "(%s, %s, %s, %s)",
    #               [mk['market'],
    #                mk['korean_name'],
    #                mk['english_name'],
    #                mk['market_warning']])

    #print(db.select("select * from m_market where market like '%s'" % '%KRW-BTC'))
