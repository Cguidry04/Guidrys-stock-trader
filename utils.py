def place_order(symbol, qty, side, mode):
    print(f"Placing {side} order for {qty} shares of {symbol} in {mode}")

def log_trade(signal, timestamp):
    with open("trades.log", "a") as f:
        f.write(f"{timestamp}: {signal}\n")