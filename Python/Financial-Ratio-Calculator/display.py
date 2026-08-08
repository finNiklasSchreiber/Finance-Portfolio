from calculations import (
    calculate_revenue_growth,
    calculate_gross_margin,
    calculate_operating_margin,
    calculate_net_margin
)

"""Formatting numbers correctly"""
#Formatting billions to make the number look nicer and easier to read
def format_billions(value):
    return f"${value / 1_000_000_000:.2f} B"

#Intake of Parameters
def print_company_summary(stock,financials):
    company_name = stock.info["longName"]
    ticker = stock.ticker

    revenue_growth = calculate_revenue_growth(financials)
    gross_margin = calculate_gross_margin(financials)
    operating_margin = calculate_operating_margin(financials)
    net_margin = calculate_net_margin(financials)

    """Displays Company name + Ticker + Fin Statement + Performance"""
    print("=" * 50)
    print(f"{'COMPANY SUMMARY':^50}")
    print("=" * 50)

    print(f"Company:            {company_name}")
    print(f"Ticker:             {ticker}")

    print("-" * 50)

    print(f"{'Financial Statement':^50}")
    print(f"{'Revenue:':20}{format_billions(financials.revenue.current)}")
    print(f"{'Gross Profit:':20}{format_billions(financials.gross_profit.current)}")
    print(f"{'Operating Income:':20}{format_billions(financials.operating_income.current)}")
    print(f"{'Net Income:':20}{format_billions(financials.net_income.current)}")
    # Displays the Performance Segment
    print("-" * 50)
    print(f"{'Performance':^50}")
    print("-" * 50)

    print(f"{'Revenue Growth:':20}{revenue_growth:.2f}%")
    print(f"{'Gross Margin:':20}{gross_margin:.2f}%")
    print(f"{'Operating Margin:':20}{operating_margin:.2f}%")
    print(f"{'Net Margin:':20}{net_margin:.2f}%")