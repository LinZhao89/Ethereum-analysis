
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
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/trace/2015/"
path1 = "/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/byMonth/month/"
#path1="D:/blockchain data at sch/New folder/blockchain/submission/original/contract/byMonth/2016/"

filename ="2016_oct.csvtest.txt"
print(filename)

# numCC_output= path1 + filename1 + "_Reciprocity_Asso_strongWeak_CC.csv"
# score_number = path1+filename1+'scc_core_number.csv'
# wcore_number = path1+filename1+'wcc_core_number.csv'
# num_output= path1 + filename1+ "_simpleDirected_node_edge_num.csv"

multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
multinum_node=multiGraph.vcount()
print(f'multinum_node:{multinum_node}')
multinum_edge=multiGraph.ecount()
print(f'multinum_edge:{multinum_edge}')

simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
sim_node = simpleGraph.vcount()
sim_edge = simpleGraph.ecount()
print(f' simpleNode:{sim_node}')
print(f' simpleEdg: {sim_edge}')

reciprocity_igraph = simpleGraph.reciprocity()
print(f'reciprocity_igraph: {reciprocity_igraph}')
asso_igraph = simpleGraph.assortativity_degree(directed=False)
print(f'asso_igraph: {asso_igraph}')

# StrongConnectedComponent = simpleGraph.components(mode=STRONG)
# leng_strongCC= len(StrongConnectedComponent)
# print(f' # scc {leng_strongCC}')
# maxStrongConnectedComponent = StrongConnectedComponent.giant()  #dd is the giant graph
# strong_num_node=maxStrongConnectedComponent.vcount()
# print(f' scc node: {strong_num_node}')
# scc_num_edge = maxStrongConnectedComponent.ecount()
# print(f' scc edge {scc_num_edge}')

# weakConnectedComponent = simpleGraph.components(mode=WEAK)
# leng_weakCC= len(weakConnectedComponent)
# print(f' # wcc : {leng_weakCC}')
# maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
# weak_num_node=maxWeakConnectedComponent.vcount()
# print(f' wcc node: {weak_num_node}')
# wcc_num_edge = maxWeakConnectedComponent.ecount()
# print(f' wcc edge: {wcc_num_edge}')


# ##-------------calcualte core from largest weakly cppnnected component----grapy:maxWeakConnectedComponent----------
# maxWeakConnectedComponent.to_undirected()   
# core_decom=maxWeakConnectedComponent.shell_index(mode=ALL)
# # the argument is value within range of core_decom
# kcore = maxWeakConnectedComponent.k_core(max(core_decom))
# print(f' wcc max(core-decom) {max(core_decom)}')
# wmain_coreV=kcore.vcount()
# wmain_coreE = kcore.ecount()
# xx=pd.DataFrame(core_decom)
# xx.to_csv(wcore_number, index=False)

# maxStrongConnectedComponent.to_undirected()   
# core_decom=maxStrongConnectedComponent.shell_index(mode=ALL)
# # the argument is value within range of core_decom
# kcore = maxWeakConnectedComponent.k_core(max(core_decom))
# print(f' scc max(core_decom): {max(core_decom)}')
# smain_coreV=kcore.vcount()
# smain_coreE = kcore.ecount()
# xx=pd.DataFrame(core_decom)
# xx.to_csv(score_number, index=False)

    
          
# with open(numCC_output, 'w', newline='') as file2:
#       writer2 = csv.writer(file2)
#       writer2.writerow(['multi_node','multi_edge','sim_node','sim_edge','reciprocity_overall','Assor_simpleUndirected',
#                         'numStrongComponent','max scc node','max scc edge', 
#                         'numWeakComponent','max wcc node','max wcc edge',
#                         'wcc mainCoreG.number_of_nodes()','wcc mainCoreG.number_of_edges()',
#                         'scc mainCoreG.number_of_nodes()','scc mainCoreG.number_of_edges()']) 
#       writer2.writerow([multinum_node, multinum_edge, sim_node, sim_edge, reciprocity_igraph,asso_igraph,
#                         leng_strongCC,strong_num_node,scc_num_edge,
#                         leng_weakCC,weak_num_node,wcc_num_edge,
#                         wmain_coreV, wmain_coreE,
#                         smain_coreV, smain_coreE])
