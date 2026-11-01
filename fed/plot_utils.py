from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_gdp_trends(
        df: pd.DataFrame, countries: list[str] | None = None) -> Figure:
    """Plot GDP growth trajectories over time for selected economies.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned GDP DataFrame in long format with columns
        ['Country Name', 'Year', 'GDP'].
    countries : list[str] | None, optional
        List of country names to plot.
        If None, plots all countries in the dataset.

    Returns
    -------
    Figure
        Matplotlib figure object containing the plot.
    """
    sns.set_theme(style="whitegrid")

    plot_df = df[df["Country Name"].isin(countries)] if countries else df

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

    # Render trajectory lines
    sns.lineplot(
        data=plot_df,
        x="Year",
        y="GDP",
        hue="Country Name",
        marker="o",
        linewidth=2,
        ax=ax,
    )

    ax.set_title(
        "GDP Trajectories Across Major Economies (2000–2022)",
        fontsize=13,
        pad=12,
        fontweight="bold",
    )
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("GDP (Billion USD)", fontsize=11)

    years = sorted(plot_df["Year"].unique())
    if years:
        ax.set_xticks(range(min(years), max(years) + 1, 2))

    ax.legend(
        title="Country",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        frameon=False,
    )

    plt.tight_layout()
    return fig
