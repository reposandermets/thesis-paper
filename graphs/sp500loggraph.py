import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data = yf.download(['SPY'], start="2000-01-01", end="2023-01-31", interval="1mo")

# Plot the adjusted close price as a time series
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(data.index, data['Adj Close'])
ax.set_xlabel('Aeg')
ax.set_ylabel('Korrigeeritud sulgemishind')
ax.set_title('SPY korrigeeritud sulgemishinna ajalugu')
ax.grid(True)

# Apply logarithmic scale
ax.set_yscale('log')

# Customize y-axis ticks to display prices
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))
ax.yaxis.set_major_locator(ticker.LogLocator(base=2, numticks=100))

plt.show()
