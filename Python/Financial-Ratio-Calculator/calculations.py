#Calculation formula for margins
def calculate_margin(numerator, denominator):
    return (numerator / denominator) * 100
#Calculation formula for growth
def calculate_growth(current, previous):

    return ((current - previous) / previous) * 100
#Growth Calculations
def calculate_revenue_growth(financials):

    return calculate_growth(
        financials.revenue.current,
        financials.revenue.previous
    )
def calculate_fcf_growth(financials):

    return calculate_growth(
        financials.free_cash_flow.current,
        financials.free_cash_flow.previous
    )

#Margin Calculations
def calculate_gross_margin(financials):

    return calculate_margin(
        financials.gross_profit.current,
        financials.revenue.current
    )
def calculate_operating_margin(financials):

    return calculate_margin(
        financials.operating_income.current,
        financials.revenue.current
    )
def calculate_net_margin(financials):

    return calculate_margin(
        financials.net_income.current,
        financials.revenue.current
    )
def calculate_fcf_margin(financials):

    return calculate_margin(
        financials.free_cash_flow.current,
        financials.revenue.current
    )
