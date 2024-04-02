# A class for all need  to backtest a strategy

import pandas as pd
import numpy as np

class Cerebro:
    def __init__(self, strategy, data, cash, InitialPortfolio = None):
        self.strategy = strategy
        self.data = data
        self.cash = cash
        self.portfolio = InitialPortfolio

    def print_state(self):
        print('Cash: ', self.cash)
        print('Strategy: ', self.strategy)
        print('Data: ', self.data)
        print('Portfolio: ', self.portfolio)