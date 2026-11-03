from pathlib import Path

import pandas as pd


DATA_PATH: Path = Path(__file__).parent.parent / "data" / "gdp_data.csv"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the GDP data from a semicolon-separated CSV file.

    Parameters
    ----------
    path : Path, optional
        Location of the CSV file. Defaults to DATA_PATH.

    Returns
    -------
    pd.DataFrame
        Raw GDP data in wide format, with one column per year.
    """
    return pd.read_csv(path, sep=";")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Reshape the GDP data to long format and fix data types.

    Parameters
    ----------
    df : pd.DataFrame
        Raw GDP data in wide format, as returned by load_data.

    Returns
    -------
    pd.DataFrame
        Long-format data with columns ['Country Name', 'Country Code',
        'Year', 'GDP']. Rows with a missing GDP value are dropped.
    """
    long_df = df.melt(
        id_vars=["Country Name", "Country Code"],
        var_name="Year",
        value_name="GDP",
    )
    long_df["Year"] = long_df["Year"].astype(int)
    long_df["GDP"] = pd.to_numeric(long_df["GDP"], errors="coerce")
    return long_df.dropna(subset=["GDP"])
