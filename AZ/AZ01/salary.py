import pandas as pd

df = pd.read_csv('dz.csv')
df.fillna({'Salary':0}, inplace=True)
df.fillna({'City':'Город не указан'}, inplace=True)
df.to_csv('dz.csv', index=False)

group = df.groupby('City')['Salary'].mean()

print(group)

