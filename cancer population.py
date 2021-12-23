import networkx as nx
import EoN
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib import animation
import pandas as pd

G = nx.grid_2d_graph(100, 100)  # each node is (u,v) where 0<=u,v<=99 #we’ll initially infect those near the middle
initial_infections = [(u, v) for (u, v) in G if 50 < u < 55 and 50 < v < 55]
#initial_nano = [(x, y) for (x, y) in G if 47 < x < 49 and 47 < y < 49]
initial_blood1 = [(x, y) for (x, y) in G if 3 < x < 5 and 3 < y < 5]
initial_blood2 = [(x, y) for (x, y) in G if 33 < x < 35 and 80 < y < 82]
initial_blood3 = [(x, y) for (x, y) in G if 88 < x < 90 and 45 < y < 47]

H = nx.DiGraph()  # the spontaneous transitions
#H.add_edge('Nano', 'Heal', rate=0.3)
J = nx.DiGraph()  # the induced transitions
J.add_edge(('Cancer', 'Normal'), ('Cancer', 'Cancer'), rate=0.65)
#J.add_edge(('Nano', 'Cancer'), ('Nano', 'Nano'), rate=2)

IC = defaultdict(lambda: 'Normal')
for node in initial_infections:
    IC[node] = 'Cancer'
for i in initial_blood1:
    IC[i] = 'Blood'
for i in initial_blood2:
    IC[i] = 'Blood'
for i in initial_blood3:
    IC[i] = 'Blood'
#for i in initial_nano:
#    IC[i] = 'Nano'

return_statuses = ['Normal', 'Cancer', 'Heal', 'Nano','Blood']
color_dict = {'Normal': 'peachpuff', 'Cancer': 'black', 'Heal': 'aqua', 'Nano': 'slategrey','Blood':'red'}
pos = {node: node for node in G}
tex = False
sim_kwargs = {'color_dict': color_dict, 'pos': pos, 'tex': tex}
sim = EoN.Gillespie_simple_contagion(G, H, J, IC, return_statuses, tmax=60,
                                     return_full_data=True, sim_kwargs=sim_kwargs)
times, D = sim.summary()

new_timeseries = (times)
ani = sim.animate(ts_plots=[['Cancer']], node_size=4)
FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
ani.save('healgraph.gif', fps=5)



