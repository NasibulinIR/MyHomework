import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv

file_path = 'cleanned_prices.csv'
data = read_csv(file_path)
prices = data['Цена']
mean_price = prices.mean()
print(mean_price)

plt.hist(data, bins=20)
plt.xlabel('Цена')
plt.ylabel('Кол-во в шт.')
plt.title('Гистограмма цен на диваны')
plt.show()