# Tested on Ubuntu. Require GTK3.
"""
sudo apt-get update
sudo apt-get install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0
"""

import yfinance as yf
import pandas as pd
import matplotlib

# Set the backend to TkAgg
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt

# Download Amazon's stock data
ticker = "AMZN"
start_date = "2020-01-01"
end_date = "2023-03-31"

data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the PS bands
window = 20
data['Upper_PS'] = data['High'].rolling(window=window).max()
data['Lower_PS'] = data['Low'].rolling(window=window).min()

# Create a plot
plt.figure(figsize=(14, 8))
plt.plot(data.index, data['Close'], label=f'{ticker} Close Price', color='black', alpha=0.5)
plt.plot(data.index, data['Upper_PS'], label='Upper PS Band', color='red', alpha=0.7)
plt.plot(data.index, data['Lower_PS'], label='Lower PS Band', color='blue', alpha=0.7)

# Customize the plot
plt.title(f'{ticker} Stock Chart with PS Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid()

# Show the plot
plt.show()
