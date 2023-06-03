#
# tmdb15k/clean.py
#

import pandas as pd

"""
Clean the dataset.

This removes unused columns, removes rows with missing values and removes
duplicate rows.
"""
def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(axis='columns', columns=[
        'Unnamed: 0',
        'adult',
        'backdrop_path',
        'cast',
        'crew',
        'poster_path',
        'video',
    ])

    df = df.dropna()
    df = df.fillna('')
    df = df.drop_duplicates()

    return df

"""
Remove movies that are not in English.
"""
def remove_non_english(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['original_language'] == 'en']

    return df.drop(axis='columns', columns=['original_language'])

"""
Remove all columns except the given columns.
"""
def keep_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    to_delete = df.columns.difference(columns)
    return df.drop(axis='columns', columns=to_delete)
