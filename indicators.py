import pandas as pd
import ta

class Indicators:
    def get_data(self, ticker):
        # placeholder - fetch OHLCV data from Alpaca or Alpha Vantage
        return pd.DataFrame()

    def calculate_all(self, df):
        df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
        df['macd'] = ta.trend.MACD(df['close']).macd()
        df['ema20'] = ta.trend.EMAIndicator(df['close'], window=20).ema_indicator()
        return df