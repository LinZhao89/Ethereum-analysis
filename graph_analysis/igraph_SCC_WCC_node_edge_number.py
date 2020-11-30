
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
path1="D:/"

# specify edgelist
filename = "trace_net_2019test.txt"
print(filename)
numCC_output= path1 + filename + "_WCC_SCC_node_edge_num.csv"

# loading
multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)

StrongConnectedComponent = simpleGraph.components(mode=STRONG)
leng_strongCC= len(StrongConnectedComponent)
maxStrongConnectedComponent = StrongConnectedComponent.giant()  # giant graph
strong_num_node=maxStrongConnectedComponent.vcount()
print(f'strong_num_node:{strong_num_node}')
strong_num_edge=maxStrongConnectedComponent.ecount()
print(f'strong_num_edge:{strong_num_edge}')

weakConnectedComponent = simpleGraph.components(mode=WEAK)
leng_weakCC= len(weakConnectedComponent)
maxWeakConnectedComponent = weakConnectedComponent.giant()  # giant graph
weak_num_node=maxWeakConnectedComponent.vcount()
print(f'weak_num_node: {weak_num_node}')
weak_num_edge=maxWeakConnectedComponent.ecount()
print(f'weak_num_edge: {weak_num_edge}')


##-------------calcualte core from largest weakly cppnnected component----grapy:maxWeakConnectedComponent----------
maxStrongConnectedComponent.to_undirected()   
core_decom=maxStrongConnectedComponent.shell_index(mode=ALL)

maxcore = max(core_decom)
kcore = maxStrongConnectedComponent.k_core(maxcore)
print(f' scc max core_decom value {maxcore}')
main_coreV=kcore.vcount()
main_coreE = kcore.ecount()
print(f' scc main node {main_coreV}')
print(f' scc main edge {main_coreE}')

          
with open(numCC_output, 'w', newline='') as file2:
      writer2 = csv.writer(file2)
      writer2.writerow(['SCC_node_number','SCC_edge_number','WCC_node_number','WCC_edge_number',
                        'SCC maxCore value','SCCmainCoreG.number_of_nodes()','SCCmainCoreG.number_of_edges()']) 
      writer2.writerow([strong_num_node,strong_num_edge,weak_num_node,
                      weak_num_edge, maxcore, main_coreV, main_coreE])
