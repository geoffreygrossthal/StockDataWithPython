"""
Get the forward Price-to-Earnings (P/E) ratio for a given stock ticker.
Parameters:
ticker (str): Stock ticker symbol.
Returns:
float or None: Forward P/E ratio if available, else None.
"""

import yfinance as yf

def get_forward_pe(ticker):
    try:
        stock = yf.Ticker(ticker)
        forward_pe = stock.info.get("forwardPE")
        return forward_pe
    except Exception as e:
        print(f"Error fetching forward P/E ratio for {ticker}: {e}")
        return None