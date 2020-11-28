# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:53:49 2020

@author: Lettuce
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
import pandas as pd
import numpy as np 
#path1 = "C:/Users/superLin/Documents/blockchain/"
#path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/transaction/"
path1="/home/LBS_ZHAOLIN/graph_analysis/block_chain/contract/"
path2015= path1+"2015/contract_net_address_hash_2015_full.csv"
path2016= path1+"2016/contract_net_address_hash_2016_full.csv"
path2017= path1+"2017/contract_net_address_hash_2017_full.csv"
path2018= path1+"2018/contract_net_address_hash_2018_full.csv"
path2019= path1+"2019/contract_net_address_hash_2019_full.csv"


year2015=pd.read_csv(path2015, header=None, index_col=None)
year2015.columns = ['account','idx']
print("5: ", datetime.datetime.now())

year2016=pd.read_csv(path2016, header=None, index_col=None)
year2016.columns = ['account','idx']
print("6: ", datetime.datetime.now())

df3 = pd.merge(year2015, year2016, how='inner', left_on='account', right_on='account')
df3.to_csv(path1+"2015-2016-contract-accountSummary.csv", sep=',',index=False)

print("56: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''

year2017=pd.read_csv(path2017, header=None, index_col=None)
year2017.columns = ['account','idx']
print("7: ", datetime.datetime.now())

year2016=pd.read_csv(path2016, header=None, index_col=None)
year2016.columns = ['account','idx']
print("6: ", datetime.datetime.now())

df4 = pd.merge(year2016, year2017, how='inner', left_on='account', right_on='account')
df4.to_csv(path1+"2016-2017-contract-accountSummary.csv", sep=',',index=False)

print("67: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''

year2017=pd.read_csv(path2017, header=None, index_col=None)
year2017.columns = ['account','idx']
print("7: ", datetime.datetime.now())

year2018=pd.read_csv(path2018, header=None, index_col=None)
year2018.columns = ['account','idx']
print("8: ", datetime.datetime.now())

df5 = pd.merge(year2017, year2018, how='inner', left_on='account', right_on='account')
df5.to_csv(path1+"2017-2018-contract-accountSummary.csv", sep=',',index=False)

print("78: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
year2019=pd.read_csv(path2019, header=None, index_col=None)
year2019.columns = ['account','idx']
print("9: ", datetime.datetime.now())

year2018=pd.read_csv(path2018, header=None, index_col=None)
year2018.columns = ['account','idx']
print("8: ", datetime.datetime.now())

df6 = pd.merge(year2018, year2019, how='inner', left_on='account', right_on='account')
df6.to_csv(path1+"2018-2019-contract-accountSummary.csv", sep=',',index=False)

print("89: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
df7 = pd.merge(df3, df4, how='inner', left_on='account', right_on='account')
df7.to_csv(path1+"2015-2017-contract-accountSummary.csv", sep=',',index=False)

print("57: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
df8 = pd.merge(df7, df5, how='inner', left_on='account', right_on='account')
df8.to_csv(path1+"2015-2018-contract-accountSummary.csv", sep=',',index=False)

print("58: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
df9 = pd.merge(df8, df6, how='inner', left_on='account', right_on='account')
df9.to_csv(path1+"2015-2019-contract-accountSummary.csv", sep=',',index=False)
print("59: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
df10 = pd.merge(df4, df5, how='inner', left_on='account', right_on='account')
df10.to_csv(path1+"2016-2018-contract-accountSummary.csv", sep=',',index=False)
print("68: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
df11 = pd.merge(df10, df6, how='inner', left_on='account', right_on='account')
df11.to_csv(path1+"2016-2019-contract-accountSummary.csv", sep=',',index=False)
print("69: ", datetime.datetime.now())
'''------------------------------------------------------------------------'''
df12 = pd.merge(df5, df6, how='inner', left_on='account', right_on='account')
df12.to_csv(path1+"2017-2019-contract-accountSummary.csv", sep=',',index=False)
print("79: ", datetime.datetime.now())







#print(common)
#a_set = set(account2018) 
#b_set = set(account2019) 
#common = a_set.intersection(b_set)

#df = pandas.DataFrame(data={"common": list(common)})
#df.to_csv("./2018-2019-Transaction-accountSummary.csv", sep=',',index=False)
#print("4: ", datetime.datetime.now())
