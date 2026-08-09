import yfinance as yf

"""Collecting the Data that is needed for the program"""
from financial_data import load_financial_data
from financial_data import get_historical_data
from display import print_company_summary
from charting import plot_revenue

"""Stock Ticker Assignment"""
#Asks for input, assigns value and prints the name to check if you have the right company
while True:
    ticker = input("Enter ticker to analyze: ").upper()
    stock = yf.Ticker(ticker)

    try:
        company_name = stock.info["longName"]
        break

    except KeyError:
        print(f"Couldn't find a stock with ticker '{ticker}'. Please enter ticker again.")

while True:
    print("\nSelect analysis period:")
    print("[1] Annual")
    print("[2] Quarterly")

    choice = input("Enter Choice: ").strip().lower()

    if choice in("1", "annual"):
        period = "annual"
        break
    elif choice in("2", "quarterly"):
        period = "quarterly"
        break
    else:
        print("Invalid Choice. Please try again.")


"""Financial Data"""
financials = load_financial_data(
    stock,
    period=period
)

"""Actual Display"""
print_company_summary(stock,financials)

revenue = get_historical_data(
        stock,
        "Total Revenue",
        period= period
    )
plot_revenue(revenue, period=period)