import datetime
from indicators import Indicators
from models import MLModels
from utils import place_order, log_trade

class TradingBot:
    def __init__(self, config):
        self.config = config
        self.indicators = Indicators()
        self.models = MLModels()

    def run(self, mode="Paper Trading"):
        # Fetch data (placeholder)
        data = self.indicators.get_data("AAPL")
        
        # Generate features
        features = self.indicators.calculate_all(data)
        
        # Predict signal
        signal = self.models.predict(features)
        
        # Place trade
        if signal == "BUY":
            place_order("AAPL", 1, "buy", mode)
        elif signal == "SELL":
            place_order("AAPL", 1, "sell", mode)
        
        # Log
        log_trade(signal, datetime.datetime.now())