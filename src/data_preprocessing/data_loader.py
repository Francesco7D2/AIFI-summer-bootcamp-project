# -*- coding: utf-8 -*-
"""
Data Loader Class
"""

import yfinance as yf
import pandas as pd
import os

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)




class DataLoader:
    def __init__(self, tickers, start_date, end_date, raw_data_path='data/raw/'):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.raw_data_path = raw_data_path
        self.data = None

    def download_data(self, interval='daily', name_file_out="raw_data.csv"):
        data_frames = []
        for ticker in self.tickers:
            stock_data = yf.download(ticker, start=self.start_date, end=self.end_date)
            data_frames.append(stock_data)

        self.data = pd.concat(data_frames, keys=self.tickers, names=['Ticker', 'Date'])

        raw_data_file = os.path.join(self.raw_data_path, name_file_out)
        self.data.to_csv(raw_data_file)

    def basic_preprocessing(self, feature='Adj Close'):
        self.data = self.data[feature]

    def load_data(self, interval='daily', feature='Adj Close'):
        if self.data is None:
            self.download_data(interval)

        self.basic_preprocessing(feature)

        return self.data

