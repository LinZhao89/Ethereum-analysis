
import igraph
from igraph import *

import pandas as pd
import csv
import sys
maxInt = sys.maxsize
import datetime


def triangles(g):
    cliques = g.cliques(min=3, max=3)
    result = [0] * g.vcount()
    for i, j, k in cliques:
        result[i] += 1
        result[j] += 1
        result[k] += 1
    return result


print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/2015/"
path1="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/2016/"
#path1 = 'C:/Users/linzhao2/Downloads/blockchain_data/'
#path1 = 'C:/Users/superLin/Documents/blockchain/'
filename = "contract_net_2016_fulltest.txt"
print(filename)
#nod = path1+"transaction_net_address_hash_2015.csv"

#core_number = path1+filename+'_IGRAPH_WCCmaincore_bystronglyNode.csv'
#WCCtriangle_counting= path1+filename+'_IGRAPH_WCC_trangles.csv'
SCCtriangle_counting= path1+filename+'_IGRAPH_SCC_trangles.csv'
#WCCtransitivity= path1+filename+'_IGRAPH_WCC_transivityNode.csv'
SCCtransitivity= path1+filename+'_IGRAPH_SCC_transivityNode.csv'
SCC_WCC_summary = path1+filename+'_IGRAPH_SCC_trangles_summary.csv'

#node_list = pd.read_csv(nod, header = None)
###multi_edge_list = pd.read_csv(multi, header = None)
multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
#vs = VertexSeq(simpleGraph)
#for ver in simpleGraph.vs:
#    ver["value"]=node_list[0][ver.index]
#    print(ver)
    
#    
'''STRONGLY  cc'''
STRONGConnectedComponent = simpleGraph.components(mode=STRONG)
maxSTRONGConnectedComponent = STRONGConnectedComponent.giant()  #dd is the giant graph
maxSTRONGConnectedComponent.to_undirected()   
#
#SCCtriangle_node = triangles(maxSTRONGConnectedComponent)
#
#xx=pd.DataFrame(SCCtriangle_node)
#with open(SCCtriangle_counting, 'w') as f:
#    f.write(xx.to_string(header = False, index = False))  
#    
#SCCsum_triangle = sum(SCCtriangle_node)
#
#SCCtran_node = maxSTRONGConnectedComponent.transitivity_local_undirected()
#SCCtran_nodedf=pd.DataFrame(SCCtran_node)
#SCCtran_nodedf = SCCtran_nodedf.fillna(0)
#SCCave_tran_node_nonan = sum(SCCtran_nodedf[0])/len(SCCtran_nodedf[0])
#print(f'--SCCave_tran_node_nonan: {SCCave_tran_node_nonan}')
#with open(SCCtransitivity, 'w') as f:
#    f.write(SCCtran_nodedf.to_string(header = False, index = False))  
#
#SCCave_tran_node = maxSTRONGConnectedComponent.transitivity_avglocal_undirected() #average culstering, yes, but didnt count nan
#print(f'SCCave_tran_node: {SCCave_tran_node}')
#SCCglobal_transivity = maxSTRONGConnectedComponent.transitivity_undirected() # samve as networkx nx.transitivity result 
#print(f' SCCglobal_transivity: {SCCglobal_transivity}')


#'''weakly cc'''
#weakConnectedComponent = simpleGraph.components(mode=WEAK)
#maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
#maxWeakConnectedComponent.to_undirected()   

#''' calculate trianle'''
#WCCtriangle_node = triangles(maxWeakConnectedComponent)
#print("start: ", datetime.datetime.now())
#xx=pd.DataFrame(WCCtriangle_node)
#with open(WCCtriangle_counting, 'w') as f:
#    f.write(xx.to_string(header = False, index = False))  
#WCCsum_triangle = sum(WCCtriangle_node)
#'''---------------------------------------------------------'''

'''local clustering coefficient'''
SCCtran_localCoe = maxSTRONGConnectedComponent.transitivity_local_undirected(mode='zero')
#SCCtran_nodedf=pd.DataFrame(SCCtran_localCoe)

SCC_subgraph_degree = maxSTRONGConnectedComponent.degree()
#for ver1 in maxWeakConnectedComponent.vs:
#    print(ver1)
#    print(f' degree{ ver1.degree()}')

num_triangle=[]
for idx in range(len(SCCtran_localCoe)):
    numtriangle = round(0.5* SCCtran_localCoe[idx] * SCC_subgraph_degree[idx] *( SCC_subgraph_degree[idx]-1))
    num_triangle.append(numtriangle)
#WCCtran_nodedf = WCCtran_nodedf.fillna(0)
#WCCave_tran_node = sum(WCCtran_nodedf[0])/len(WCCtran_nodedf[0])
#print(f'--WCCave_tran_node_nonan: {WCCave_tran_node}')
with open(SCCtriangle_counting, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['node_degree', 'node_triangle'])
    writer.writerows(zip(SCC_subgraph_degree, num_triangle))
    
SCCsum_triangle = sum(num_triangle)
print(f'sum of all triangles: {SCCsum_triangle}')

'''global culstering coefficient'''
SCCave_tran_node = maxSTRONGConnectedComponent.transitivity_avglocal_undirected(mode='zero') #average culstering, yes, but didnt count nan
print(f'global culstering coefficient: {SCCave_tran_node}')
#with open(WCCtransitivity, 'w') as f:
#    f.write(WCCtran_nodedf.to_string(header = False, index = False))  

'''global transivity'''
SCCglobal_transivity = maxSTRONGConnectedComponent.transitivity_undirected() # samve as networkx nx.transitivity result 
print(f' global transivity: {SCCglobal_transivity}')

''' ------------OUTPUT SUMMARY---------------'''
with open(SCC_WCC_summary, 'w') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow(["SCCave_tran_node","SCCglobal_transivity","SCCsum_triangle"]) 
    writer2.writerow([SCCave_tran_node,SCCglobal_transivity,SCCsum_triangle])

print("start: ", datetime.datetime.now())
#
#'''----------------------------------------------------'''
#StrongConnectedComponent = simpleGraph.components(mode=STRONG)
#leng_strongCC= len(StrongConnectedComponent)
#print(f'---{leng_strongCC}')
#maxStrongConnectedComponent = StrongConnectedComponent.giant()  #dd is the giant graph
##################maxStrongConnectedComponent.to_undirected()
#core_decom=maxStrongConnectedComponent.shell_index(mode=ALL)
#print(f' {len(core_decom)}')
## the argument is value within range of core_decom
#kcore = maxStrongConnectedComponent.k_core(max(core_decom))
#for ver1 in kcore.vs:
#    print(ver1)
#  
#main_coreV=kcore.vcount()
#main_coreE = kcore.ecount()
#with open(core_number, 'w') as f1:
#    writer2 = csv.writer(f1)
#    writer2.writerow(["WCC maincore V", "WCC maincore E"]) 
#    writer2.writerow([main_coreV,main_coreE])
#    
#vCentrality= kcore.betweenness()
#
#with open(centrality, 'w') as f2:
#    writer3 = csv.writer(f2)
#    writer3.writerow(["betweenCentrality", "account"]) 
#    for  idx, ver1 in enumerate(kcore.vs):
##        print(idx)
#        writer3.writerow([vCentrality[idx],ver1["value"]])
#


#xx=pd.DataFrame(vCentrality)
#with open(centrality, 'w') as f:
#    f.write(xx.to_string(header = False, index = False))   





















#strong_num_node=maxStrongConnectedComponent.vcount()
#print(strong_num_node)

#weakConnectedComponent = simpleGraph.components(mode=WEAK)
##leng_weakCC= len(weakConnectedComponent)
#maxWeakConnectedComponent = weakConnectedComponent.giant()  #dd is the giant graph
##weak_num_node=maxWeakConnectedComponent.vcount()
##print(weak_num_node)
###-------------calcualte core from largest weakly cppnnected component----grapy:maxWeakConnectedComponent----------
#maxWeakConnectedComponent.to_undirected()   
#core_decom=maxWeakConnectedComponent.shell_index(mode=ALL)
# the argument is value within range of core_decom
#kcore = maxStrongConnectedComponent.k_core(max(core_decom))





#xx=pd.DataFrame(core_decom)
#xx.to_csv(core_number, index=False)
    
          
#with open(numCC_output, 'w', newline='') as file2:
#      writer2 = csv.writer(file2)
#      writer2.writerow(['reciprocity_overall','Assor_simpleUndirected','numStrongComponent',
#                        'len(largestStrongComponent)','numWeakComponent','len(largestWeakomponent)',
#                        'mainCoreG.number_of_nodes()','mainCoreG.number_of_edges()']) 
#      writer2.writerow([reciprocity_igraph,asso_igraph, leng_strongCC,
#                      strong_num_node,leng_weakCC,weak_num_node,main_coreV, main_coreE])
