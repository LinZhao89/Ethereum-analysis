'''for multilevel community detection algorithm '''
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
        
path2 ="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/"
path1 =path2 + "2018/"

nod =path1 + "contract_net_address_hash_2018_full.csv"
node_list = pd.read_csv(nod, header = None)

# path2 ="D:/blockchain data at sch/New folder/blockchain/submission/original/contract/"

#path2="/home/LinZamOu/graph/blockchain/contract/"
year = "byMonth/3month_data/label/short/2018_"

# year2 = "byMonth/3month_data/multilabel/2018_10/"
year2 = "byMonth/3month_data/multilabel/2018_9_2more/"

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


month = "9"
janfeb=path2+year+"jun.csvtest.txt"
#janfeb = path2+"byMonth/3month_data/train/2016_jan_feb_mar.csvtest.txt"
# janfeb=path2+"contract_net_2016_fulltest.txt"

# node_list = pd.read_csv(nod, header = None)
multiGraph = Graph.Read_Edgelist(sep1, directed=True) # produce multiDigraphi 
#simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
simpleGraph = multiGraph
simpleGraph.to_undirected()
print("1: ", datetime.datetime.now())
vs = VertexSeq(simpleGraph)
for ver in simpleGraph.vs:
    ver["value"]=node_list[1][ver.index]   
    # print(ver["value"])

walk_cluster =simpleGraph.community_multilevel()

largest_cluster=walk_cluster.giant()
mainE = largest_cluster.ecount()
mainV = largest_cluster.vcount()
print(f' giant V: {mainV}, giantE = {mainE}')

all_subgraaph=walk_cluster.subgraphs()
print("2: ", datetime.datetime.now())

count=0
for idx in range(len(all_subgraaph)):
    if all_subgraaph[idx].vcount() > 2:
        count+=1
        each_edge = all_subgraaph[idx].get_edgelist()
        xxx  = all_subgraaph[idx].vs['value']
        df_merge=pd.DataFrame(each_edge)
        each_edge_real = []
        for each in each_edge: 
            each_edge_real.append([xxx[each[0]], xxx[each[1]]])
        df_merge_real=pd.DataFrame(each_edge_real)                           
        df_merge_real.to_csv(path2+year2+"hashed/"+"2moreThannode_"+month+str(count)+"_eachGraph.csv", index=False,header=False)
        df_merge.to_csv(path2+year2+"index/"+ "2moreThannode_"+month+str(count)+"_eachGraph.csv", index=False,header=False)
'''
with open(path2+year2+month+"_contract2016_summary_multilevel.csv", 'w', newline='') as file1:
    writer1 = csv.writer(file1)
    writer1.writerow(["giantE", "giantV", "count"])
    writer1.writerow([mainE, mainV, count])
print("scc: ", datetime.datetime.now())
'''
# count1=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 2:
#         count1+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"2moreThannode_"+month+str(count1)+"_eachGraph.csv", index=False,header=False)
# count2=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 3:
#         count2+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"3moreThannode_"+month+str(count2)+"_eachGraph.csv", index=False,header=False)
# count3=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 4:
#         count3+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"4moreThannode_"+month+str(count3)+"_eachGraph.csv", index=False,header=False)
# count4=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 5:
#         count4+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"5moreThannode_"+month+str(count4)+"_eachGraph.csv", index=False,header=False)
# count5=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 6:
#         count5+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"6moreThannode_"+month+str(count5)+"_eachGraph.csv", index=False,header=False)
# count6=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 7:
#         count6+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"7moreThannode_"+month+str(count6)+"_eachGraph.csv", index=False,header=False)
        
# count7=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 8:
#         count7+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"8moreThannode_"+month+str(count7)+"_eachGraph.csv", index=False,header=False)
# print("scc: ", datetime.datetime.now())        
# count8=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 9:
#         count8+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"9moreThannode_"+month+str(count8)+"_eachGraph.csv", index=False,header=False)
        
# count9=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 10:
#         count9+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"10moreThannode_"+month+str(count9)+"_eachGraph.csv", index=False,header=False)
        
# count10=0
# for idx in range(len(all_subgraaph)):
#     if all_subgraaph[idx].vcount() > 11:
#         count10+=1
#         each_edge = all_subgraaph[idx].get_edgelist()
#         #    print(each_edge)
#         df_merge=pd.DataFrame(each_edge)
#         df_merge.to_csv(path2+year2+"11moreThannode_"+month+str(count10)+"_eachGraph.csv", index=False,header=False)

# out = pd.Series(membership, ind)
# merges_val = walk_result_apr.merges
#df_merge=pd.DataFrame(membership)
#df_merge.to_csv(path2+year2+month+"_contract2017__simple.csv", index=True)
