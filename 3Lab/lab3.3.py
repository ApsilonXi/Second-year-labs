import matplotlib.pyplot as plt
import numpy as np

jobs = ["Сон", "Учёба", "Отдых", "Прогулка"]
count = [24, 45, 32, 12]

plt.bar(jobs, count)
plt.title("Распределение времени")
plt.xlabel("Дела")
plt.ylabel("Значения")

plt.show()
