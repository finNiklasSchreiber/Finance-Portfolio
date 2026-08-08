from models import FinancialMetric
from models import FinancialData

#Gets financial Data from the stock
def load_financial_data(stock):
    financials = FinancialData()

    financials.revenue = get_financial_value(
        stock,
        "Total Revenue"
    )
    financials.gross_profit = get_financial_value(
        stock,
        "Gross Profit"
    )
    financials.operating_income = get_financial_value(
        stock,
        "Operating Income"
    )
    financials.net_income = get_financial_value(
        stock,
        "Net Income"
    )
    return financials

#Gets financial statement from the stock that has been entered
def get_financial_value(stock, metric):

    values = stock.financials.loc[metric]

    current = values.iloc[0]

    previous = values.iloc[1]

    return FinancialMetric(current, previous)