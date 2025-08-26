import numpy as np
import matplotlib.pyplot as plt

first_array = np.random.rand(5)  # координата х
second_array = np.random.rand(5) # координата y

plt.scatter(first_array, second_array)
plt.ylabel('Ось У')
plt.xlabel('Ось Х')
plt.show()
