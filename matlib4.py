import matplotlib.pyplot as plt
import numpy as np
from random import randint


def crugdg(n):
  ch = []
  d = []
  for i in range(n):
    ch.append(str(i + 1) + ' часть')
    d.append(randint(1000, 10000))
  plt.pie(d, labels=ch, autopct='%1.1f%%')
  plt.title('Диаграмма из ' + str(n) + ' частей')
  plt.show()


crugdg(10)
