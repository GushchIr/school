import networkx as nx
import matplotlib.pyplot as plt
import sys

nodes = input()
graph = nx.Graph()
for i in nodes:
  graph.add_node(i)
ways = []
for i in sys.stdin:
  i = i.split()
  if len(i) > 0:
    ways.append(i)
for i in ways:
  graph.add_edge(i[0], i[1], weight=float(i[2]))
pos = nx.circular_layout(graph) 
nx.draw(graph, pos, with_labels=True, font_weight='bold') 
edge_weight = nx.get_edge_attributes(graph,'weight') 
nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_weight) 
plt.show()

# Пример ввода:
# ABCDE
# A B 1.6
# D C 2.7
# C A 4.1
# B C 3.7
# E A 2.2
# E F 6.8
