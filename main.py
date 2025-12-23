from src.data_loader import load_csv
from src.data_cleaning import clean_data
from src.analysis import basic_stats
from visualization import plot_histogram

DATA_PATH = "data/data.csv" # change this line if your data is located elsewhere

def main():
    df = load_csv(DATA_PATH)
    df = clean_data(df)

    stats = basic_stats(df, df.columns[0])
    print("Basic statistics: ", stats)

    plot_histogram(df, df.columns[0])

if __name__ == "__main__":
    main()