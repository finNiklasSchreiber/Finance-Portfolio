import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def plot_revenue(revenue, period="annual", save_path=None):

    if period == "annual":
        labels = revenue.index.year.astype(str)

    elif period == "quarterly":
        labels = (
            "Q"
            + revenue.index.quarter.astype(str)
            + " "
            + revenue.index.year.astype(str)
        )

    else:
        raise ValueError("Period must be 'annual' or 'quarterly'")

    values = revenue.values

    # Creating the chart
    plt.figure(figsize = (10, 5))

    plt.plot(
        labels,
        values,
        marker="o",
        linewidth=2
    )

    # Grid
    plt.grid(
        True,
        alpha=0.2,
        linestyle="--"
    )

    """Titles and labels
    plt.title(
        "Revenue Development",
        fontsize=16,
        fontweight="bold",
        pad=15
    )"""

    # Determine which x-axis labels should be displayed
    number_of_points = len(labels)

    if number_of_points <= 10:
        tick_positions = range(number_of_points)
    else:
        number_of_labels = 8
        step = (number_of_points - 1) // (number_of_labels - 1)

        tick_positions = list(range(0, number_of_points, step))

        if tick_positions[-1] != number_of_points - 1:
            tick_positions.append(number_of_points - 1)

    tick_labels = [labels[i] for i in tick_positions]

    plt.xticks(
        tick_positions,
        tick_labels
    )

    plt.xlabel(
        "Period",
        fontsize=11
    )

    plt.ylabel(
        "Revenue",
        fontsize=11
    )

    # Formatting revenue values
    formatter = FuncFormatter(
        lambda x, pos: f"${x / 1_000_000_000:.0f}B"
    )

    plt.gca().yaxis.set_major_formatter(formatter)

    # Improve spacing
    plt.tight_layout()

    # Save chart if a path was provided
    if save_path:
        plt.savefig(
            save_path,
            bbox_inches="tight"
        )

    # plt.show()