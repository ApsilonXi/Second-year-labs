import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11, 1)

figure, ax = plt.subplots(2, 5)
plt.grid

result = []
for i in x:
  result.append(np.random.uniform(-1,1))

for i in range(2):
  for j in range(5):
    ax[i][j].plot(x, result)
 
plt.show()