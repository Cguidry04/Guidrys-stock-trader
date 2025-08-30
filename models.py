from sklearn.ensemble import RandomForestClassifier

class MLModels:
    def __init__(self):
        self.model = RandomForestClassifier()

    def predict(self, features):
        # placeholder logic
        return "BUY" if features['rsi'].iloc[-1] < 30 else "SELL" if features['rsi'].iloc[-1] > 70 else "HOLD" 