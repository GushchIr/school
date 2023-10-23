import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin


def manygr():
  x = [i/10 for i in range(-50, 50, 1)]
  y1 = [cos(i) for i in x]
  y2 = [sin(i) for i in x]
  x2 = [i / 10 for i in range(1, 100, 1)]
  y3 = [i**2 for i in x2]
  y4 = [2/i for i in x2]
  plt.subplot(3, 2, 1)
  plt.plot(x, y1)
  plt.grid()
  plt.title('y = cos(x)')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.subplot(3, 2, 2)
  plt.plot(x, y2)
  plt.grid()
  plt.title('y = sin(x)')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.subplot(3, 2, 5)
  plt.plot(x2, y3)
  plt.grid()
  plt.title('y = x**2')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.subplot(3, 2, 6)
  plt.plot(x2, y4)
  plt.grid()
  plt.title('y = 2/x')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()


manygr()
