"""
Collect degree, indegree and outdegree for each vertice in the network. 
"""
import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

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
filename = "token_net_2015"
multi =path1 + filename+ ".csv" 
nod = path1+"token_net_address_hash_2015.csv"

degreeDistribution_output= path1 + filename + "_degreeDistribution.csv"
in_out_degree_output = path1+filename+'_in_out_degree.csv'

multi_edge_list = pd.read_csv(multi, header = None)
node_list = pd.read_csv(nod, header = None)

multidiG = nx.MultiDiGraph()
#simpleG = nx.Graph()

# add mutlti-edge 
for i, elrow in multi_edge_list.iterrows():
    multidiG.add_edge(elrow[0], elrow[1])
    if (i % 10000 == 0):
        print(f' alive i is {i}')
        
   
####-----------calculate degree/indegree/outdegree/------------------#######
with open(degreeDistribution_output, 'w', newline='') as file, open(in_out_degree_output, 'w', newline='') as file1:
    writer = csv.writer(file)
    writer.writerow(["idx", "node", "multiDigraph", "Graph"])
    writer1 = csv.writer(file1)
    writer1.writerow(["idx", "node", "multidigraph_in", "multidigraph_out"])
    for i, nodrow  in node_list.iterrows():
        # number of degree
        x = multidiG.degree(nodrow[1])
        # number of in/out degrree
        gindegree = multidiG.in_degree(nodrow[1])
        goutdegree = multidiG.out_degree(nodrow[1])
        
        # write to csv
        writer.writerow([nodrow[1],nodrow[0], x ])
        writer1.writerow([nodrow[1],nodrow[0], gindegree , goutdegree])
