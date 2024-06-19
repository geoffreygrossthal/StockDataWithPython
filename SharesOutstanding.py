
"""
Get the shares outstanding for a given stock ticker.
Parameters:
ticker (str): Stock ticker symbol.
Returns:
float or None: Shares outstanding if available, else None.
"""
import yfinance as yf

def get_shares_outstanding(ticker):
    try:
        # Create a Ticker object for the given ticker symbol
        stock = yf.Ticker(ticker)

        # Get the shares outstanding information
        shares_outstanding = stock.info.get("sharesOutstanding")

        return shares_outstanding
    except Exception as e:
        print(f"Error fetching shares outstanding for {ticker}: {e}")
        return None
