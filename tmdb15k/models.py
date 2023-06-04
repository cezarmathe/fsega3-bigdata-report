#
# tmdb15k/models.py
#

# This file defines various models that can be applied on the dataset.

import numpy as np
import pandas as pd

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from xgboost import XGBRegressor

"""
Prepare the data for model training and testing.

Returns: X_train, X_test, y_train, y_test
"""
def prepare_model_data(X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                       y: pd.DataFrame | pd.Series,
                       test_size: float = 0.2,
                       random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X_data: pd.DataFrame | pd.Series

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

"""A model that uses linear regression."""
class LinearRegressionModel:
    def __init__(self,
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series):
        X_train, X_test, y_train, y_test = prepare_model_data(X, y)

        self.lr = LinearRegression()
        self.lr.fit(X_train, y_train)
        y_pred = self.lr.predict(X_test)
        self.mse = mean_squared_error(y_test, y_pred)
        self.rmse = np.sqrt(self.mse)

"""A model that uses decision tree regression."""
class DecisionTreeRegressionModel:
    def __init__(self,
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series,
                 random_state: int = 42):
        X_train, X_test, y_train, y_test = prepare_model_data(X, y)

        self.dtr = DecisionTreeRegressor(random_state=random_state)
        self.dtr.fit(X_train, y_train)
        y_pred = self.dtr.predict(X_test)
        self.mse = mean_squared_error(y_test, y_pred)
        self.rmse = np.sqrt(self.mse)

"""A model that uses random forest regression."""
class RandomForestRegressionModel:
    def __init__(self,
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series,
                 n_estimators: int = 100,
                 random_state: int = 42):
        X_train, X_test, y_train, y_test = prepare_model_data(X, y)

        self.rfr = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
        self.rfr.fit(X_train, y_train)
        y_pred = self.rfr.predict(X_test)
        self.mse = mean_squared_error(y_test, y_pred)
        self.rmse = np.sqrt(self.mse)

"""A model that uses gradient boosting regression."""
class GradientBoostingRegressionModel:
    def __init__(self,
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series,
                 random_state: int = 42):
        X_train, X_test, y_train, y_test = prepare_model_data(X, y)

        self.gbr = GradientBoostingRegressor(random_state=random_state)
        self.gbr.fit(X_train, y_train)
        y_pred = self.gbr.predict(X_test)
        self.mse = mean_squared_error(y_test, y_pred)
        self.rmse = np.sqrt(self.mse)

"""A model that uses XGB regression."""
class XGBRegressionModel:
    def __init__(self,
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series,
                 random_state: int = 42):
        X_train, X_test, y_train, y_test = prepare_model_data(X, y)

        self.xgbr = XGBRegressor(random_state=random_state)
        self.xgbr.fit(X_train, y_train)
        y_pred = self.xgbr.predict(X_test)
        self.mse = mean_squared_error(y_test, y_pred)
        self.rmse = np.sqrt(self.mse)
