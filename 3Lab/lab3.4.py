import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 20)
y = np.linspace(1, 5, 20)

f = x**2 - 3*x*y +y**2 + x + 2*y + 5

ax = plt.subplot()
ax.set_title('График кривой')
ax.set_xlabel('Ось x')
ax.set_ylabel('Ось y')
ax.plot(f)

plt.grid()
plt.show()



