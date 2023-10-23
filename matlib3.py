import matplotlib.pyplot as plt
import numpy as np


def stolbdiag(s, a, b, c, d, e, f, g):
  a = a.split()
  b = b.split()
  c = c.split()
  d = d.split()
  e = e.split()
  f = f.split()
  g = g.split()
  w = [a[0], b[0], c[0], d[0], e[0], f[0], g[0]]
  fz = [int(a[1]), int(b[1]), int(c[1]), int(d[1]), int(e[1]), int(f[1]), int(g[1])]
  plt.bar(w, fz)
  plt.title(s)
  s = s.split(' и ')
  plt.xlabel(s[0])
  plt.ylabel(s[1])
  plt.show()


stolbdiag('Факультет и количество поступивших', 'СМ1 100', 'СМ2 78', 'СМ3 90', 'СМ4 107', 'СМ5 89', 'СМ6 92', 'СМ7 103')
