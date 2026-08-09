import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def plot_revenue(revenue, period = "annual"):

    if period == "annual":
        labels = revenue.index.year.astype(str)[::-1]

    elif period == "quarterly":
        labels = (
                "Q"
                + revenue.index.quarter.astype(str)
                + " "
                + revenue.index.year.astype(str)
        )[::-1]

    else:
        raise ValueError("Period must be 'annual' or 'quarterly'")
    values = revenue.values[::-1]

    plt.plot(labels, values, marker ="o")
    plt.grid(True, alpha=0.3)

    plt.title("Revenue Development")
    plt.xlabel("Year")
    plt.ylabel("Revenue")

    #Running the numbers so they are easy to read on the chart
    formatter = FuncFormatter(
        lambda x, pos: f"${x / 1_000_000_000:.0f}B"
    )
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.show()
