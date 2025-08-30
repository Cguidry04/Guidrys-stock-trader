import streamlit as st
from trading_bot import TradingBot
import yaml

st.set_page_config(page_title="AI Stock Trading Bot", layout="wide")

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

bot = TradingBot(config)

st.title("📈 AI Stock Trading Bot 2025")

mode = st.radio("Select Mode:", ["Paper Trading", "Live Trading"])

if st.button("Start Trading"):
    bot.run(mode)
    st.success(f"Bot started in {mode} mode!")