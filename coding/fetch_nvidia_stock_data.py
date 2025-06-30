# filename: fetch_nvidia_stock_data.py
import yfinance as yf
import pandas as pd

# Define the ticker symbol and date range
ticker_symbol = 'NVDA'
start_date = '2024-03-23'
end_date = '2024-04-23'

# Fetch historical stock price data
nvidia_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Show the retrieved data
print(nvidia_data[['Open', 'High', 'Low', 'Close', 'Volume']])