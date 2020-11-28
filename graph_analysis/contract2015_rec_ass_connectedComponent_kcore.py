# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:31:26 2020

"""

import networkx as nx
import pandas as pd
import csv
import sys
print(nx.__version__)
maxInt = sys.maxsize
import datetime
print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
path1="D:"
filename = "contract_net2015"
multi =path1 + filename+ ".csv" 
nod = path1+"contract_net_address_hash2015.csv"

properties= path1+filename+'properties.csv'
core_number = path1+filename+'core_number_byNode.csv'
multi_edge_list = pd.read_csv(multi, header = None)
node_list = pd.read_csv(nod, header = None)

####should use multigraph(undirected) or multiDigraph (directed), cause each node may have multiple edges 
multidiG = nx.MultiDiGraph()
simpleG = nx.Graph()
diG = nx.DiGraph()

# add mutlti-edge 
for i, elrow in multi_edge_list.iterrows():
    # multidiG.add_edge(elrow[0], elrow[1])
    simpleG.add_edge(elrow[0], elrow[1])
    diG.add_edge(elrow[0], elrow[1])
    if (i % 50000 == 0):
        print(f' alive i is {i}')
   
print("finsh graph: ", datetime.datetime.now())

####-----------calculate degree/indegree/outdegree/------------------#######
  
reciprocity_overall = nx.algorithms.overall_reciprocity(diG)

# print(f'len of reciprocity_overall: {reciprocity_overall}')
assortativity_Digraph = nx.algorithms.assortativity.degree_assortativity_coefficient(simpleG) 
numStrongComponent = nx.algorithms.components.number_strongly_connected_components(diG)
#Generate nodes in strongly connected components of graph.
stronglyComponent = nx.algorithms.components.strongly_connected_components(diG)
# largest component
largestStrongComponent = max(stronglyComponent, key=len)

# print(f'len of largestStrongComponent: {len(largestStrongComponent)}')
numWeakComponent = nx.algorithms.components.number_weakly_connected_components(diG)
largestWeakomponent = max(nx.algorithms.components.weakly_connected_components(diG), key=len)
print(f'len of largestWeakomponent: {len(largestWeakomponent)}')

simpleG.remove_edges_from(nx.selfloop_edges(simpleG))  
mainCoreG = nx.algorithms.core.k_core(simpleG) 
coreNum = nx.algorithms.core.core_number(simpleG)
