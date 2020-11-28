# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:40:10 2020

@author: linzhao2

method 1: using bi-directed edge - undirected edge 
"""

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
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/trace/2015/"
path1 = "/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/byMonth/month/"
path1="D:/blockchain data at sch/New folder/blockchain/submission/original/contract/byMonth/2016/"

filename ="2016_dec.csvtest.txt"
print(filename)

multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
multinum_node=multiGraph.vcount()
print(f'multinum_node:{multinum_node}')
multinum_edge=multiGraph.ecount()
print(f'multinum_edge:{multinum_edge}')

simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
sim_node_bi = simpleGraph.vcount()
sim_edge_bi = simpleGraph.ecount()
print(f' simpleNode:{sim_node_bi}')
print(f' simpleEdg: {sim_edge_bi}')

reciprocity_igraph = simpleGraph.reciprocity()

simpleGraph.to_undirected()
sim_node_un = simpleGraph.vcount()
sim_edge_un = simpleGraph.ecount()
print(f' simple-undiNode:{sim_node_un}')
print(f' simple-undiEdg: {sim_edge_un}')

print(f' difference: {sim_edge_bi - sim_edge_un}')
