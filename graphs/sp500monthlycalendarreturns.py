import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download(['SPY'], start="2000-01-01", end="2023-01-31", interval="1mo")

# Calculate monthly returns
data['Monthly Returns'] = data['Adj Close'].pct_change()

# Remove NaN values (the first row will have a NaN value for monthly returns)
data = data.dropna()

# Group data by calendar month and calculate mean returns
mean_monthly_returns = data.groupby(data.index.month)['Monthly Returns'].mean()

# Plot the bar chart of mean monthly returns
months = ['Jaanuar', 'Veebruar', 'Märts', 'Aprill', 'Mai', 'Juuni', 'Juuli', 'August', 'September', 'Oktoober', 'November', 'Detsember']
plt.figure(figsize=(14, 7))
plt.bar(months, mean_monthly_returns * 100)
plt.xlabel('Kuu')
plt.ylabel('Keskmine tootlus (%)')
plt.title('SPY keskmine igakuine tootlus kalendrikuude alusel')
plt.grid(True)
plt.show()
