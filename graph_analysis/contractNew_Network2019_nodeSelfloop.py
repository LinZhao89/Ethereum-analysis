# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:31:26 2020
Count vertice and arcs
"""

import networkx as nx
import pandas as pd
import csv
import sys
import pandas as pd
maxInt = sys.maxsize
import datetime
print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
path1="D:/"

filename = "contract_net_2019_full"
print(filename)
multi =path1 + filename+ ".csv" 

nod = path1+"contract_net_address_hash_2019_full.csv"
degreeDistribution_output= path1 + filename + "_node_selfloop_multiDiG.csv"

multi_edge_list = pd.read_csv(multi, header = None)
node_list = pd.read_csv(nod, header = None)


multidiG = nx.MultiGraph()
simpleG = nx.Graph()
diG = nx.DiGraph()

# add mutlti-edge 
for i, elrow in multi_edge_list.iterrows():
    multidiG.add_edge(elrow[0], elrow[1])
    simpleG.add_edge(elrow[0], elrow[1])
    diG.add_edge(elrow[0], elrow[1])
    
    if (i % 100000 == 0):
        print(f' alive i is {i}')
        
#simpleGnoLoop = simpleG.remove_edges_from(nx.selfloop_edges(simpleG))         
print("finsh graph: ", datetime.datetime.now())

####-----------calculate degree/indegree/outdegree/------------------#######

print('-contract2019 net ---')
print('# of edges multi: {}'.format(multidiG.number_of_edges()))
print(' # of self loop multi: {}'.format(nx.number_of_selfloops(multidiG)))
print('# of edges, siG: {}'.format(simpleG.number_of_edges()))
print(' # of self loop siG: {}'.format(nx.number_of_selfloops(simpleG)))
print('# of edges, diG: {}'.format(diG.number_of_edges()))
print(' # of self loop diG: {}'.format(nx.number_of_selfloops(diG)))      
#print('# of nodes: {}'.format(g.number_of_nodes()))


with open(degreeDistribution_output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["# of edges multi", " # of self loop multi", "# of edges simple", " # of self loop simple", "# of edges diG", " # of self loop diG"])
    writer.writerow([multidiG.number_of_edges(),nx.number_of_selfloops(multidiG),simpleG.number_of_edges(),nx.number_of_selfloops(simpleG),diG.number_of_edges(),nx.number_of_selfloops(diG)])

print("end: ", datetime.datetime.now())
  
