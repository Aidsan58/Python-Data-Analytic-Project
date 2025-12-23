import pandas as pd

pd.options.display.max_columns = 30

df = pd.read_csv('../data/data.csv')

print(df)
