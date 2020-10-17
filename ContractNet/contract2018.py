# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 00:22:01 2020

"""

#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```contract_net_address_hash.csv: (address, hashID)                                      #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```contract_net.csv: (hashed_from_address, hashed_to_address)                            #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.traces`                          #
#```taken from `bigquery-public-data.ethereum_blockchain.contracts`                       #
#*****************************************************************************************#

import csv
import sys
import datetime
maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
print("start: ", datetime.datetime.now())
#csv.field_size_limit(sys.maxsize)


a = 0
nodes = {}
contracts = {}
n = 0
count= 0
path1 ="E:/trace/"
path2 ="E:/contract/"

with open(path2+"contracts2015.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})
                
with open(path2+"contracts2016.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})

with open(path2+"contracts2017.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})
                
with open(path2+"contracts2018.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})   
    
# with open(path2+"contract2019_consolidate.csv", "r") as cFile:
#         reader = csv.reader(cFile)
#         for rows in reader:
#             if rows[0] != 'address':
#                 contracts.update({rows[0]: "sc"})   
        
#['transaction_hash', 'transaction_index', 'from_address', 'to_address', 'value', 'input', 'output', 'contract_type', 'call_type', 'reward_type', 'gas', 'gas_used', 'subcontracts', 'contract_address', 'error', 'status', 'block_timestamp', 'block_number', 'block_hash']
f = path1+"trace2018.csv"
print("start: ", datetime.datetime.now())
with open(f, "r") as gFile:
    reader = csv.reader(line.replace('\0','') for line in gFile)
    with open(path2+ "contract_net2018.csv", "a+", newline ='') as tfile:
        writer = csv.writer(tfile)
        for rows in reader:
            try:
                if rows[2] != 'from_address':
                    # row[15]is status
                    if rows[15] == '1':
                        if ((rows[2] != '') and (rows[3] != '')):
                            if ((contracts.get(rows[2]) is not None) and ((contracts.get(rows[3])) is not None)):
                                if nodes.get(rows[2]) is None:
                                    nodes.update({rows[2] : n})
                                    n+=1
                                if nodes.get(rows[3]) is None:
                                    nodes.update({rows[3]: n})
                                    n+=1
    
                                writer.writerow([nodes[rows[2]], nodes[rows[3]]])
                                count +=1 
            except IndexError:
                pass
            continue
print(f, " done")
a+=1
with open(path2+"contract_net_address_hash2018.csv", "w", newline ='') as hfile:
    hasher = csv.writer(hfile)
    for k,v in nodes.items():
        hasher.writerow([k,v])

print(n)
print(count)
print(len(list(nodes.keys())))
