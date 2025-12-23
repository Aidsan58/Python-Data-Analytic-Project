import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(df, column):
    plt.figure()
    plt.hist(df[column], bins = 20) # equal width intervals that group numeric data
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show() # render histogram

def plot_scatterplot(df, column_x, column_y):
    # Convert columns to numeric, force non-numeric values to NaN
    df[column_x] = pd.to_numeric(df[column_x], errors='coerce')
    df[column_y] = pd.to_numeric(df[column_y], errors='coerce')

    # Drop rows where either value is missing (non-numeric)
    df = df.dropna(subset=[column_x, column_y])

    # Plot
    plt.figure() # canvas for plot elements
    plt.scatter(df[column_x], df[column_y])
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(f"{column_y} vs {column_x}")
    plt.show() # render scatterplot