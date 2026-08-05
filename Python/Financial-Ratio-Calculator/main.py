import yfinance as yf

"""Collecting the Data that is needed for the program"""
from financial_data import get_financial_value
from calculations import calculate_growth
from calculations import calculate_margin
from display import print_company_summary


"""Stock Ticker Assignment"""
#Asks for input, assigns value and prints the name to check if you have the right company
ticker = input("Enter ticker to analyze: ").upper()
stock = yf.Ticker(ticker)
company_name = stock.info["longName"]

"""Financial Data"""
#These 3 are for calculating growth and getting the important numbers from the statement
revenue = get_financial_value(
    stock,
    "Total Revenue"
)
gross_profit, previous_gp = get_financial_value(
    stock,
    "Gross Profit"
)
operating_income, previous_op = get_financial_value(
    stock,
    "Operating Income"
)

"""Calculation formulas"""
revenue_growth = calculate_growth(
    revenue.current,
    revenue.previous
)
gross_margin = calculate_margin(
    gross_profit.current,
    revenue.current
)
operating_margin = calculate_margin(
    operating_income.current,
    revenue.current
)

"""Actual Display"""
print_company_summary(
company_name,
        ticker,
        revenue,
        gross_profit,
        operating_income,
        revenue_growth,
        gross_margin,
        operating_margin
)