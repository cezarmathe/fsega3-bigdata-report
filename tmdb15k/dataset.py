#
# tmdb15k/dataset.py
#

import pandas as pd

from abc import ABC, abstractmethod
from typing import Callable

DATASET_PATH = 'datasets/tmdb-15000-movies.csv'

"""Load the dataset."""
def load() -> pd.DataFrame:
    return pd.read_csv(DATASET_PATH, lineterminator='\n')

"""
ColumnProcessor is an abstract class that defines a method that takes in a
DataFrame, a source column name, and a destination column name. The method
should add a new column to the DataFrame with the destination column name that
contains the processed values of the source column.
"""
class ColumnProcessor(ABC):
    @abstractmethod
    def apply(self, df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
        pass

def process_column(df: pd.DataFrame, src: str, dst: str, processors: ColumnProcessor | list[ColumnProcessor]) -> pd.DataFrame:
    if isinstance(processors, ColumnProcessor):
        return processors.apply(df, src, dst)

    i = 0

    for processor in processors:
        actual_dst = dst if i == 0 else f"{dst}_{i}"
        df = processor.apply(df, src, actual_dst)
        i += 1

    return df

"""
FunctionalColumnProcessor is a class that applies a function to a DataFrame.
"""
class FunctionalColumnProcessor(ColumnProcessor):
    def __init__(self, process_function: Callable[[pd.DataFrame, str, str], pd.DataFrame]):
        self.process_function = process_function

    def apply(self, df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
        return self.process_function(df, src, dst)

"""
Create a FunctionalColumnProcessor that applies a min-max normalization to a
DataFrame.
"""
def normalize_min_max() -> FunctionalColumnProcessor:
    return FunctionalColumnProcessor(DataStandardization.normalize_min_max)

def standardize_z_score() -> FunctionalColumnProcessor:
    return FunctionalColumnProcessor(DataStandardization.standardize_z_score)

"""
"""
class DataStandardization:
    @staticmethod
    def normalize_min_max(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
        df[dst] = (df[src] - df[src].min()) / (df[src].max() - df[src].min())

        return df

    @staticmethod
    def standardize_z_score(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
        df[dst] = (df[src] - df[src].mean()) / df[src].std()

        return df
