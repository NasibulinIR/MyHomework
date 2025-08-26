import numpy as np
import matplotlib.pyplot as plt

# Стартовые параметры
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=10)
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.title('Гистограмма отображения случайных данных')
plt.show()