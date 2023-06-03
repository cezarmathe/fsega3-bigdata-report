#
# tmdb15k/q1.py
#

import matplotlib.pyplot as plt
import pandas as pd

import tmdb15k.dataset as dataset
import tmdb15k.util as util

# Question 1: Average Vote Popularity Relationship
#
# What is the relationship between a movie's popularity and its average vote?
# Do more popular movies receive higher average votes?
class AverageVotePopularityRelationship:
    columns = [
        'popularity',
        'vote_average',
    ]

    def __init__(self,
                 df: pd.DataFrame,
                 average_vote_processors: list[dataset.ColumnProcessor],
                 popularity_processors: list[dataset.ColumnProcessor]):
        self.df = df
        self.average_vote_processors = average_vote_processors
        self.popularity_processors = popularity_processors

    def compute(self):
        self.df = util.clean(self.df)
        self.df = util.remove_non_english(self.df)
        self.df = util.keep_columns(self.df, self.columns)

        self.df = dataset.process_column(
            self.df,
            'vote_average',
            'vote_average_processed',
            self.average_vote_processors)

        self.df = dataset.process_column(
            self.df,
            'popularity',
            'popularity_processed',
            self.popularity_processors)

        self.correlation_coefficient = self.df['vote_average_processed'].corr(self.df['popularity_processed'])

        plt.scatter(self.df['popularity_processed'], self.df['vote_average_processed'])
        plt.xlabel('Popularity (Standardized)')
        plt.ylabel('Vote Average (Normalized)')
        plt.title('Scatter plot of Popularity vs Vote Average')
