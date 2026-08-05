from models import FinancialMetric

#Gets financial statement from the stock that has been entered
def get_financial_value(stock, metric):

    values = stock.financials.loc[metric]

    current = values.iloc[0]

    previous = values.iloc[1]

    return FinancialMetric(current, previous)