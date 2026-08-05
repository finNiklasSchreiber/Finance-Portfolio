"""Calculating the numbers and formatting correctly"""
#Formatting billions to make the number look nicer and easier to read
def format_billions(value):
    return f"${value / 1_000_000_000:.2f} B"

def print_company_summary(
        company_name,
        ticker,
        revenue,
        gross_profit,
        operating_income,
        revenue_growth,
        gross_margin,
        operating_margin):
    """Displays Company name + Ticker + Fin Statement + Performance"""
    print("=" * 50)
    print(f"{'COMPANY SUMMARY':^50}")
    print("=" * 50)

    print(f"Company:            {company_name}")
    print(f"Ticker:             {ticker}")

    print("-" * 50)

    print(f"{'Financial Statement':^50}")
    print(f"{'Revenue:':20}{format_billions(revenue.current)}")
    print(f"{'Gross Profit:':20}{format_billions(gross_profit.current)}")
    print(f"{'Operating Income:':20}{format_billions(operating_income.current)}")
    # Displays the Performance Segment
    print("-" * 50)
    print(f"{'Performance':^50}")
    print("-" * 50)

    print(f"{'Revenue Growth:':20}{revenue_growth:.2f}%")
    print(f"{'Gross Margin:':20}{gross_margin:.2f}%")
    print(f"{'Operating Margin:':20}{operating_margin:.2f}%")
