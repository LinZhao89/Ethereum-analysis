# -*- coding: utf-8 -*-
"""
Created on Fri May 29 00:58:42 2020
to count how many edges are same, delete by years 

!!!!!!for contract net only!!!!!!!!

1. take in common node and their hash in 2 year 
2. the common account id must appear in both start and end position, then they can be candidates for common edge 
3. do merge/ join 

"""

import csv
import sys
import datetime
import pandas as pd

maxInt = sys.maxsize
print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
import numpy as np 
#path1 = "C:/Users/superLin/Documents/blockchain/"
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/"
path1="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/"

path56= path1+"commonAccountSummary_new/2015-2016-contract-accountSummary.csv"
path67= path1+"commonAccountSummary_new/2016-2017-contract-accountSummary.csv"
path78= path1+"commonAccountSummary_new/2017-2018-contract-accountSummary.csv"
path89= path1+"commonAccountSummary_new/2018-2019-contract-accountSummary.csv"

path2015= path1+"2015/contract_net_2015_full.csv"
path2016= path1+"2016/contract_net_2016_full.csv"
path2017= path1+"2017/contract_net_2017_full.csv"
path2018= path1+"2018/contract_net_2018_full.csv"
path2019= path1+"2019/contract_net_2019_full.csv"

hash2015= path1+"2015/contract_net_address_hash_2015_full.csv"
hash2016= path1+"2016/contract_net_address_hash_2016_full.csv"
hash2017= path1+"2017/contract_net_address_hash_2017_full.csv"
hash2018= path1+"2018/contract_net_address_hash_2018_full.csv"
hash2019= path1+"2019/contract_net_address_hash_2019_full.csv"

###############################################################################

edge15 = pd.read_csv(path2015, index_col=None, low_memory=True)
edge15.columns = ['startIdx','endIdx']
edge16 = pd.read_csv(path2016, index_col=None, low_memory=True)
edge16.columns = ['startIdx','endIdx']
edge17 = pd.read_csv(path2017, index_col=None, low_memory=True)
edge17.columns = ['startIdx','endIdx']
edge18 = pd.read_csv(path2018, index_col=None, low_memory=True)
edge18.columns = ['startIdx','endIdx']
edge19 = pd.read_csv(path2019, index_col=None, low_memory=True)
edge19.columns = ['startIdx','endIdx']

hash15 = pd.read_csv(hash2015, index_col=None, low_memory=True)
hash15.columns = ['acc','idx']
hash16 = pd.read_csv(hash2016, index_col=None, low_memory=True)
hash16.columns = ['acc','idx']
hash17 = pd.read_csv(hash2017, index_col=None, low_memory=True)
hash17.columns = ['acc','idx']
hash18 = pd.read_csv(hash2018, index_col=None, low_memory=True)
hash18.columns = ['acc','idx']
hash19 = pd.read_csv(hash2019, index_col=None, low_memory=True)
hash19.columns = ['acc','idx']

#####################################################################
c56 = pd.read_csv(path56, header="infer",index_col=None, low_memory=True)
c56_list =c56['idx_x'].values.tolist()
edge15_isin = edge15.isin(c56_list)
edge15_isin.columns = ['startTF','endTF']
edge15_isin = pd.concat([edge15_isin,edge15], axis=1)
edge15_common = edge15_isin.drop(edge15_isin[edge15_isin['startTF'] ==False].index)
edge15_common = edge15_common.drop(edge15_common[edge15_common['endTF'] ==False].index)
 
c56_list =c56['idx_y'].values.tolist()
edge16_isin = edge16.isin(c56_list)
edge16_isin.columns = ['startTF','endTF']
edge16_isin = pd.concat([edge16_isin,edge16], axis=1)
edge16_common = edge16_isin.drop(edge16_isin[edge16_isin['startTF'] ==False].index)
edge16_common = edge16_common.drop(edge16_common[edge16_common['endTF'] ==False].index)

edge15_acc1 = []
edge15_acc2 = []
for each in edge15_common['startIdx']:
    edge15_acc1.append(hash15.iloc[each-1,0])
for each in edge15_common['endIdx']:
    edge15_acc2.append(hash15.iloc[each-1,0])
    
edge15_acc3 =pd.DataFrame(edge15_acc1)
edge15_acc4 =pd.DataFrame(edge15_acc2)
edge15_acc = pd.concat([edge15_acc3,edge15_acc4], axis=1)
edge15_acc.columns = ['start','end']

edge16_acc1 = []
edge16_acc2 = []
for each in edge16_common['startIdx']:
    edge16_acc1.append(hash16.iloc[each-1,0])
for each in edge16_common['endIdx']:
    edge16_acc2.append(hash16.iloc[each-1,0])
    
edge16_acc3 =pd.DataFrame(edge16_acc1)
edge16_acc4 =pd.DataFrame(edge16_acc2)
edge16_acc = pd.concat([edge16_acc3,edge16_acc4], axis=1)
edge16_acc.columns = ['start','end']

edge15_acc =edge15_acc.drop_duplicates()
edge15_acc['combine'] = edge15_acc['start']+ "-" +  edge15_acc['end']
edge16_acc =edge16_acc.drop_duplicates()
edge16_acc['combine'] = edge16_acc['start']+ "-" +  edge16_acc['end']

df1 = pd.merge(edge15_acc, edge16_acc, how='inner', left_on='combine', right_on='combine')
df1.to_csv(path1+"2015-2016-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("56: ", datetime.datetime.now())
###############################################################################
#####################################################################
c67 = pd.read_csv(path67, header="infer",index_col=None, low_memory=True)
c67_list =c67['idx_x'].values.tolist()
edge16_isin = edge16.isin(c67_list)
edge16_isin.columns = ['startTF','endTF']
edge16_isin = pd.concat([edge16_isin,edge16], axis=1)
edge16_common = edge16_isin.drop(edge16_isin[edge16_isin['startTF'] ==False].index)
edge16_common = edge16_common.drop(edge16_common[edge16_common['endTF'] ==False].index)
 
c67_list =c67['idx_y'].values.tolist()
edge17_isin = edge17.isin(c67_list)
edge17_isin.columns = ['startTF','endTF']
edge17_isin = pd.concat([edge17_isin,edge17], axis=1)
edge17_common = edge17_isin.drop(edge17_isin[edge17_isin['startTF'] ==False].index)
edge17_common = edge17_common.drop(edge17_common[edge17_common['endTF'] ==False].index)

edge16_acc1 = []
edge16_acc2 = []
for each in edge16_common['startIdx']:
    edge16_acc1.append(hash16.iloc[each-1,0])
for each in edge16_common['endIdx']:
    edge16_acc2.append(hash16.iloc[each-1,0])
    
edge16_acc3 =pd.DataFrame(edge16_acc1)
edge16_acc4 =pd.DataFrame(edge16_acc2)
edge16_acc = pd.concat([edge16_acc3,edge16_acc4], axis=1)
edge16_acc.columns = ['start','end']

edge17_acc1 = []
edge17_acc2 = []
for each in edge17_common['startIdx']:
    edge17_acc1.append(hash17.iloc[each-1,0])
for each in edge17_common['endIdx']:
    edge17_acc2.append(hash17.iloc[each-1,0])
    
edge17_acc3 =pd.DataFrame(edge17_acc1)
edge17_acc4 =pd.DataFrame(edge17_acc2)
edge17_acc = pd.concat([edge17_acc3,edge17_acc4], axis=1)
edge17_acc.columns = ['start','end']

edge16_acc =edge16_acc.drop_duplicates()
edge16_acc['combine'] = edge16_acc['start']+ "-" +  edge16_acc['end']
edge17_acc =edge17_acc.drop_duplicates()
edge17_acc['combine'] = edge17_acc['start']+ "-" +  edge17_acc['end']

df2 = pd.merge(edge16_acc, edge17_acc, how='inner', left_on='combine', right_on='combine')
df2.to_csv(path1+"2016-2017-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("67: ", datetime.datetime.now())
###############################################################################
 #####################################################################
c78 = pd.read_csv(path78, header="infer",index_col=None, low_memory=True)
c78_list =c78['idx_x'].values.tolist()
edge17_isin = edge17.isin(c78_list)
edge17_isin.columns = ['startTF','endTF']
edge17_isin = pd.concat([edge17_isin,edge17], axis=1)
edge17_common = edge17_isin.drop(edge17_isin[edge17_isin['startTF'] ==False].index)
edge17_common = edge17_common.drop(edge17_common[edge17_common['endTF'] ==False].index)
 
c78_list =c78['idx_y'].values.tolist()
edge18_isin = edge18.isin(c78_list)
edge18_isin.columns = ['startTF','endTF']
edge18_isin = pd.concat([edge18_isin,edge18], axis=1)
edge18_common = edge18_isin.drop(edge18_isin[edge18_isin['startTF'] ==False].index)
edge18_common = edge18_common.drop(edge18_common[edge18_common['endTF'] ==False].index)

edge17_acc1 = []
edge17_acc2 = []
for each in edge17_common['startIdx']:
    edge17_acc1.append(hash17.iloc[each-1,0])
for each in edge17_common['endIdx']:
    edge17_acc2.append(hash17.iloc[each-1,0])
    
edge17_acc3 =pd.DataFrame(edge17_acc1)
edge17_acc4 =pd.DataFrame(edge17_acc2)
edge17_acc = pd.concat([edge17_acc3,edge17_acc4], axis=1)
edge17_acc.columns = ['start','end']

edge18_acc1 = []
edge18_acc2 = []
for each in edge18_common['startIdx']:
    edge18_acc1.append(hash18.iloc[each-1,0])
for each in edge18_common['endIdx']:
    edge18_acc2.append(hash18.iloc[each-1,0])
    
edge18_acc3 =pd.DataFrame(edge18_acc1)
edge18_acc4 =pd.DataFrame(edge18_acc2)
edge18_acc = pd.concat([edge18_acc3,edge18_acc4], axis=1)
edge18_acc.columns = ['start','end']

edge17_acc =edge17_acc.drop_duplicates()
edge17_acc['combine'] = edge17_acc['start']+ "-" +  edge17_acc['end']
edge18_acc =edge18_acc.drop_duplicates()
edge18_acc['combine'] = edge18_acc['start']+ "-" +  edge18_acc['end']

df3 = pd.merge(edge17_acc, edge18_acc, how='inner', left_on='combine', right_on='combine')
df3.to_csv(path1+"2017-2018-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("78: ", datetime.datetime.now())
###############################################################################
 #####################################################################
c89 = pd.read_csv(path89, header="infer",index_col=None, low_memory=True)
c89_list =c89['idx_x'].values.tolist()
edge18_isin = edge18.isin(c89_list)
edge18_isin.columns = ['startTF','endTF']
edge18_isin = pd.concat([edge18_isin,edge18], axis=1)
edge18_common = edge18_isin.drop(edge18_isin[edge18_isin['startTF'] ==False].index)
edge18_common = edge18_common.drop(edge18_common[edge18_common['endTF'] ==False].index)
 
c89_list =c89['idx_y'].values.tolist()
edge19_isin = edge19.isin(c89_list)
edge19_isin.columns = ['startTF','endTF']
edge19_isin = pd.concat([edge19_isin,edge19], axis=1)
edge19_common = edge19_isin.drop(edge19_isin[edge19_isin['startTF'] ==False].index)
edge19_common = edge19_common.drop(edge19_common[edge19_common['endTF'] ==False].index)

edge18_acc1 = []
edge18_acc2 = []
for each in edge18_common['startIdx']:
    edge18_acc1.append(hash18.iloc[each-1,0])
for each in edge18_common['endIdx']:
    edge18_acc2.append(hash18.iloc[each-1,0])
    
edge18_acc3 =pd.DataFrame(edge18_acc1)
edge18_acc4 =pd.DataFrame(edge18_acc2)
edge18_acc = pd.concat([edge18_acc3,edge18_acc4], axis=1)
edge18_acc.columns = ['start','end']

edge19_acc1 = []
edge19_acc2 = []
for each in edge19_common['startIdx']:
    edge19_acc1.append(hash19.iloc[each-1,0])
for each in edge19_common['endIdx']:
    edge19_acc2.append(hash19.iloc[each-1,0])
    
edge19_acc3 =pd.DataFrame(edge19_acc1)
edge19_acc4 =pd.DataFrame(edge19_acc2)
edge19_acc = pd.concat([edge19_acc3,edge19_acc4], axis=1)
edge19_acc.columns = ['start','end']

edge18_acc =edge18_acc.drop_duplicates()
edge18_acc['combine'] = edge18_acc['start']+ "-" +  edge18_acc['end']
edge19_acc =edge19_acc.drop_duplicates()
edge19_acc['combine'] = edge19_acc['start']+ "-" +  edge19_acc['end']

df4 = pd.merge(edge18_acc, edge19_acc, how='inner', left_on='combine', right_on='combine')
df4.to_csv(path1+"2018-2019-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("89: ", datetime.datetime.now())
###############################################################################
 
df5 = pd.merge(df1, df2, how='inner', left_on='combine', right_on='combine')
df5.to_csv(path1+"2015-2017-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("57: ", datetime.datetime.now())

df6 = pd.merge(df5, df3, how='inner', left_on='combine', right_on='combine')
df6.to_csv(path1+"2015-2018-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("58: ", datetime.datetime.now())

df6 = pd.merge(df6, df4, how='inner', left_on='combine', right_on='combine')
df6.to_csv(path1+"2015-2019-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("59: ", datetime.datetime.now())

df7 = pd.merge(df3, df4, how='inner', left_on='combine', right_on='combine')
df7.to_csv(path1+"2017-2019-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("79: ", datetime.datetime.now())

df7 = pd.merge(df2, df7, how='inner', left_on='combine', right_on='combine')
df7.to_csv(path1+"2016-2019-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("69: ", datetime.datetime.now())

df8 = pd.merge(df2, df3, how='inner', left_on='combine', right_on='combine')
df8.to_csv(path1+"2016-2018-contract-simpleDirected_commonEdge.csv", sep=',',index=False)
print("68: ", datetime.datetime.now())





