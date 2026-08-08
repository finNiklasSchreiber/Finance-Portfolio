import yfinance as yf

"""Collecting the Data that is needed for the program"""
from financial_data import load_financial_data
from display import print_company_summary

"""Stock Ticker Assignment"""
#Asks for input, assigns value and prints the name to check if you have the right company
ticker = input("Enter ticker to analyze: ").upper()
stock = yf.Ticker(ticker)
company_name = stock.info["longName"]

"""Financial Data"""
financials = load_financial_data(stock)

"""Actual Display"""
print_company_summary(stock,financials)