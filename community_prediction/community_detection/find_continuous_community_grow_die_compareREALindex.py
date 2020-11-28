"""
Created on Wed Jul 29 23:38:35 2020

find same / subisomorphism for each month 
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

def cmp_nodes(g2, g1, i2, i1):
    return g1.vs[i1]['value'] == g2.vs[i2]['value']

def cmp_nodes1(g2, g1, i2, i1):
    return g1.vs[i1]['value'] == g2.vs[i2]['value']

name = "2018_9-11_to_12_4more_"
path2 ="D:/"

year= "byMonth/3month_data/"

directoryPath1 = path2 +year +"multilabel/2018_91011_4more/index/"
directoryPath2 = path2 +year + "multilabel/2018_12_2more/index/"
nod1 = path2 +year +"multilabel/2018_91011_4more/hashed/result/"
nod2 = path2 +year +"multilabel/2018_12_2more/hashed/result/"

ent1 = []
catchName1=[]
entries1 = os.listdir(directoryPath1)
for entry1 in entries1:
    if entry1.endswith('.txt'):
        print(f' {entry1.split(".")[0]}')
        g1 = Graph.Read_Edgelist(directoryPath1+entry1, directed=False) # produce multiDigraph 
        node_list1 = pd.read_csv(nod1+entry1.split(".")[0]+ ".csvhased.csv", header = None)
        for i in g1.vs:
            i['value'] = node_list1[1][i.index]
#            print(i['value'])
        ent1.append(g1)
        catchName1.append(entry1)


catchName2=[]
ent2 = []        
entries2 = os.listdir(directoryPath2)
for entry2 in entries2:
    
    if entry2.endswith('.txt'):
        print(f' {entry2}')
        print('-----------')
        g2 = Graph.Read_Edgelist(directoryPath2+entry2, directed=False) # produce multiDigraph 
        node_list2 = pd.read_csv(nod2+entry2.split(".")[0]+ ".csvhased.csv", header = None)
        for i in g2.vs:
            i['value'] = node_list2[1][i.index]
#            print(i['value'])
#        for i in g2.vs:
#            i['value'] = i.index
        ent2.append(g2) 
        catchName2.append(entry2)

print("------finish take in---------")
        
g1g2=[] 

Name12 = []

count1=0

for x1 in ent1:
    # print(g1)
#    for v in x1.vs:
#            v['value'] = v.index
    count2=0
    for x2 in ent2:
        result2 = x1.subisomorphic_vf2(x2,node_compat_fn=cmp_nodes)

        if result2 ==True:
            g1g2.append([x1, x2])
            Name12.append([catchName1[count1], catchName2[count2]])
            
        count2+=1
    count1+=1
print(Name12)        
df2=pd.DataFrame(Name12)
df2.columns=['g1', 'g2']
g1name =df2.drop_duplicates(subset=['g1'])['g1'].tolist()


for i in catchName1:
    if i not in g1name:
        print(i)
        g1_rest = Graph.Read_Edgelist(directoryPath1+i, directed=False) 

        for j in g1_rest.vs:
            j['value'] = j.index
     
        if g1_rest.vcount() >5:
            g1_rest_sub = g1_rest.decompose(mode=WEAK)
            for g3 in g1_rest_sub:
                count2=0
                for g2 in ent2:
                    result3 = g2.subisomorphic_vf2(g3,node_compat_fn=cmp_nodes1 )
                    #result3 = g2.subisomorphic_vf2(g3)
                    print(result3)
                    if result3 ==True:
                        print(g3)
                        print(g2)
                        print("enter result 3=true")
                        g1g2.append([g3, g2])
                        Name12.append([i, catchName2[count2]])
                    count2+=1
        
        
df1=pd.DataFrame(g1g2)
df2=pd.DataFrame(Name12)
df2.columns=['g1', 'g2']
df2.to_csv(path2+year+name+"matchGraph_name_growth_compareRealIdx_g1g2.csv", index=False,header=False)
df3 = pd.concat([df1, df2], axis=1)
df3.to_csv(path2+year+name+"matchGraph_compareRealIdxd.csv", index=False,header=False)
