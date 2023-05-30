import yfinance as yf
import pandas as pd
import numpy as np

data = yf.download(['SPY'], start="2000-01-01", end="2023-01-31", interval="1mo")

# Calculate monthly returns
data['Monthly Returns'] = data['Adj Close'].pct_change()

# Remove NaN values (the first row will have a NaN value for monthly returns)
data = data.dropna()

# Calculate standard deviation of monthly returns
std_dev = data['Monthly Returns'].std()

print("Standard deviation of monthly returns:", std_dev)
