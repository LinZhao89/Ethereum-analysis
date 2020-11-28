
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
path2 = "D:/"
year = "byMonth/2017/2017_"
year = "2017_"
jan1 = path2+year+"jan.csvtest.txt"
feb1 = path2+year+"feb.csvtest.txt"
mar1 = path2+year+"mar.csvtest.txt"
apr1 = path2+year+"apr.csvtest.txt"
may1 = path2+year+"may.csvtest.txt"
jun1 = path2+year+"jun.csvtest.txt"
jul1 = path2+year+"jul.csvtest.txt"
aug1 = path2+year+"aug.csvtest.txt"
sep1 = path2+year+"sep.csvtest.txt"
octo1 = path2+year+"oct.csvtest.txt"
nov1 = path2+year+"nov.csvtest.txt"
dec1 = path2+year+"dec.csvtest.txt"

janfeb=path2+year+"sep.csvtest.txt"

WCCtriangle_counting= path2+'2017_sep_IGRAPH_WCC_trangles2.csv'
WCCtransitivity= path2+'2017_sep_IGRAPH_WCC_transivityNode2.csv'
SCC_WCC_summary = path2+'2017_sep_IGRAPH_WCC_trangles_summary2.csv'

#multi_edge_list = pd.read_csv(multi, header = None)
multiGraph = Graph.Read_Edgelist(janfeb, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)

weakConnectedComponent = simpleGraph.components(mode=WEAK)
maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
maxWeakConnectedComponent.to_undirected() 

WCCtran_localCoe = maxWeakConnectedComponent.transitivity_local_undirected(mode='zero')
WCCtran_nodedf=pd.DataFrame(WCCtran_localCoe)

WCC_subgraph_degree = maxWeakConnectedComponent.degree()
#for ver1 in maxWeakConnectedComponent.vs:
#    print(ver1)
#    print(f' degree{ ver1.degree()}')

num_triangle=[]
for idx in range(len(WCCtran_localCoe)):
    numtriangle = round(0.5* WCCtran_localCoe[idx] * WCC_subgraph_degree[idx] *( WCC_subgraph_degree[idx]-1))
    num_triangle.append(numtriangle)
#WCCtran_nodedf = WCCtran_nodedf.fillna(0)
#WCCave_tran_node = sum(WCCtran_nodedf[0])/len(WCCtran_nodedf[0])
#print(f'--WCCave_tran_node_nonan: {WCCave_tran_node}')
    
with open(WCCtriangle_counting, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['node_degree', 'node_triangle'])
    writer.writerows(zip(WCC_subgraph_degree, num_triangle))
    
WCCsum_triangle = sum(num_triangle)
print(f'sum of all triangles: {WCCsum_triangle}')

'''global culstering coefficient'''
WCCave_tran_node = maxWeakConnectedComponent.transitivity_avglocal_undirected(mode='zero') #average culstering, yes, but didnt count nan
print(f'global culstering coefficient: {WCCave_tran_node}')
#with open(WCCtransitivity, 'w') as f:
#    f.write(WCCtran_nodedf.to_string(header = False, index = False))  

'''global transivity'''
WCCglobal_transivity =maxWeakConnectedComponent.transitivity_undirected() # samve as networkx nx.transitivity result 
print(f' global transivity: {WCCglobal_transivity}')

''' ------------OUTPUT SUMMARY---------------'''
with open(SCC_WCC_summary, 'w') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow(["WCCave_tran_node","WCCglobal_transivity","SCCsum_triangle"]) 
    writer2.writerow([WCCave_tran_node,WCCglobal_transivity,WCCsum_triangle])

print("start: ", datetime.datetime.now())














#reciprocity_igraph = simpleGraph.reciprocity()
#asso_igraph = simpleGraph.assortativity_degree(directed=False)
#
#StrongConnectedComponent = simpleGraph.components(mode=STRONG)
#leng_strongCC= len(StrongConnectedComponent)
#maxStrongConnectedComponent = StrongConnectedComponent.giant()  #dd is the giant graph
#strong_num_node=maxStrongConnectedComponent.vcount()
#print(strong_num_node)

# weakConnectedComponent = simpleGraph.components(mode=WEAK)
# leng_weakCC= len(weakConnectedComponent)
# print(leng_weakCC)
# maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
# weak_num_node=maxWeakConnectedComponent.vcount()
# print(weak_num_node)


##-------------calcualte core from largest weakly cppnnected component----grapy:maxWeakConnectedComponent----------
#maxWeakConnectedComponent.to_undirected()   
#core_decom=maxWeakConnectedComponent.shell_index(mode=ALL)
## the argument is value within range of core_decom
#kcore = maxWeakConnectedComponent.k_core(max(core_decom))
#main_coreV=kcore.vcount()
#main_coreE = kcore.ecount()
# xx=pd.DataFrame(core_decom)
# xx.to_csv(core_number, index=False)
    
          
# with open(numCC_output, 'w', newline='') as file2:
#       writer2 = csv.writer(file2)
#       writer2.writerow(['reciprocity_overall','Assor_simpleUndirected','numStrongComponent',
#                         'len(largestStrongComponent)','numWeakComponent','len(largestWeakomponent)',
#                         'mainCoreG.number_of_nodes()','mainCoreG.number_of_edges()']) 
#       writer2.writerow([reciprocity_igraph,asso_igraph, leng_strongCC,
#                       strong_num_node,leng_weakCC,weak_num_node,main_coreV, main_coreE])
