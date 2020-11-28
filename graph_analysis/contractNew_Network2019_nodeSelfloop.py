# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:31:26 2020

@author: zhao lin
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
# path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contracts/2016/"
path1="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/2019/"
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/2015/"
# path1="C:/Users/linzhao2/Downloads/"
filename = "contract_net_2019_full"
print(filename)
multi =path1 + filename+ ".csv" 
#undir = path1+path2+'transaction_net_2019.csvremoveDuplicate.csv'
nod = path1+"contract_net_address_hash_2019_full.csv"
degreeDistribution_output= path1 + filename + "_node_selfloop_multiDiG.csv"
#in_out_degree_output = path1+filename+'_in_out_degree_multiDiG.csv'
# properties= path1+filename+'properties.csv'
# core_number = path1+filename+'core_number_byNode.csv'
multi_edge_list = pd.read_csv(multi, header = None)
node_list = pd.read_csv(nod, header = None)

####should use multigraph(undirected) or multiDigraph (directed), cause each node may have multiple edges 
#multidiG = nx.MultiDiGraph()
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
#    writer1.writerow(["idx", "node", "multidigraph_in", "multidigraph_out"])
#    for i, nodrow  in node_list.iterrows():
#        # number of degree
#        x = multidiG.degree(nodrow[1])
#        # y = simpleG.degree(nodrow[1])
#        # number of in/out degrree
#        gindegree = multidiG.in_degree(nodrow[1])
#        goutdegree = multidiG.out_degree(nodrow[1])
#        
#        # write to csv
#        # writer.writerow([nodrow[1],nodrow[0], x , y])
#        writer.writerow([nodrow[1],nodrow[0], x ])
#        writer1.writerow([nodrow[1],nodrow[0], gindegree , goutdegree])

print("end: ", datetime.datetime.now())
  
# reciprocity_overall = nx.algorithms.overall_reciprocity(diG)
# assortativity_Digraph = nx.algorithms.assortativity.degree_assortativity_coefficient(simpleG) 
#degreeCentrality = nx.algorithms.centrality.degree_centrality(simpleG) # node is key, then value 

# numStrongComponent = nx.algorithms.components.number_strongly_connected_components(diG)
# largestStrongComponent = max(nx.algorithms.components.strongly_connected_components(diG), key=len)
# print(f'len of largestStrongComponent: {len(largestStrongComponent)}')
# numWeakComponent = nx.algorithms.components.number_weakly_connected_components(diG)
# largestWeakomponent = max(nx.algorithms.components.weakly_connected_components(diG), key=len)
# print(f'len of largestWeakomponent: {len(largestWeakomponent)}')

# no argumeent return main core, 
#The main core is the core with the largest degree.
#https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=1507&context=dissertations




# simpleG.remove_edges_from(nx.selfloop_edges(simpleG))  
# mainCoreG = nx.algorithms.core.k_core(simpleG) 
# coreNum = nx.algorithms.core.core_number(simpleG)

# print('mainCoreG # of nodes: {}'.format(mainCoreG.number_of_nodes()))
# print('mainCoreG # of edges: {}'.format(mainCoreG.number_of_edges()))

# with open(core_number, 'w', newline='') as file3:
#     writer3 = csv.writer(file3)
#     for key, value in coreNum.items():
#        writer3.writerow([key, value])
    
# with open(properties, 'w', newline='') as file2:
#      writer2 = csv.writer(file2)
#      writer2.writerow(['reciprocity_overall','numStrongComponent',
#                        'len(largestStrongComponent)','numWeakComponent','len(largestWeakomponent)',
#                        'mainCoreG.number_of_nodes()','mainCoreG.number_of_edges()']) 
#      writer2.writerow([reciprocity_overall,numStrongComponent,
#                       len(largestStrongComponent),numWeakComponent,len(largestWeakomponent),mainCoreG.number_of_nodes(),
#                       mainCoreG.number_of_edges()])
                      
#                      
#                      multidiG.number_of_edges(),simpleG.number_of_edges(),nx.number_of_selfloops(multidiG),
#                      nx.number_of_selfloops(simpleG)])
