"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""
import csv

def searchStock(ticker):
    data = list(csv.reader(open('task5.csv', 'r')))

    exact_matches = [i for i in data if i[0] == ticker]

    if len(exact_matches) == 1:
        print(f"Company Name: {exact_matches[0][1]}")
    elif len(exact_matches) > 1:
        print(f"There are {len(exact_matches)} companies with the exact ticker '{ticker}'.")
    else:
        #if no exact, then partial
        partial_matches = [i for i in data if ticker in i[0]]
        
        if len(partial_matches) > 1:
            print(f"There are {len(partial_matches)} companies that have {ticker} in their ticker.")
        elif len(partial_matches) == 1:
            print(f"Company Name: {partial_matches[0][1]}")
        else:
            print("No match found.")

ticker = input("Enter the stock symbol to search: ").strip().upper()
searchStock(ticker)