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
        
path1 = 'D:'
filename ="contract_net_2017_fulltest.txt"
print(filename)
numCC_output= path1 + filename + "_Reciprocity_Asso_strongWeak_CC.csv"
score_number = path1+filename+'scc_core_number.csv'
wcore_number = path1+filename+'wcc_core_number.csv'
num_output= path1 + filename + "_simpleDirected_node_edge_num.csv"

multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
multinum_node=multiGraph.vcount()
print(f'multinum_node:{multinum_node}')
multinum_edge=multiGraph.ecount()
print(f'multinum_edge:{multinum_edge}')

simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)

reciprocity_igraph = simpleGraph.reciprocity()
asso_igraph = simpleGraph.assortativity_degree(directed=False)

StrongConnectedComponent = simpleGraph.components(mode=STRONG)
leng_strongCC= len(StrongConnectedComponent)
print(f' # scc {leng_strongCC}')
maxStrongConnectedComponent = StrongConnectedComponent.giant()  #dd is the giant graph
strong_num_node=maxStrongConnectedComponent.vcount()
print(f' scc node: {strong_num_node}')
scc_num_edge = maxStrongConnectedComponent.ecount()
print(f' scc edge {scc_num_edge}')

weakConnectedComponent = simpleGraph.components(mode=WEAK)
leng_weakCC= len(weakConnectedComponent)
print(f' # wcc : {leng_weakCC}')
maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
weak_num_node=maxWeakConnectedComponent.vcount()
print(f' wcc node: {weak_num_node}')
wcc_num_edge = maxWeakConnectedComponent.ecount()
print(f' wcc edge: {wcc_num_edge}')


##-------------calcualte core from largest weakly cppnnected component--------------
maxWeakConnectedComponent.to_undirected()   
core_decom=maxWeakConnectedComponent.shell_index(mode=ALL)
# the argument is value within range of core_decom
kcore = maxWeakConnectedComponent.k_core(max(core_decom))
print(f' wcc max(core-decom) {max(core_decom)}')
wmain_coreV=kcore.vcount()
wmain_coreE = kcore.ecount()
xx=pd.DataFrame(core_decom)
xx.to_csv(wcore_number, index=False)

maxStrongConnectedComponent.to_undirected()   
core_decom=maxStrongConnectedComponent.shell_index(mode=ALL)
# the argument is value within range of core_decom
kcore = maxWeakConnectedComponent.k_core(max(core_decom))
print(f' scc max(core_decom): {max(core_decom)}')
smain_coreV=kcore.vcount()
smain_coreE = kcore.ecount()
xx=pd.DataFrame(core_decom)
xx.to_csv(score_number, index=False)
          
with open(numCC_output, 'w', newline='') as file2:
      writer2 = csv.writer(file2)
      writer2.writerow(['reciprocity_overall','Assor_simpleUndirected',
                        'numStrongComponent','max scc node','max scc edge', 
                        'numWeakComponent','max wcc node','max wcc edge',
                        'wcc mainCoreG.number_of_nodes()','wcc mainCoreG.number_of_edges()',
                        'scc mainCoreG.number_of_nodes()','scc mainCoreG.number_of_edges()']) 
      writer2.writerow([reciprocity_igraph,asso_igraph,
                        leng_strongCC,strong_num_node,scc_num_edge,
                        leng_weakCC,weak_num_node,wcc_num_edge,
                        wmain_coreV, wmain_coreE,
                        smain_coreV, smain_coreE])
