from models import FinancialMetric
from models import FinancialData

FINANCIAL_STATEMENT_MAP = {
    "Free Cash Flow": "cashflow"
}


#Getting historical Data from the stock
def get_historical_data(stock,metric, period="annual"):
    statement_type = FINANCIAL_STATEMENT_MAP.get(metric, "financials")

    if period == "annual":

        if statement_type == "cashflow":
            financial_statement = stock.cashflow
        else:
            financial_statement = stock.financials

    elif period == "quarterly":

        if statement_type == "cashflow":
            financial_statement = stock.quarterly_cashflow
        else:
            financial_statement = stock.quarterly_financials

    else:
        raise ValueError("Period must be 'annual' or 'quarterly'")

    values = financial_statement.loc[metric].dropna()

    return values.sort_index()


#Gets financial Data from the stock
def load_financial_data(stock, period = "annual"):
    financials = FinancialData()

    financials.revenue = get_financial_value(
        stock,
        "Total Revenue",
        period = period
    )
    financials.gross_profit = get_financial_value(
        stock,
        "Gross Profit",
        period = period
    )
    financials.operating_income = get_financial_value(
        stock,
        "Operating Income",
        period = period
    )
    financials.net_income = get_financial_value(
        stock,
        "Net Income",
        period=period
    )
    financials.free_cash_flow = get_financial_value(
        stock,
        "Free Cash Flow",
        period=period
    )
    return financials

#Gets financial statement from the stock that has been entered
def get_financial_value(stock, metric, period="annual"):

    statement_type = FINANCIAL_STATEMENT_MAP.get(metric, "financials")

    if period == "annual":

        if statement_type == "cashflow":
            financial_statement = stock.cashflow
        else:
            financial_statement = stock.financials

    elif period == "quarterly":

        if statement_type == "cashflow":
            financial_statement = stock.quarterly_cashflow
        else:
            financial_statement = stock.quarterly_financials

    else:
        raise ValueError("Period must be 'annual' or 'quarterly'")

    values = financial_statement.loc[metric].dropna()

    current = values.iloc[0]
    previous = values.iloc[1]

    return FinancialMetric(current, previous)

def get_cashflow_value(stock, metric):
    values = stock.cashflow.loc[metric]

    current = values.iloc[0]

    previous = values.iloc[1]

    return FinancialMetric(current,previous)