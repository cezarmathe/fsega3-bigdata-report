
# tmdb15k/workflows.py
#

# Workflows for defining potential relationships and analyzing them.

import pandas as pd

from tmdb15k.models import (
    LinearRegressionModel,
    DecisionTreeRegressionModel,
    RandomForestRegressionModel,
    GradientBoostingRegressionModel,
    XGBRegressionModel,
)

def model_columns() -> list[str]:
    return ['L', 'DT', 'RF', 'GB', 'XGB']

class Analysis:
    def __init__(self,
                 parameter_names: list[str],
                 X: pd.DataFrame | list[pd.DataFrame | pd.Series] | pd.Series,
                 y: pd.DataFrame | pd.Series):
        self.parameter_names = parameter_names

        self.results = {
            'L': LinearRegressionModel(X, y),
            'DT': DecisionTreeRegressionModel(X, y),
            'RF': RandomForestRegressionModel(X, y),
            'GB': GradientBoostingRegressionModel(X, y),
            'XGB': XGBRegressionModel(X, y),
        }

    def summary(self) -> pd.DataFrame:
        parameter_tickboxes = [f'X' for _ in range(len(self.parameter_names))]
        parameter_columns = self.parameter_names

        model_results: list[float] = []
        model_names: list[str] = []

        for k in self.results:
            model_results.append(self.results[k].rmse)
            model_names.append(k)

        values = parameter_tickboxes + model_results
        columns = parameter_columns + model_names

        return pd.DataFrame(data=[values], columns=columns)
