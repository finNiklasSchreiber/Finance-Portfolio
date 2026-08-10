import yfinance as yf
import os

"""Collecting the Data that is needed for the program"""
from financial_data import(
    load_financial_data,
    get_historical_data
)
from display import print_company_summary
from charting import plot_revenue
from calculations import(
    calculate_historical_numbers,
    calculate_growth
)
from report import(
    create_report
)

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

"""Historical Data"""
revenue = get_historical_data(
        stock,
        "Total Revenue",
        period= period
    )

"""Historical Revenue Growth"""
historical_growth = calculate_historical_numbers(
    revenue,
    calculate_growth
)
"""Revenue Chart"""
chart_path = os.path.join(
    "output",
    f"{ticker}_{period}_revenue.png"
)

plot_revenue(
    revenue,
    period=period,
    save_path=chart_path
)

"""Actual Display"""
print_company_summary(stock,financials)

"""Historical Growth Display"""
print("\nHistorical Revenue Growth:")

for date, growth in historical_growth.items():
    print(f"{date.year}: {growth:.2f}%")

"""Creating output"""
create_report(
    company_name,
    ticker,
    period,
    financials,
    revenue,
    historical_growth,
    chart_path
)