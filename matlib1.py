import matplotlib.pyplot as plt
import numpy as np


def per_gr(f1, f2):
  x = np.linspace(-20, 20, 100)
  fx1 = f1[5:]
  fx2 = f2[5:]
  y1 = eval(fx1)
  y2 = eval(fx2)
  plt.plot(x, y1, label='y1')
  plt.plot(x, y2, label='y2')
  plt.title('Пересечение графиков ' + f1 + ' и ' + f2)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid()
  plt.legend()
  plt.show()

  
per_gr('y1 = 2 * x - 6', 'y2 = -x + 4')
