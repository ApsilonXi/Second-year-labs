from matplotlib.ticker import AutoMinorLocator
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

nyu = 7
o = 4

nyu2 = 6
o2 = 3

x = np.linspace(0, 10, 100)

f = 1/(o*np.sqrt(2*np.pi)) * np.e**(-(x-nyu)**2 / o**2)
f2 = 1/(o2*np.sqrt(2*np.pi)) * np.e**(-(x-nyu2)**2 / o2**2)

ax.set_title('График функции f(x)')
ax.set_xlabel('Ось абцисс')
ax.set_ylabel('Ось ординат')
ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
plt.plot(x, f, c='green', label = 'f(x)')
plt.plot(x, f2, c='red', label = 'f2(x)')

ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)


plt.show()
