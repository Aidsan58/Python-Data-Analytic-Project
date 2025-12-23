import numpy as np

def basic_stats(df, column):
    """Return basic stats for column"""
    return {
        "mean": np.mean(df[column]), # mean
        "median": np.median(df[column]), # median
        "std": np.std(df[column]), # standard deviation
    }