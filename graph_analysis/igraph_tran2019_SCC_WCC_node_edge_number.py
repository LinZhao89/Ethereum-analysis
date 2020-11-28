
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

filename = "trace_net_2019test.txt"
print(filename)
numCC_output= path1 + filename + "_WCC_SCC_node_edge_num.csv"


#multi_edge_list = pd.read_csv(multi, header = None)
multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)

#reciprocity_igraph = simpleGraph.reciprocity()
#asso_igraph = simpleGraph.assortativity_degree(directed=False)

StrongConnectedComponent = simpleGraph.components(mode=STRONG)
leng_strongCC= len(StrongConnectedComponent)
maxStrongConnectedComponent = StrongConnectedComponent.giant()  #dd is the giant graph
strong_num_node=maxStrongConnectedComponent.vcount()
print(f'strong_num_node:{strong_num_node}')
strong_num_edge=maxStrongConnectedComponent.ecount()
print(f'strong_num_edge:{strong_num_edge}')

weakConnectedComponent = simpleGraph.components(mode=WEAK)
leng_weakCC= len(weakConnectedComponent)
maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
weak_num_node=maxWeakConnectedComponent.vcount()
print(f'weak_num_node: {weak_num_node}')
weak_num_edge=maxWeakConnectedComponent.ecount()
print(f'weak_num_edge: {weak_num_edge}')


##-------------calcualte core from largest weakly cppnnected component----grapy:maxWeakConnectedComponent----------
maxStrongConnectedComponent.to_undirected()   
core_decom=maxStrongConnectedComponent.shell_index(mode=ALL)
# the argument is value within range of core_decom
maxcore = max(core_decom)
kcore = maxStrongConnectedComponent.k_core(maxcore)
print(f' scc max core_decom value {maxcore}')
main_coreV=kcore.vcount()
main_coreE = kcore.ecount()
print(f' scc main node {main_coreV}')
print(f' scc main edge {main_coreE}')
#xx=pd.DataFrame(core_decom)
#xx.to_csv(core_number, index=False)
    
          
with open(numCC_output, 'w', newline='') as file2:
      writer2 = csv.writer(file2)
      writer2.writerow(['SCC_node_number','SCC_edge_number','WCC_node_number','WCC_edge_number',
                        'SCC maxCore value','SCCmainCoreG.number_of_nodes()','SCCmainCoreG.number_of_edges()']) 
      writer2.writerow([strong_num_node,strong_num_edge,weak_num_node,
                      weak_num_edge, maxcore, main_coreV, main_coreE])
