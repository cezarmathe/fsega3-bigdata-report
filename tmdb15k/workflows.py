#
# tmdb15k/workflows.py
#

# Workflows for defining potential relationships and analyzing them.

import pandas as pd

from matplotlib import pyplot as plt

from tmdb15k.models import (
    LinearRegressionModel,
    DecisionTreeRegressionModel,
    RandomForestRegressionModel,
    GradientBoostingRegressionModel,
    XGBRegressionModel,
)

class Analysis:
    def __init__(self,
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series):
        self.lr = LinearRegressionModel(X, y)
        self.dtr = DecisionTreeRegressionModel(X, y)
        self.rfr = RandomForestRegressionModel(X, y)
        self.gbr = GradientBoostingRegressionModel(X, y)
        self.xgbr = XGBRegressionModel(X, y)

    def best(self) -> str:
        models = [
            ('Linear Regression', self.lr.rmse),
            ('Decision Tree Regression', self.dtr.rmse),
            ('Random Forest Regression', self.rfr.rmse),
            ('Gradient Boosting Regression', self.gbr.rmse),
            ('XGB Regression', self.xgbr.rmse)
        ]

        return min(models, key=lambda x: x[1])[0]

    def worst(self) -> str:
        models = [
            ('Linear Regression', self.lr.rmse),
            ('Decision Tree Regression', self.dtr.rmse),
            ('Random Forest Regression', self.rfr.rmse),
            ('Gradient Boosting Regression', self.gbr.rmse),
            ('XGB Regression', self.xgbr.rmse)
        ]

        return max(models, key=lambda x: x[1])[0]

    def summary(self) -> pd.DataFrame:
        models = [
            ('Linear Regression', self.lr.rmse),
            ('Decision Tree Regression', self.dtr.rmse),
            ('Random Forest Regression', self.rfr.rmse),
            ('Gradient Boosting Regression', self.gbr.rmse),
            ('XGB Regression', self.xgbr.rmse)
        ]

        return pd.DataFrame(models, columns=['Model', 'RMSE']).sort_values(by='RMSE', ascending=True)


class Relationship:
    def __init__(self,
                 name: str,
                 x: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series):
        self.name = name
        self.x = x
        self.y = y
        self.analysis: Analysis | None = None

    def analyze(self) -> Analysis:
        self.analysis = Analysis(self.x, self.y)
        return self.analysis

    def print_summary(self) -> None:
        analysis: Analysis = self.analysis if self.analysis is not None else self.analyze()
        print(f"===> Summary | {self.name}")
        print(analysis.summary())

    def print_plot(self) -> None:
        analysis: Analysis = self.analysis if self.analysis is not None else self.analyze()

        models = ['Linear Regression', 'Decision Tree', 'Random Forest', 'Gradient Boosting', 'XGBoost']
        mse_values = [
            analysis.lr.mse,
            analysis.dtr.mse,
            analysis.rfr.mse,
            analysis.gbr.mse,
            analysis.xgbr.mse
        ]
        plt.figure(figsize=(10, 5))
        plt.bar(models, mse_values)
        plt.xlabel('Regression Models')
        plt.ylabel('Mean Squared Error')
        plt.title(f"{self.name}: Comparison of Different Regression Models")
        plt.show()
