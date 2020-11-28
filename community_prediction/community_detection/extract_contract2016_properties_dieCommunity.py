# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:13:35 2020

@author: linzhao2

baseed on the file name to load in each graph => calcuate the properties for each graph 
"""
import os
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

name = "1-3_to_4_"       
name2 = "2016_123/2/"
path2 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/"
#path2 ="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/"
year= "byMonth/3month_data/multilabel/"

# jan1 = path2+year+"jan.csvtest.txt"
# janfeb=path2+"contract_net_2016_fulltest.txt"

# node_list = pd.read_csv(nod, header = None)
#multiGraph = Graph.Read_Edgelist(aug1, directed=True) # produce multiDigraph 
#simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
filelist = pd.read_csv(path2+year+name+"matchGraph_name_growthg2g1.csv", header=None)
filelist.columns=['90days', 'dec']
filelist1 = filelist.drop_duplicates(subset=['90days'])

directoryPath = path2 +year+ name2
'''
transitivity=[]
diameter=[]
radius=[]
ave_shortest_path_length = []
density=[]
sum_triangle=[]
ave_clustering_coeff=[]
articulation=[]
adhesion=[]
cohesion=[]
reciprocity=[]
assort=[]
'''

feature = []
count=0
entries = os.listdir(directoryPath)

for i in entries:
    if i not in filelist1.values:
        print(i)
        count+=1
   # if entry.endswith('.csv'):
        g1 = Graph.Read_Edgelist(path2+year+name2+i, directed=True)
        num_node = g1.vcount()
        num_edge = g1.ecount()
        density=2*num_node/(num_edge*(num_edge-1))
        
        # triangle, transitivity
        transitivity=g1.transitivity_undirected()
        sum_triangle=len(g1.cliques(min=3, max=3))
        ave_clustering_coeff=g1.transitivity_avglocal_undirected(mode='zero')
        
        ### art, adhesion, cohesion
        articulation=g1.articulation_points() 
        adhesion=g1.adhesion()
        cohesion=g1.cohesion()
        
        # rec, assort
        reciprocity=g1.reciprocity()
        assort=g1.assortativity_degree(directed=False)
        
        ### diameter radius
        eccen = g1.eccentricity()
        eccen1 = [i for i in eccen if i != 0]
        diameter = max(eccen1)
        radius = min(eccen1)
        
        ### shortest path length
        shortestpath_length = g1.shortest_paths(mode=ALL)
        total_dist = 0
        count1=0
        for each in range(len(shortestpath_length)): 
            sum_dist=0
            for i in shortestpath_length[each]:
                if i != float("inf"):
                    sum_dist= sum_dist+i
                    count1+=1
            # print(f' sum_dist----: {sum_dist}')
            total_dist = total_dist+sum_dist
            # print (f' total_dist=========== : {total_dist}')
        if count1 != 0:
            ave_shortest_path = total_dist/count1
        print(f'wcc ave_shortest {ave_shortest_path}')
        
        print(f' total number of files {count}')
        feature.append([num_node,num_edge,density,transitivity,sum_triangle,ave_clustering_coeff
                        ,len(articulation),adhesion,cohesion,reciprocity,assort,diameter,radius,ave_shortest_path])

df2=pd.DataFrame(feature)
df2.columns=['num_node','num_edge','density','transitivity','sum_triangle','ave_clustering_coeff','articulation','adhesion'
             ,'cohesion','reciprocity','assort','diameter','radius','ave_shortest_path']
df2.to_csv(path2+year+name+"matchGraph_features_more2_growth_die.csv", index=False,header=True)