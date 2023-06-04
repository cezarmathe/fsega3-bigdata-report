#
# tmdb15k/ops.py
#

# This file contains various operations that can be performed on the TMDB15K
# dataset.

import numpy as np
import pandas as pd

"""Apply min-max normalization to a column in a DataFrame."""
def normalize_min_max(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
    df[dst] = (df[src] - df[src].min()) / (df[src].max() - df[src].min())
    return df

"""Apply z-score standardization to a column in a DataFrame."""
def standardize_z_score(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
    df[dst] = (df[src] - df[src].mean()) / df[src].std()
    return df

"""Apply log10 transformation to a column in a DataFrame."""
def log10(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
    df[dst] = np.log10(df[src] + 1)
    return df
