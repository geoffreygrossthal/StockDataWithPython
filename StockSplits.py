"""
Retrieve the stock splits for a given ticker symbol.

Args:
ticker (str): The ticker symbol of the stock.

Returns:
- pandas.DataFrame: A DataFrame containing stock splits information if available.
- str: A message indicating no stock splits found for the given ticker if splits are empty.
- str: An error message if an exception occurs during the retrieval process.
"""

import yfinance as yf

def get_stock_splits(ticker):
    try:
        stock = yf.Ticker(ticker)
        splits = stock.splits
        if not splits.empty:
            return splits
        else:
            return f"No stock splits found for {ticker}"
    except Exception as e:
        return f"Error occurred: {str(e)}"
