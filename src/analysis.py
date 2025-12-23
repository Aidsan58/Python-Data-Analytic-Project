import numpy as np
import pandas as pd

def basic_stats(df, column):
    """Return basic stats for column"""
    return {
        "mean": np.mean(df[column]), # mean
        "median": np.median(df[column]), # median
        "std": np.std(df[column]), # standard deviation
    }

def correlation(df, column_1, column_2):
    corr_value = df[column_1].corr(df[column_2])
    print(f"Correlation between {column_1} and {column_2} is {corr_value}.")
    return corr_value