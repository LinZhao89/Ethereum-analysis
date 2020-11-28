
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

name = "2019_7-9_to_10_4more_"
name2="2019_789_4more/index/"
path2 ="D:/"

year= "byMonth/3month_data/multilabel/"

# jan1 = path2+year+"jan.csvtest.txt"
# janfeb=path2+"contract_net_2016_fulltest.txt"

# node_list = pd.read_csv(nod, header = None)
#multiGraph = Graph.Read_Edgelist(aug1, directed=True) # produce multiDigraph 
#simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
filelist = pd.read_csv(path2+year+name+"matchGraph_name_growth_compareRealIdx_g1g2.csv", header=None)
filelist.columns=['150days', 'dec']
filelist1 = filelist.drop_duplicates(subset=['150days'])

directoryPath = path2 + year+ name2
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
countNum = 0

with open(path2+year+name +'matchGraph_features_more4_growth_die_multiG2.csv', mode='a') as f:
    f.write('num_node'+','+'num_edge'+','+'density'+','+'transitivity'+','+'sum_triangle'+','+'ave_clustering_coeff'+','
         +'len(articulation)'+','+'adhesion'+','+'cohesion'+','+'reciprocity'+','+'assort'+','+'diameter'+','+'radius'+'\n')

    for i in entries:
        if i not in filelist1.values :
            print(i)
            count+=1
            if (count < 500):
       # if entry.endswith('.csv'):
                g1 = Graph.Read_Edgelist(path2+year+name2+i, directed=True)
                #g1= g1.simplify(multiple=True, loops = False, combine_edges = None)
                g1.to_undirected()
            
                num_node = g1.vcount()
                num_edge = g1.ecount()
                if(num_node < 5000):
                    density=2*num_edge/(num_node*(num_node-1))
            
            # triangle, transitivity
                    transitivity=g1.transitivity_undirected()
                    sum_triangle=len(g1.cliques(min=3, max=3))
                    ave_clustering_coeff=g1.transitivity_avglocal_undirected(mode='zero')
            
            ### art, adhesion, cohesion
                    articulation=g1.articulation_points() 
                    adhesion=g1.adhesion()
                    cohesion=g1.cohesion()
                    print('end of ad/co') 
            # rec, assort
                    reciprocity=g1.reciprocity()
                    assort=g1.assortativity_degree(directed=False)
            
            ### diameter radius
                    eccen = g1.eccentricity()
                    eccen1 = [i for i in eccen if i != 0]
                    diameter = max(eccen1)
                    radius = min(eccen1)
    
                    print(f' total number of files {count}')
                    f.write(str(num_node)+','+str(num_edge)+','+str(density)+','+str(transitivity)+','+str(sum_triangle)+','+str(ave_clustering_coeff)+','
                            +str(len(articulation))+','+str(adhesion)+','+str(cohesion)+','+str(reciprocity)+','+str(assort)+','+str(diameter)+','+str(radius)+'\n')
                    
                    feature.append([num_node,num_edge,density,transitivity,sum_triangle,ave_clustering_coeff
                            ,len(articulation),adhesion,cohesion,reciprocity,assort,diameter,radius])
print(count)
df2=pd.DataFrame(feature)
df2.columns=['num_node','num_edge','density','transitivity','sum_triangle','ave_clustering_coeff','articulation','adhesion'
             ,'cohesion','reciprocity','assort','diameter','radius']
df2.to_csv(path2+year+name + "matchGraph_features_more4_growth_die_multiG1.csv", index=False,header=True)

