import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for Amazon
symbol = "AMZN"

# Define the start and end dates for the data
start_date = "2015-01-01"
end_date = "2021-12-31"

# Retrieve the historical data for the stock price of Amazon
data = yf.download(symbol, start=start_date, end=end_date)

# Read the market capitalization and revenue data from a CSV file
# You can download the CSV file from the SEC website or other financial data providers
financials = pd.read_csv("https://www.sec.gov/files/company_tickers/ticker_master.csv")
market_cap = financials[financials["ticker"] == symbol]["market_cap"].values[0]
revenue = financials[financials["ticker"] == symbol]["revenue"].values[0]

# Calculate the PS ratio
ps_ratio = market_cap / revenue

# Plot the stock price and PS ratio as subplots
fig, axs = plt.subplots(2, sharex=True, figsize=(12, 8))
fig.suptitle("Amazon Stock Price and Price-to-Sales Ratio (2015-2021)")

# Plot the stock price as the first subplot
axs[0].plot(data["Close"])
axs[0].set_ylabel("Stock Price ($)")
axs[0].grid(True)

# Plot the PS ratio as the second subplot
axs[1].fill_between(data.index, ps_ratio, alpha=0.3)
axs[1].plot(ps_ratio, color="blue")
axs[1].set_ylabel("Price-to-Sales Ratio")
axs[1].grid(True)

# Save the chart as a PNG file
plt.savefig("amazon_stock_price_ps_ratio.png")
plt.show()
