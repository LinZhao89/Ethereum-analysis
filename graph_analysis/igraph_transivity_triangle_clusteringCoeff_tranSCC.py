
import igraph
from igraph import *

import pandas as pd
import csv
import sys
maxInt = sys.maxsize
import datetime


def triangles(g):
    cliques = g.cliques(min=3, max=3)
    result = [0] * g.vcount()
    for i, j, k in cliques:
        result[i] += 1
        result[j] += 1
        result[k] += 1
    return result


print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
path1="D:/"

filename = "contract_net_2016_fulltest.txt"
print(filename)

SCCtriangle_counting= path1+filename+'_IGRAPH_SCC_trangles.csv'
#WCCtransitivity= path1+filename+'_IGRAPH_WCC_transivityNode.csv'
SCCtransitivity= path1+filename+'_IGRAPH_SCC_transivityNode.csv'
SCC_WCC_summary = path1+filename+'_IGRAPH_SCC_trangles_summary.csv'


multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
#vs = VertexSeq(simpleGraph)
#for ver in simpleGraph.vs:
#    ver["value"]=node_list[0][ver.index]
#    print(ver)
    
#    
'''STRONGLY  cc'''
STRONGConnectedComponent = simpleGraph.components(mode=STRONG)
maxSTRONGConnectedComponent = STRONGConnectedComponent.giant()  #dd is the giant graph
maxSTRONGConnectedComponent.to_undirected()   

'''local clustering coefficient'''
SCCtran_localCoe = maxSTRONGConnectedComponent.transitivity_local_undirected(mode='zero')
#SCCtran_nodedf=pd.DataFrame(SCCtran_localCoe)

SCC_subgraph_degree = maxSTRONGConnectedComponent.degree()
#for ver1 in maxWeakConnectedComponent.vs:
#    print(ver1)
#    print(f' degree{ ver1.degree()}')

num_triangle=[]
for idx in range(len(SCCtran_localCoe)):
    numtriangle = round(0.5* SCCtran_localCoe[idx] * SCC_subgraph_degree[idx] *( SCC_subgraph_degree[idx]-1))
    num_triangle.append(numtriangle)
#WCCtran_nodedf = WCCtran_nodedf.fillna(0)
#WCCave_tran_node = sum(WCCtran_nodedf[0])/len(WCCtran_nodedf[0])
#print(f'--WCCave_tran_node_nonan: {WCCave_tran_node}')
with open(SCCtriangle_counting, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['node_degree', 'node_triangle'])
    writer.writerows(zip(SCC_subgraph_degree, num_triangle))
    
SCCsum_triangle = sum(num_triangle)
print(f'sum of all triangles: {SCCsum_triangle}')

'''global culstering coefficient'''
SCCave_tran_node = maxSTRONGConnectedComponent.transitivity_avglocal_undirected(mode='zero') #average culstering, yes, but didnt count nan
print(f'global culstering coefficient: {SCCave_tran_node}')
#with open(WCCtransitivity, 'w') as f:
#    f.write(WCCtran_nodedf.to_string(header = False, index = False))  

'''global transivity'''
SCCglobal_transivity = maxSTRONGConnectedComponent.transitivity_undirected() # samve as networkx nx.transitivity result 
print(f' global transivity: {SCCglobal_transivity}')

''' ------------OUTPUT SUMMARY---------------'''
with open(SCC_WCC_summary, 'w') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow(["SCCave_tran_node","SCCglobal_transivity","SCCsum_triangle"]) 
    writer2.writerow([SCCave_tran_node,SCCglobal_transivity,SCCsum_triangle])

print("start: ", datetime.datetime.now())
node=maxStrongConnectedComponent.vcount()
