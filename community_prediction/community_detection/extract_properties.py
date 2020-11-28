
"""
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

name = "2018_8-10_to_11_4more_"
name1="2018_8910_4more/index/"

path2 ="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/"
year= "byMonth/3month_data/multilabel/"
filelist = pd.read_csv(path2+year+name+"matchGraph_name_growth_compareRealIdx_g1g2.csv", header=None)
filelist.columns=['150days', 'dec']
filelist1 = filelist.drop_duplicates(subset=['150days'])

directoryPath = path2 + year+name1
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
for i in filelist1.values:
    print(i[0])
    if i[0] in entries:
        count+=1
   # if entry.endswith('.csv'):
        g1 = Graph.Read_Edgelist(path2+year+name1+i[0], directed=True)
        #g1 = g1.simplify(multiple=True, loops=False, combine_edges =None)
        g1.to_undirected()

        num_node = g1.vcount()
        num_edge = g1.ecount()
        if num_edge > 1:
            density=2*num_edge/(num_node*(num_node-1))
        
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
        
            print(f' total number of files {count}')
            feature.append([num_node,num_edge,density,transitivity,sum_triangle,ave_clustering_coeff
                        ,len(articulation),adhesion,cohesion,reciprocity,assort,diameter,radius])

df2=pd.DataFrame(feature)
df2.columns=['num_node','num_edge','density','transitivity','sum_triangle','ave_clustering_coeff','articulation','adhesion'
             ,'cohesion','reciprocity','assort','diameter','radius']
df2.to_csv(path2+year+name+"matchGraph_features_more4_growth_multiG.csv", index=False,header=True)
