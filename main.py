# main.py

from SharesOutstanding import get_shares_outstanding

def main():
    # Prompt the user to enter a ticker symbol
    ticker = input("Enter the ticker symbol: ")

    # Call the function to get shares outstanding
    shares_outstanding = get_shares_outstanding(ticker)

    if shares_outstanding is not None:
        print(f"Shares Outstanding for {ticker}: {shares_outstanding}")
    else:
        print(f"Failed to retrieve shares outstanding for {ticker}")

if __name__ == "__main__":
    main()

