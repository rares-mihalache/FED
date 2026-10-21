from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).parent.parent / "data" / "gdp_data.csv"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the GDP data from a semicolon-separated CSV file"""
    return pd.read_csv(path, sep=";")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Reshape the GDP data to long format and fix data types."""
    long_df = df.melt(
        id_vars=["Country Name", "Country Code"],
        var_name="Year",
        value_name="GDP",
    )
    long_df["Year"] = long_df["Year"].astype(int)
    long_df["GDP"] = pd.to_numeric(long_df["GDP"], errors="coerce")
    return long_df.dropna(subset=["GDP"])
