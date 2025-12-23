import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.figure()
    plt.hist(df[column], bins = 20) # equal width intervals that group numeric data
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show() # render histogram