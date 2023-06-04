#
# tmdb15k/datapoints.py
#

# This file contains class definitions for various data points that can be found
# in the TMDB15K dataset.

import pandas as pd

from sklearn.preprocessing import MultiLabelBinarizer

import tmdb15k.ops as ops

class VoteAverage:
    def __init__(self, df: pd.DataFrame):
        self.df = df[['vote_average']]
        self.df.fillna(0, inplace=True)
        self.df = ops.normalize_min_max(self.df, 'vote_average', 'vote_average_min_max')
        self.df = ops.standardize_z_score(self.df, 'vote_average', 'vote_average_z_score')
        self.columns = ['vote_average', 'vote_average_min_max', 'vote_average_z_score']
        self.df_min_max = self.df['vote_average_min_max']
        self.df_z_score = self.df['vote_average_z_score']

class Popularity:
    def __init__(self, df: pd.DataFrame):
        self.df = df[['popularity']]
        self.df.fillna(0, inplace=True)
        self.df = ops.normalize_min_max(self.df, 'popularity', 'popularity_min_max')
        self.df = ops.standardize_z_score(self.df, 'popularity', 'popularity_z_score')
        self.columns = ['popularity', 'popularity_min_max', 'popularity_z_score']
        self.df_min_max = self.df['popularity_min_max']
        self.df_z_score = self.df['popularity_z_score']

class VoteCount:
    def __init__(self, df: pd.DataFrame):
        self.df = df[['vote_count']]
        self.df.fillna(0, inplace=True)
        self.df = ops.log10(self.df, 'vote_count', 'vote_count_log10')
        self.df = ops.normalize_min_max(self.df, 'vote_count_log10', 'vote_count_log10_min_max')
        self.df = ops.standardize_z_score(self.df, 'vote_count_log10', 'vote_count_log10_z_score')
        self.columns = ['vote_count', 'vote_count_log10', 'vote_count_log10_min_max', 'vote_count_log10_z_score']
        self.df_log10 = self.df['vote_count_log10']
        self.df_log10_min_max = self.df['vote_count_log10_min_max']
        self.df_log10_z_score = self.df['vote_count_log10_z_score']

class Genres:
    def __init__(self, df: pd.DataFrame):
        df['genres_filled'] = df['genres'].fillna('[]')
        df['genres_list'] = df['genres_filled'].apply(lambda x: eval(x))
        df['genre_names'] = df['genres_list'].apply(lambda x: [i['name'].lower().replace(' ', '_') for i in x])
        mlb = MultiLabelBinarizer()
        genres_encoded = mlb.fit_transform(df['genre_names'])
        genre_names = mlb.classes_

        self.columns: list[str] = ["genre_" + i for i in genre_names]
        self.df = pd.DataFrame(genres_encoded, columns=self.columns, index=df.index)

        df.drop(columns=['genres_filled', 'genres_list', 'genre_names'], inplace=True)

class Keywords:
    def __init__(self, df: pd.DataFrame):
        df['keywords_filled'] = df['keywords'].fillna('[]')
        df['keywords_list'] = df['keywords_filled'].apply(lambda x: eval(x))
        df['keyword_names'] = df['keywords_list'].apply(lambda x: [i.lower().replace(' ', '_').replace(',', '') for i in x])
        mlb = MultiLabelBinarizer()
        keywords_encoded = mlb.fit_transform(df['keyword_names'])
        keyword_names = mlb.classes_

        self.columns: list[str] = ["keyword_" + i for i in keyword_names]
        self.df = pd.DataFrame(keywords_encoded, columns=self.columns, index=df.index)

        df.drop(columns=['keywords_filled', 'keywords_list', 'keyword_names'], inplace=True)

        keyword_occurrences = self.df.sum().sort_values(ascending=False)
        self.columns_top_20 = keyword_occurrences.head(20).index.tolist()

class ReleaseDate:
    def __init__(self, df: pd.DataFrame):
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        df['release_year'] = df['release_date'].dt.year
        df['release_month'] = df['release_date'].dt.month
        df['release_day'] = df['release_date'].dt.day

        self.df: pd.DataFrame = df[['release_date', 'release_year', 'release_month', 'release_day']]
        self.columns: list[str] = ['release_date', 'release_year', 'release_month', 'release_day']
        self.series_datetime: pd.Series = self.df['release_date']
        self.series_year: pd.Series = self.df['release_year']
        self.series_month: pd.Series = self.df['release_month']
        self.series_day: pd.Series = self.df['release_day']
