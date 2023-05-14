import yfinance as yf

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = yf.download(['SPY'], start="2000-01-01", end="2023-01-31", interval="1mo")

plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Adj Close'])
plt.xlabel('Aeg')
plt.ylabel('Korrigeeritud sulgemishind')
plt.title('SPY korrigeeritud sulgemishinna ajalugu')
plt.grid(True)
plt.yscale('log')
plt.show()
