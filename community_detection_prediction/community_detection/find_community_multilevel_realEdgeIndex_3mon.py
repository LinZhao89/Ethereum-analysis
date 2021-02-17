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
        
path2 ="D/"
path1 =path2 + "2018/"

nod =path1 + "contract_net_address_hash_2018_full.csv"
node_list = pd.read_csv(nod, header = None)

year = "byMonth/3month_data/train/2018_"


year2 = "byMonth/3month_data/multilabel/2018_678_4more/"

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

month = "678"
janfeb=path2+year+"jun_jul_aug.csvtest.txt"
#janfeb = path2+"byMonth/3month_data/train/2016_jan_feb_mar.csvtest.txt"
# janfeb=path2+"contract_net_2016_fulltest.txt"

# node_list = pd.read_csv(nod, header = None)
multiGraph = Graph.Read_Edgelist(janfeb, directed=True) # produce multiDigraphi 
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

count=0
for idx in range(len(all_subgraaph)):
    if all_subgraaph[idx].vcount() > 4:
        count+=1
        each_edge = all_subgraaph[idx].get_edgelist()
        xxx  = all_subgraaph[idx].vs['value']
        df_merge=pd.DataFrame(each_edge)
        each_edge_real = []
        for each in each_edge: 
            each_edge_real.append([xxx[each[0]], xxx[each[1]]])
        df_merge_real=pd.DataFrame(each_edge_real)                           
        df_merge_real.to_csv(path2+year2+"hashed/"+"4moreThannode_"+month+str(count)+"_eachGraph.csv", index=False,header=False)
        df_merge.to_csv(path2+year2+"index/"+"4moreThannode_"+month+str(count)+"_eachGraph.csv", index=False,header=False)

