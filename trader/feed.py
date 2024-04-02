# get Data from MongoDB

import pandas as pd
import numpy as np
from pymongo import MongoClient

def get_data(symbol,date):
    #[str] symbol : "BTC/USDT"
    #[str] date : "2021-01-01"
    # ====sample====
    # feed.get_data(symbol = 'BTC/USDT', date= '2024-04-01')

    client = MongoClient('localhost', 27017)
    db = client['crypto']
    collection = db['ohlcv']
    query = {'symbol':symbol,'date':date}
    data = pd.DataFrame((collection.find_one(query)['data']))
    return data