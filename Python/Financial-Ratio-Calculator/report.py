import os

from calculations import (
    calculate_growth,
    calculate_margin
)

#Making table for a better structure for the report
def create_revenue_table(revenue, period):

    rows = ""

    for date, value in revenue.items():

        if period == "quarterly":
            label = f"Q{date.quarter} {date.year}"
        else:
            label = str(date.year)

        rows += f"""
        <tr>
            <td>{label}</td>
            <td class="numeric">${value / 1_000_000_000:.2f}B</td>
        </tr>
        """

    return rows

def create_growth_table(historical_growth, period):

    rows = ""

    for date, growth in historical_growth.items():

        if period == "quarterly":
            label = f"Q{date.quarter} {date.year}"
        else:
            label = str(date.year)

        rows += f"""
        <tr>
            <td>{label}</td>
            <td class="numeric">
                <span class="growth-{'positive' if growth > 0 else 'negative' if growth < 0 else ''}">
                    {growth:.2f}%
                </span>
            </td>
        </tr>
        """

    return rows

def calculate_report_metrics(financials):
    # Current values
    revenue_current = financials.revenue.current
    gross_profit_current = financials.gross_profit.current
    operating_income_current = financials.operating_income.current
    net_income_current = financials.net_income.current
    fcf_current = financials.free_cash_flow.current

    # Current growth
    revenue_growth = calculate_growth(
        financials.revenue.current,
        financials.revenue.previous
    )

    fcf_growth = calculate_growth(
        financials.free_cash_flow.current,
        financials.free_cash_flow.previous
    )

    # Current margins
    gross_margin = calculate_margin(
        financials.gross_profit.current,
        financials.revenue.current
    )

    operating_margin = calculate_margin(
        financials.operating_income.current,
        financials.revenue.current
    )

    net_margin = calculate_margin(
        financials.net_income.current,
        financials.revenue.current
    )

    fcf_margin = calculate_margin(
        financials.free_cash_flow.current,
        financials.revenue.current
    )

    return {
        "revenue_current": revenue_current,
        "gross_profit_current": gross_profit_current,
        "operating_income_current": operating_income_current,
        "net_income_current": net_income_current,
        "fcf_current": fcf_current,
        "revenue_growth": revenue_growth,
        "fcf_growth": fcf_growth,
        "gross_margin": gross_margin,
        "operating_margin": operating_margin,
        "net_margin": net_margin,
        "fcf_margin": fcf_margin
    }

#Actual HTML report Structure
def create_report_html(
    company_name,
    ticker,
    period,
    metrics,
    revenue_table,
    growth_table,
    chart_filename
):
    revenue_current = metrics["revenue_current"]
    gross_profit_current = metrics["gross_profit_current"]
    operating_income_current = metrics["operating_income_current"]
    net_income_current = metrics["net_income_current"]
    fcf_current = metrics["fcf_current"]

    revenue_growth = metrics["revenue_growth"]
    fcf_growth = metrics["fcf_growth"]

    gross_margin = metrics["gross_margin"]
    operating_margin = metrics["operating_margin"]
    net_margin = metrics["net_margin"]
    fcf_margin = metrics["fcf_margin"]

    # HTML
    report = f"""
    <!DOCTYPE html>

    <html>

    <head>
        <meta charset="UTF-8">
        <title>Indicator - {ticker}</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 30px;
            }}

            h1 {{
                margin-bottom: 5px;
                font-size: 32px;
                letter-spacing: 1px;
                color: #1f4e79;
            }}

            .report-subtitle{{
                color: #555;
                font-size: 18px;
                margin-top: 0;
                margin-bottom: 30px;
            }}

            .company-name{{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 5px;
            }}

            .report-meta{{
                color: #666;
                font-size: 14px;
                padding-bottom: 20px;
                border-bottom: 1px solid #ccc;
            }}

            h2 {{
                margin-top: 45px;
                margin-bottom: 18px;
                font-size: 22px;
                border-left: 4px solid #1f4e79;
                padding-left: 10px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
            }}

            th,
            td {{
                padding: 9px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}

            th {{
                font-weight: bold;
                text-align: left;
                border-bottom: 2px solid #333;
            }}

            .numeric {{
                text-align: right;
            }}

            .growth-positive {{
                color: #2e7d32;
            }}

            .growth-negative {{
                 color: #c62828;
            }}

        </style>
    </head>

    <body>

        <header class="report-header">

            <h1>INDICATOR</h1>

            <p class="report-subtitle">
            Financial Analysis Report
            </p>

            <div class="company-name">
            {company_name}
            </div>

            <div class="report-meta">
            {ticker} · {period.title()} Analysis
            </div>
        </header>


        <h2>Financial Overview</h2>

        <table>

            <tr>
                <th>Metric</th>
                <th class="numeric">Value</th>
            </tr>

            <tr>
                <td>Revenue</td>
                <td class="numeric">${revenue_current / 1_000_000_000:.2f}B</td>
            </tr>

            <tr>
                <td>Gross Profit</td>
                <td class="numeric">${gross_profit_current / 1_000_000_000:.2f}B</td>
            </tr>

            <tr>
                <td>Operating Income</td>
                <td class="numeric">${operating_income_current / 1_000_000_000:.2f}B</td>
            </tr>

            <tr>
                <td>Net Income</td>
                <td class="numeric">${net_income_current / 1_000_000_000:.2f}B</td>
            </tr>

            <tr>
                <td>Free Cash Flow</td>
                <td class="numeric">${fcf_current / 1_000_000_000:.2f}B</td>
            </tr>

        </table>


        <h2>Performance</h2>

        <table>

            <tr>
                <th>Metric</th>
                <th class="numeric">Value</th>
            </tr>

            <tr>
                <td>Revenue Growth</td>
                <td class="numeric">
                    <span class="growth-{'positive' if revenue_growth > 0 else 'negative' if revenue_growth < 0 else ''}">
                        {revenue_growth:.2f}%
                    </span>
                </td>
            </tr>

            <tr>
                <td>FCF Growth</td>
                <td class="numeric">
                    <span class="growth-{'positive' if fcf_growth > 0 else 'negative' if fcf_growth < 0 else ''}">
                        {fcf_growth:.2f}%
                    </span>
                </td>
            </tr>

            <tr>
                <td>Gross Margin</td>
                <td class="numeric">{gross_margin:.2f}%</td>
            </tr>

            <tr>
                <td>Operating Margin</td>
                <td class="numeric">{operating_margin:.2f}%</td>
            </tr>

            <tr>
                <td>Net Margin</td>
                <td class="numeric">{net_margin:.2f}%</td>
            </tr>

            <tr>
                <td>FCF Margin</td>
                <td class="numeric">{fcf_margin:.2f}%</td>
            </tr>

        </table>


        <h2>Historical Revenue</h2>

        <table>

            <tr>
                <th>Period</th>
                <th class="numeric">Revenue</th>
            </tr>

            {revenue_table}

        </table>


        <h2>Historical Revenue Growth</h2>

        <table>

            <tr>
                <th>Period</th>
                <th class="numeric">Revenue Growth</th>
            </tr>

            {growth_table}

        </table>


        <h2>Revenue Development</h2>

        <img
            src="{chart_filename}"
            alt="Revenue Development"
        >


    </body>

    </html>
    """

    return report


def create_report(
        company_name,
        ticker,
        period,
        financials,
        revenue,
        historical_growth,
        chart_path
):

    chart_filename = os.path.basename(chart_path)

    metrics = calculate_report_metrics(financials)

    revenue_table = create_revenue_table(
        revenue,
        period
    )

    growth_table = create_growth_table(
        historical_growth,
        period
    )

    report = create_report_html(
        company_name,
        ticker,
        period,
        metrics,
        revenue_table,
        growth_table,
        chart_filename
    )

    #Making sure folder exists
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(
        output_folder,
        f"{ticker}_{period}_report.html"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)