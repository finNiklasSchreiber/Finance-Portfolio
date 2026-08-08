#Calculation formula for margins
def calculate_margin(numerator, denominator):
    return (numerator / denominator) * 100
#Calculation formula for growth
def calculate_growth(current, previous):

    return ((current - previous) / previous) * 100
#Calcs for Revenue growth/Gross margin/OP Margin
def calculate_revenue_growth(financials):

    return calculate_growth(
        financials.revenue.current,
        financials.revenue.previous
    )
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