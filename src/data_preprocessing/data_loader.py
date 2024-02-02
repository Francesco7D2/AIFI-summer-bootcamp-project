# -*- coding: utf-8 -*-
"""
Data Loader Class
"""

import yfinance as yf
import pandas as pd
import logging



class DataLoader:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.logger = logging.getLogger(__name__)

    def load_data(self, frequency="daily"):
        self.logger.info(f"Downloading {self.ticker} data from {self.start_date} to {self.end_date} with frequency {frequency}")
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date, interval=frequency)
            self.logger.info("Data downloaded successfully.")
            return data
        except Exception as e:
            self.logger.error(f"Error downloading data: {str(e)}")
            return None

    def save_data(self, file_path):
        data = self.load_data()
        if data is not None:
            data.to_csv(file_path)
            self.logger.info(f'Data saved to {file_path}')

    def load_from_file(self, file_path):
        try:
            data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
            self.logger.info(f'Data loaded from {file_path}')
            return data
        except Exception as e:
            self.logger.error(f"Error loading data from file: {str(e)}")
            return None