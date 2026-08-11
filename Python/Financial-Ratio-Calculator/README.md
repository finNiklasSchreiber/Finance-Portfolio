# Indicator
**Financial Ratio Calculator**


A modular Python-based financial analysis tool for equity research.

## Current Features

### Financial Analysis
- Financial Statement Analysis
- Free Cash Flow
- Revenue Growth
- FCF Growth
- Gross Margin
- Operating Margin
- Net Margin
- FCF Margin

### Data & Visualization
- Historical revenue visualization
- Historical financial data handling
- Annual and quarterly data analysis
- Ticker validation

### Reporting
- HTML financial analysis reports
- PDF financial analysis reports
- Financial overview and performance sections
- Historical revenue and revenue growth tables
- Integrated revenue development charts
- Positive and negative growth highlighting
- Annual and quarterly period labeling

### Technologies
- Python
- Pandas
- yfinance
- Matplotlib
- WeasyPrint

## Setup
Indicator is currently set up for Windows.

### Requirements
- Python 3.13 or later
- Git

### Installation
1. Clone the repository
2. Navigate to `Python/Financial-Ratio-Calculator` in PowerShell
3. Create a virtual environment:

   `python -m venv .venv`
4. Activate the virtual environment:

   `.\.venv\Scripts\Activate.ps1`
5. Install the required Python packages:

   `pip install -r requirements.txt`
6. Run Indicator:

   `python main.py`

### PDF Generation

Indicator uses a bundled WeasyPrint executable for PDF generation.

The executable is located at:

`tools/weasyprint.exe`

No separate WeasyPrint Python package or native PDF library installation is required.


## Added in Last Update — v0.6

- Added reproducible Windows setup
- Added bundled WeasyPrint executable for PDF generation
- Removed the Python WeasyPrint dependency
- Added automatic creation of the output folder
- Improved portability across Windows systems


### Project Status
Learning project - actively developed.

### Roadmap
- Generic financial metric charting
- Historical profitability charts
- Cash flow visualization
- Improved financial data sources
- More advanced financial ratios
- Cross-platform support