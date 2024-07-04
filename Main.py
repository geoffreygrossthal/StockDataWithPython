from StockSplits import get_stock_splits
from SharesOutstanding import get_shares_outstanding
from DataFrame import get_ticker_data 
from ForwardPE import get_forward_pe

def display_menu():
    print("\nMenu:")
    print("1. Get Stock Splits")
    print("2. Get Shares Outstanding")
    print("3. Get Ticker Data")
    print("4. Get Forward P/E Ratio")
    print("5. Exit")

def handle_stock_splits(ticker):
    splits_data = get_stock_splits(ticker)
    if isinstance(splits_data, str):
        print(splits_data) 
    else:
        print(f"Stock Splits for {ticker}:")
        print(splits_data)

def handle_shares_outstanding(ticker):
    shares_outstanding = get_shares_outstanding(ticker)
    if shares_outstanding is not None:
        print(f"Shares Outstanding for {ticker}: {shares_outstanding}")
    else:
        print(f"Failed to retrieve shares outstanding for {ticker}")

def handle_ticker_data(ticker):
    ticker_data = get_ticker_data(ticker)
    if ticker_data is not None:
        print(f"\nData for Ticker: {ticker}")
        print(ticker_data)
    else:
        print(f"Failed to retrieve data for {ticker}")

def handle_forward_pe(ticker):
    forward_pe_ratio = get_forward_pe(ticker)
    if forward_pe_ratio is not None:
        print(f"Forward P/E Ratio for {ticker}: {forward_pe_ratio}")
    else:
        print(f"Failed to retrieve forward P/E ratio for {ticker}")


def main():
    ticker_symbol = input("Enter the ticker symbol: ")

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        print()

        if choice == '1':
            handle_stock_splits(ticker_symbol)
        
        elif choice == '2':
            handle_shares_outstanding(ticker_symbol)
        
        elif choice == '3':
            handle_ticker_data(ticker_symbol)
        
        elif choice == '4':
            handle_forward_pe(ticker_symbol)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()

