
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
path1="D:/"

filename ="2016_oct.csvtest.txt"
print(filename)

multiGraph = Graph.Read_Edgelist(path1 + filename, directed=True) # produce multiDigraph 
multinum_node=multiGraph.vcount()
print(f'multinum_node:{multinum_node}')
multinum_edge=multiGraph.ecount()
print(f'multinum_edge:{multinum_edge}')

simpleGraph = multiGraph.simplify(multiple=True, loops=True, combine_edges=None)
sim_node = simpleGraph.vcount()
sim_edge = simpleGraph.ecount()
print(f' simpleNode:{sim_node}')
print(f' simpleEdg: {sim_edge}')

reciprocity_igraph = simpleGraph.reciprocity()
print(f'reciprocity_igraph: {reciprocity_igraph}')
asso_igraph = simpleGraph.assortativity_degree(directed=False)
print(f'asso_igraph: {asso_igraph}')

