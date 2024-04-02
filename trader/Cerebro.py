# A class for all that need to backtest a strategy

import pandas as pd
import numpy as np

class Strategy:
    def __init__(self, data):
        self.data = data
        self.dataclose = self.data['close']
    
    def next(self, index):
        # 示例策略: 当前价格低于前一天，则买入; 高于前一天，则卖出
        if index > 0:
            if self.dataclose[index] < self.dataclose[index - 1]:
                return 0.001
            elif self.dataclose[index] > self.dataclose[index - 1]:
                return -0.001
        return 0

class Cerebro:
    def __init__(self, strategy, InitialPortfolio = None):
        self.strategy = strategy # 策略实例
        self.data = strategy.data
        self.portfolio = InitialPortfolio if InitialPortfolio is not None else {'USDT' : 0}
        self.trades = []

    def print_state(self):
        print(f'Portfolio: {self.portfolio}')

    def buy(self, symbol ,index, amount):
        price = self.data['close'][index]
        if self.portfolio['USDT'] >= price * amount:
            self.portfolio['USDT'] -= price * amount
            self.portfolio.setdefault(symbol, 0)
            self.portfolio[symbol] += amount
            print(f'Bought {amount} for {price} each at index {index}')

    def sell(self,symbol,index, amount):
        if self.portfolio.get(symbol, 0) >= amount:
            price = self.data['close'][index]
            self.portfolio['USDT'] += price * amount
            self.portfolio[symbol] -= amount
            print(f'Sold {amount} for {price} each at index {index}')

    def run(self,symbol):
        for index in range(len(self.data)):
            decision = self.strategy.next(index)
            if decision > 0 :
                self.buy(symbol, index, abs(decision))  # 买入1单位
            elif decision < 0 and self.portfolio.get(symbol, 0) > 0:
                self.sell(symbol, index, abs(decision))  # 卖出1单位
            # self.print_state(index)
