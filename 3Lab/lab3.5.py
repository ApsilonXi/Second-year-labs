import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) #добавили область и обратились к первой строке, первому столбцу, первой ячейке

x = np.linspace(-np.pi, np.pi, 100) #генератор последовательности (нач. точка, кон. точка, общее количество точек в последовательности)
y = np.linspace(-np.pi, np.pi, 100)

ax.set_title('График функции sin(xy)')
ax.set_xlabel('ось абцисс')
ax.set_ylabel('ось ординат')

z = np.sin(x*y)

ax.plot(z)

plt.show()