# Community Detection Script 

There are 3 steps in community detection

## Identify communities using Multi-level algorithm 
find_contract2019_community_multilevel_realEdgeIndex_3mon.py 
Note: python igraph library output communities edgelist using index instead of real value of nodes. In order to perform matching in next step, it is needed to attach values (which is annual basis index) to each nodes. 

## Match communities in 3-month dataset and 1-month dataset
find_continuous_community1_grow_die_compareREALindex.py
This script makes use of vf2 algorithm for subiomorphism matching. The matching not only consider graph shape but also node values to be matched. 

## Extract properties for each community
extract_contract2016_properties.py
The script extract local and global properties of each community to be training/testing data. 
