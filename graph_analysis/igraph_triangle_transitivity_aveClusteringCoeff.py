import igraph
from igraph import *

import pandas as pd
import csv
import sys
maxInt = sys.maxsize
import datetime

print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
path2 = "D:/"
year = "2017_"

# year2017 edgelist file
multi = path2 + "contract_net_2017_fulltest.txt"

WCCtriangle_counting= path2+'2017_IGRAPH_WCC_trangles.csv'
WCCtransitivity= path2+'2017_IGRAPH_WCC_transivityNode.csv'
SCC_WCC_summary = path2+'2017_IGRAPH_WCC_trangles_summary.csv'

multi_edge_list = pd.read_csv(multi, header = None)
multiGraph = Graph.Read_Edgelist(multi_edge_list, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)

weakConnectedComponent = simpleGraph.components(mode=WEAK)
maxWeakConnectedComponent = weakConnectedComponent.giant()  # the giant graph
maxWeakConnectedComponent.to_undirected() 

WCCtran_localCoe = maxWeakConnectedComponent.transitivity_local_undirected(mode='zero')
WCCtran_nodedf=pd.DataFrame(WCCtran_localCoe)

WCC_subgraph_degree = maxWeakConnectedComponent.degree()

num_triangle=[]
for idx in range(len(WCCtran_localCoe)):
    numtriangle = round(0.5* WCCtran_localCoe[idx] * WCC_subgraph_degree[idx] *( WCC_subgraph_degree[idx]-1))
    num_triangle.append(numtriangle)
    
with open(WCCtriangle_counting, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['node_degree', 'node_triangle'])
    writer.writerows(zip(WCC_subgraph_degree, num_triangle))
    
WCCsum_triangle = sum(num_triangle)
print(f'sum of all triangles: {WCCsum_triangle}')

'''global culstering coefficient'''
WCCave_tran_node = maxWeakConnectedComponent.transitivity_avglocal_undirected(mode='zero') #average culstering, yes, but didnt count nan
print(f'global culstering coefficient: {WCCave_tran_node}')


'''global transivity'''
WCCglobal_transivity =maxWeakConnectedComponent.transitivity_undirected() # samve as networkx nx.transitivity result 
print(f' global transivity: {WCCglobal_transivity}')


''' ------------OUTPUT SUMMARY---------------'''
with open(SCC_WCC_summary, 'w') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow(["WCCave_tran_node","WCCglobal_transivity","SCCsum_triangle"]) 
    writer2.writerow([WCCave_tran_node,WCCglobal_transivity,WCCsum_triangle])

