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
    column_x = pd.to_numeric(column_x, errors='coerce')
    column_y = pd.to_numeric(column_y, errors='coerce')

    # Drop rows where either value is missing (non-numeric)
    df = df.dropna(subset=[column_x, column_y])

    # Plot
    df.plot(kind='scatter', x=column_x, y=column_y)
    plt.show()