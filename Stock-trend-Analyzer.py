import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = input("Enter the Ticker of the Company: ").upper()

df = yf.download(ticker, period='2y')
if df.empty:
    print("Invalid Input")
    exit()

prices = df["Adj Close"] if "Adj Close" in df else df["Close"]

df2 = pd.DataFrame()
df2["Price"] = prices
df2["Momentum"] = prices.pct_change(20)
df2["20MA"] = prices.rolling(20).mean()
returns = prices.pct_change()
df2["Volatility"] = returns.rolling(20).std()

df2 = df2.dropna()

last = df2.iloc[-1]

p  = float(last["Price"])
m  = float(last["Momentum"])
ma = float(last["20MA"])
vol = float(last["Volatility"])

avg_vol = df2["Volatility"].mean()
low_vol_threshold = avg_vol * 1.2

if any(np.isnan([p, m, ma, vol])):
    signal = "Insufficient Data"
elif p > ma and vol < low_vol_threshold and m > 0.04:
    signal = "Strong Uptrend"
elif p > ma and vol < low_vol_threshold and 0 < m <= 0.04:
    signal = "Weak Uptrend"
elif p < ma and vol < low_vol_threshold and m < -0.04:
    signal = "Strong Downtrend"
elif p < ma and vol < low_vol_threshold and -0.04 <= m < 0:
    signal = "Weak Downtrend"
else:
    signal = "Uncertain"

print("Trend Signal:", signal)
print(f"Price: {p:.2f}, MA20: {ma:.2f}, Momentum: {m:.4f}, Volatility: {vol:.4f}")



