# -*- coding: utf-8 -*-

import talib


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



class FeatureExtractor:
    def __init__(self, data, processed_data_path='data/processed/'):
        self.data = data
        self.processed_data_path = processed_data_path

    def get_dollar_volume(self):
        self.data['dollar_volume'] = (self.data['Close'] * self.data['Volume']).prod(axis=1)

    def get_RSI(self, window=14):
        self.data['rsi'] = talib.RSI(self.data['Close'], timeperiod=window)

    def get_bbands(self, window=20, num_std=20):
        upper_band, middle_band, lower_band = talib.BBANDS(self.data['Close'], timeperiod=window, nbdevup=num_std, nbdevdn=num_std)

        self.data['upper_band'] = upper_band
        self.data['middle_band'] = middle_band
        self.data['lower_band'] = lower_band

    def get_atr(self, window=14):
        atr = talib.ATR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=window)
        self.data['atr'] = atr

    def get_natr(self, window=14):
        natr = talib.NATR(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=window)
        self.data['natr'] = natr

    def get_macd(self, fast_period=12, slow_period=26, signal_period=9):
        macd, signal, _ = talib.MACD(self.data['Close'], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
        self.data['macd'] = macd
        self.data['macd_signal'] = signal

    def get_ppo(self, fast_period=12, slow_period=26, signal_period=9):
        ppo = talib.PPO(self.data['Close'], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
        self.data['ppo'] = ppo

    def get_obv(self, volume_column='Volume'):
        obv = talib.OBV(self.data['Close'], self.data[volume_column])
        self.data['obv'] = obv

    def get_adx(self, window=14):
        adx = talib.ADX(self.data['High'], self.data['Low'], self.data['Close'], timeperiod=window)
        self.data['adx'] = adx

    def get_cmf(self, window=20):
        cmf = talib.CMF(self.data['High'], self.data['Low'], self.data['Close'], self.data['Volume'], timeperiod=window)
        self.data['cmf'] = cmf

    def get_date_dummy(self):
        self.data['year'] = self.data.index.year
        self.data['month'] = self.data.index.month
        self.data['weekday'] = self.data.index.weekday

    def get_stochastic_oscillator(self, fast_k_period=14, slow_d_period=3):
        k, d = talib.STOCH(self.data['High'], self.data['Low'], self.data['Close'], fastk_period=fast_k_period, slowk_period=3, slowd_period=slow_d_period)
        self.data['stoch_k'] = k
        self.data['stoch_d'] = d
        
        
    
    def get_ichimoku_cloud(self, tenkan_period=9, kijun_period=26, senkou_span_b_period=52, displacement=26):
        high_prices = self.data['High']
        low_prices = self.data['Low']
        close_prices = self.data['Close']

        tenkan_sen = talib.SMA(high_prices + low_prices, timeperiod=tenkan_period) / 2
        kijun_sen = talib.SMA(high_prices + low_prices, timeperiod=kijun_period) / 2

        senkou_span_a = (tenkan_sen + kijun_sen) / 2
        senkou_span_b = talib.SMA(high_prices + low_prices, timeperiod=senkou_span_b_period) / 2

        senkou_span_a = senkou_span_a.shift(displacement)
        senkou_span_b = senkou_span_b.shift(displacement)

        self.data['tenkan_sen'] = tenkan_sen
        self.data['kijun_sen'] = kijun_sen
        self.data['senkou_span_a'] = senkou_span_a
        self.data['senkou_span_b'] = senkou_span_b

    def get_sma(self, window=20):
        close_prices = self.data['Close']
        sma = talib.SMA(close_prices, timeperiod=window)
        self.data['sma'] = sma

    def get_ema(self, window=20):
        close_prices = self.data['Close']
        ema = talib.EMA(close_prices, timeperiod=window)
        self.data['ema'] = ema

	
		
