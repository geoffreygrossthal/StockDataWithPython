import pandas as pd
import yfinance as yf

def get_ticker_data(ticker):
    try:
        ticker_object = yf.Ticker(ticker)

        # Convert info() output from dictionary to dataframe
        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
        temp.reset_index(inplace=True)
        temp.columns = ["Attribute", "Recent"]

        return temp
    except Exception as e:
        print(f"Error occurred for {ticker}: {str(e)}")
        return None