#
# tmdb15k/filter.py
#

import pandas as pd

from abc import ABC, abstractmethod

"""A filter that can be applied to a DataFrame."""
class Filter(ABC):
    @abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

"""Apply one or more filters to a DataFrame."""
def apply(df: pd.DataFrame, filters: Filter | list[Filter]) -> pd.DataFrame:
    if isinstance(filters, list):
        for f in filters:
            df = f.apply(df)

        return df

    return filters.apply(df)

# class ColumnValues(Filter):
#     def __init__(self, column: str, values: any | list):
#         self.column = column
#         self.values = values

#     def apply(self, df: pd.DataFrame) -> pd.DataFrame:
#         if isinstance(self.values, list):
#             return df[df[self.column].isin(self.values)]

#         return df[df[self.column] == self.values]

class ColumnPredicate(Filter):
    def __init__(self, column: str, predicate: callable[[pd.DataFrame], bool]):
        self.column = column
        self.predicate = predicate

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[self.predicate(df[self.column])]

def values_less_than(column: str, value) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x < value)

def values_less_than_or_equal_to(column: str, value) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x <= value)

def values_greater_than(column: str, value) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x > value)

def values_greater_than_or_equal_to(column: str, value) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x >= value)

def values_equal_to(column: str, value) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x == value)

def values_not_equal_to(column: str, value) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x != value)

def values(column: str, values: list) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: x.isin(values))

def not_values(column: str, values: list) -> ColumnPredicate:
    return ColumnPredicate(column, lambda x: ~x.isin(values))
