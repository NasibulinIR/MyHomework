import pandas as pd

df = pd.read_csv('1985-1992_Top_Chart.csv')

print(df.head(5))
print('-'*80)
print(df.info())
print('-'*80)
print(df.describe())



