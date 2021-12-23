import networkx as nx
import EoN
from collections import defaultdict
from matplotlib import animation


G = nx.grid_2d_graph(100, 100)
initial_GA = [(x, y) for (x, y) in G if 3 < x < 5 and 3 < y < 5]
initial_GA2 = [(x, y) for (x, y) in G if 33 < x < 35 and 80 < y < 82]
initial_GA3 = [(x, y) for (x, y) in G if 88 < x < 90 and 45 < y < 47]

H = nx.DiGraph()  # the spontaneous transitions
H.add_edge('GA', 'GR', rate=1)
H.add_edge('BA', 'BR', rate=1)
H.add_edge('BR', 'INACTIVE', rate=1)
H.add_edge('GR', 'INACTIVE', rate=1)
J = nx.DiGraph()
J.add_edge(('GA', 'BI'), ('GA', 'BA'), rate=4)
J.add_edge(('BA', 'BI'), ('BA', 'BA'), rate=4)

IC = defaultdict(lambda: 'BI')
for node in initial_GA:
    IC[node] = 'GA'
for i in initial_GA2:
    IC[i] = 'GA'
for i in initial_GA3:
    IC[i] = 'GA'

return_statuses = ['BI', 'BA', 'GI', 'GA','BR','GR','INACTIVE']
color_dict = {'GA': 'gold', 'BA': 'gold', 'GI': 'darkgoldenrod', 'BI': 'darkgoldenrod','GR':'saddlebrown','BR':'saddlebrown', 'INACTIVE':'darkgoldenrod'}
pos = {node: node for node in G}
tex = False
sim_kwargs = {'color_dict': color_dict, 'pos': pos, 'tex': tex}
sim = EoN.Gillespie_simple_contagion(G, H, J, IC, return_statuses, tmax=60,
                                     return_full_data=True, sim_kwargs=sim_kwargs)
times, D = sim.summary()

newD = {'Active':D['GA']+D['BA'], 'Inactive':D['GI']+D['BI']+D['INACTIVE'],'Relapse':D['GR']+D['BR']}
new_timeseries = (times,newD)
sim.add_timeseries(new_timeseries, label = 'Simulation', color_dict={'Active':'gold', 'Inactive':'darkgoldenrod', 'Relapse':'saddlebrown'})
ani = sim.animate(ts_plots=[['Active' , 'Inactive' , 'Relapse']], node_size=4)
FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
ani.save('BEE.gif', fps=5)



