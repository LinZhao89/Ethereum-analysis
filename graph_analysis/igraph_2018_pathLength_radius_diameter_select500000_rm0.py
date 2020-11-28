# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:51:03 2020
path length and diameter of random nodes
"""

import random
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
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/2015/"
path1="/home/LBS_ZHAOLIN/graph_analysis/block_chain/transaction/2016/"
print(path1)
#path1 = 'C:/Users/linzhao2/Downloads/blockchain_data/'
#path1 = 'C:/Users/superLin/Documents/blockchain/'
filename = "transaction_net_2016test.txt" 
nod = path1+"transaction_net_address_hash_2016.csv"

pathlengthWCC = path1+filename+'_IGRAPH_WCC_lenth_radius_diameter_sample_remove0.csv'
pathlengthSCC = path1+filename+'_IGRAPH_SCC_lenth_radius_diameter_sample_remove0.csv'
#chain4_number = path1+filename+'_IGRAPH_SCCmaincore_4nodeChainNum.csv'

node_list = pd.read_csv(nod, header = None)
###multi_edge_list = pd.read_csv(multi, header = None)
multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
vs = VertexSeq(simpleGraph)
for ver in simpleGraph.vs:
    ver["value"]=node_list[0][ver.index]
#    print(ver)
    
'''WEAK cc'''
weakConnectedComponent = simpleGraph.components(mode=WEAK)
#leng_weakCC= len(weakConnectedComponent)
maxweakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
print(maxweakConnectedComponent.vcount())
maxweakConnectedComponent.to_undirected()

####select randomly 100,000 points for calculation 

index = []
for  idx, ver1 in enumerate(maxweakConnectedComponent.vs):
#    print(ver1)
    index.append(idx)
    
selectNode = random.sample(index, k=500000)
WCC_sub_100000 = maxweakConnectedComponent.induced_subgraph(selectNode, implementation = "copy_and_delete")

#        writer3.writerow([vCentrality[idx],ver1["value"]])
eccen = WCC_sub_100000.eccentricity()
eccen1 = [i for i in eccen if i != 0]

diameter = max(eccen1)
radius = min(eccen1)
ave_path_length = WCC_sub_100000.average_path_length(directed = False)

#diameter = maxweakConnectedComponent.diameter(directed = False)
#radius = maxweakConnectedComponent.radius(mode = ALL)
#ave_path_length = maxweakConnectedComponent.average_path_length(directed = False)
print("wcc: ", datetime.datetime.now())
with open(pathlengthWCC, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["diameter", "radius", "ave_path_length"])
    writer.writerow([diameter, radius, ave_path_length])
print("wcc: ", datetime.datetime.now())    

'''strong cc'''
STRONGConnectedComponent = simpleGraph.components(mode=STRONG)
#leng_STRONGCC= len(STRONGConnectedComponent)
maxSTRONGConnectedComponent = STRONGConnectedComponent.giant()  #dd is the giant graph
maxSTRONGConnectedComponent.to_undirected()

index = []
for  idx, ver1 in enumerate(maxSTRONGConnectedComponent.vs):
    index.append(idx)
    
selectNode = random.sample(index, k=500000)
SCC_sub_100000 = maxSTRONGConnectedComponent.induced_subgraph(selectNode, implementation = "copy_and_delete")

eccen = SCC_sub_100000.eccentricity()
eccen1 = [i for i in eccen if i != 0]

diameter = max(eccen1)
radius = min(eccen1)
ave_path_length = SCC_sub_100000.average_path_length(directed = False)

#diameter = maxSTRONGConnectedComponent.diameter(directed = False)
#radius = maxSTRONGConnectedComponent.radius(mode = ALL)
#ave_path_length = maxSTRONGConnectedComponent.average_path_length(directed = False)
print("scc: ", datetime.datetime.now())
with open(pathlengthSCC, 'w', newline='') as file1:
    writer1 = csv.writer(file1)
    writer1.writerow(["diameter", "radius", "ave_path_length"])
    writer1.writerow([diameter, radius, ave_path_length])
print("scc: ", datetime.datetime.now())
