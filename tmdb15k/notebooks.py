#
# tmdb15k/notebooks.py
#

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.tree import DecisionTreeRegressor

"""Apply min-max normalization to a column in a DataFrame."""
def normalize_min_max(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
    df[dst] = (df[src] - df[src].min()) / (df[src].max() - df[src].min())
    return df

"""Apply z-score standardization to a column in a DataFrame."""
def standardize_z_score(df: pd.DataFrame, src: str, dst: str) -> pd.DataFrame:
    df[dst] = (df[src] - df[src].mean()) / df[src].std()
    return df

class VoteAverage:
    def __init__(self, df: pd.DataFrame):
        self.df = df[['vote_average']]
        self.df.fillna(0, inplace=True)
        self.df = normalize_min_max(self.df, 'vote_average', 'vote_average_min_max')
        self.df = standardize_z_score(self.df, 'vote_average', 'vote_average_z_score')
        self.columns = ['vote_average', 'vote_average_min_max', 'vote_average_z_score']

class Popularity:
    def __init__(self, df: pd.DataFrame):
        self.df = df[['popularity']]
        self.df.fillna(0, inplace=True)
        self.df = normalize_min_max(self.df, 'popularity', 'popularity_min_max')
        self.df = standardize_z_score(self.df, 'popularity', 'popularity_z_score')
        self.columns = ['popularity', 'popularity_min_max', 'popularity_z_score']

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

"""
Prepare data for training and testing.
"""
def prepare_data(X: pd.DataFrame | list[pd.DataFrame], y: pd.Series, test_size: float = 0.2, random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X_data: pd.DataFrame

    if isinstance(X, list):
        X_data = pd.concat(X, axis=1)
    else:
        X_data = X

    X_data = X_data.fillna(0)
    y_train = y.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(X_data,
                                                        y_train,
                                                        test_size=test_size,
                                                        random_state=random_state)

    return X_train, X_test, y_train, y_test

class ComputedLinearRegression:
    def __init__(self, X: pd.DataFrame | list[pd.DataFrame], y: pd.Series):
        X_train, X_test, y_train, y_test = prepare_data(X, y)

        self.lr = LinearRegression()
        self.lr.fit(X_train, y_train)
        y_pred = self.lr.predict(X_test)
        self.mse = mean_squared_error(y_test, y_pred)
        self.rmse = np.sqrt(self.mse)
