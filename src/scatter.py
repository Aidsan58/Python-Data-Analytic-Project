import 

pd.options.display.max_columns = 30

df = pd.read_csv('../data/data.csv')

# Convert columns to numeric, force non-numeric values to NaN
df['Yield (mg/mL)'] = pd.to_numeric(df['Yield (mg/mL)'], errors='coerce')
df['kcat (1/min)'] = pd.to_numeric(df['kcat (1/min)'], errors='coerce')

# Drop rows where either value is missing (non-numeric)
df = df.dropna(subset=['Yield (mg/mL)', 'kcat (1/min)'])

# Plot
df.plot(kind='scatter', y='Yield (mg/mL)', x='kcat (1/min)')
plt.show()

print(df[['Yield (mg/mL)']].corrwith(df['kcat (1/min)']))
