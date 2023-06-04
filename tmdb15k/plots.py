#
# tmdb15k/plots.py
#

# Utilities for creating plots.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""Creates and displays a scatter plot."""
def scatter(x: pd.DataFrame | pd.Series, y: pd.DataFrame | pd.Series, title: str | None = None):
    plt.scatter(x, y)

    x_name: str
    if isinstance(x, pd.DataFrame):
        x_name = x.columns.join(',')
    else:
        x_name = str(x.name)

    y_name: str
    if isinstance(y, pd.DataFrame):
        y_name = y.columns.join(',')
    else:
        y_name = str(y.name)

    plt.xlabel(x_name)
    plt.ylabel(y_name)
    if title:
        plt.title(title)
    plt.show()

def box(measurement: pd.DataFrame | pd.Series,
        values: pd.DataFrame | pd.Series,
        title: str | None = None):
    df = pd.concat([measurement, values], axis=1)

    id_vars: list[str] = []
    value_columns: list[str] = []
    id_column: str

    if isinstance(measurement, pd.DataFrame):
        id_vars = measurement.columns.to_list()
        id_column = measurement.columns.join('-')
    else:
        id_vars = [str(measurement.name)]
        id_column = str(measurement.name)

    if isinstance(values, pd.DataFrame):
        value_columns = values.columns.to_list()
    else:
        value_columns = [str(values.name)]

    df_melted = df.melt(id_vars=id_vars,
                        value_vars=value_columns,
                        var_name="Values",
                        value_name='melted_value')

    df_melted = df_melted[df_melted['melted_value'] == 1]

    plt.figure(figsize=(10,6))
    sns.boxplot(data=df_melted, x='Values', y=id_column)
    plt.xticks(rotation=90)
    if title:
        plt.title(title)
    else:
        plt.title('Value by ' + id_column)
    plt.show()
