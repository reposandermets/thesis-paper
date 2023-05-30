import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download(['SPY'], start="2000-01-01", end="2023-01-31", interval="1mo")

# Calculate monthly returns
# data['Monthly Returns'] = data['Adj Close'].pct_change()

data['Monthly Returns'] = 100 * ((data['Adj Close']/ data['Adj Close'].shift(1)) - 1)

# Remove NaN values (the first row will have a NaN value for monthly returns)
data = data.dropna()

# Plot the histogram of monthly returns
plt.figure(figsize=(14, 7))
plt.hist(data['Monthly Returns'], bins=50, edgecolor='k', alpha=0.75)
plt.xlabel('Igakuised tootlused')
plt.ylabel('Sagedus')
plt.title('SPY igakuiste tootluste tulpdiagramm')
plt.grid(True)
plt.show()
