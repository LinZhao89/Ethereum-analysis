# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:20:11 2020

read degree value , find top 10 with its account name and multiDigraph degree value 
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
path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/token_trf/"


degree_top10 = path1+'degree_top10.csv'


degree_number = path1+'2015/token_net_2015_degreeDistribution.csv'
degree_list = pd.read_csv(degree_number)
data_sort = degree_list.sort_values("multiDigraph",ascending=False,ignore_index=True)

with open(degree_top10, 'w') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow("year2015") 
    for idx in range(10):
        writer2.writerow([data_sort['node'][idx], data_sort['multiDigraph'][idx]])



degree_number = path1+'2016/token_net_2016_degreeDistribution.csv'
degree_list = pd.read_csv(degree_number)
data_sort = degree_list.sort_values("multiDigraph",ascending=False,ignore_index=True)

with open(degree_top10, 'a') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow("year2016") 
    for idx in range(10):
        writer2.writerow([data_sort['node'][idx], data_sort['multiDigraph'][idx]])
        
degree_number = path1+'2017/token_net_2017_degreeDistribution.csv'
degree_list = pd.read_csv(degree_number)
data_sort = degree_list.sort_values("multiDigraph",ascending=False,ignore_index=True)

with open(degree_top10, 'a') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow("year2017") 
    for idx in range(10):
        writer2.writerow([data_sort['node'][idx], data_sort['multiDigraph'][idx]])
        
        
degree_number = path1+'2018/token_net_2018_degreeDistribution.csv'
degree_list = pd.read_csv(degree_number)
data_sort = degree_list.sort_values("multiDigraph",ascending=False,ignore_index=True)

with open(degree_top10, 'a') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow("year2018") 
    for idx in range(10):
        writer2.writerow([data_sort['node'][idx], data_sort['multiDigraph'][idx]])
        
        
degree_number = path1+'2019/token_net_2019_degreeDistribution.csv'
degree_list = pd.read_csv(degree_number)
data_sort = degree_list.sort_values("multiDigraph",ascending=False,ignore_index=True)

with open(degree_top10, 'a') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow("year2019") 
    for idx in range(10):
        writer2.writerow([data_sort['node'][idx], data_sort['multiDigraph'][idx]])