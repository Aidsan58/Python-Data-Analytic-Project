import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 30

df = pd.read_csv('../data/data.csv')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for x in df.index:
    if is_number(df.loc[x, "Yield (mg/mL)"]) != True:
        df.drop(x, inplace = True)

for y in df.index:
    if is_number(df.loc[y, "kcat (1/min)"]) != True:
        df.drop(y, inplace = True)

df.plot(kind = 'scatter', x = 'Yield (mg/mL)', y = 'kcat (1/min)')

plt.show()
