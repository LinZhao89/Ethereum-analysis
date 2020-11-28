# -*- coding: utf-8 -*-

#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```trace_net_address_hash.csv: (address, hashID)                                         #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```trace_net.csv: (hashed_from_address, hashed_to_address)                               #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.traces`                          #   
#*****************************************************************************************#

import csv
import sys
import datetime

print("start: ", datetime.datetime.now())

a = 0
nodes = {}
n = 0
count= 0

maxInt = sys.maxsize
import datetime
print("start: ", datetime.datetime.now())
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
path ="E:/trace/"
g =path+ 'trace2017.csv' 
  
#['transaction_hash', 'transaction_index', 'from_address', 'to_address', 'value', 'input', 'output', 'trace_type', 'call_type', 'reward_type', 'gas', 'gas_used', 'subtraces', 'trace_address', 'error', 'status', 'block_timestamp', 'block_number', 'block_hash']

with open(g, "r") as gFile:
    #reader = csv.reader(gFile)
    reader = csv.reader( (line.replace('\0','') for line in gFile) )
    with open(path+"trace_net_2017.csv", "a+", newline ='') as tfile:
        writer = csv.writer(tfile)
        for rows in reader:
            try:
                if rows[2] != 'from_address':
                    #print(rows[15])
                    if(rows[15]=='1'):
                    #if int(rows[15]) == 1:
                        if ((rows[2] != '') and (rows[3] != '')):
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

with open(path+"trace_net_address_hash_2017.csv", "w", newline ='') as hfile:
    hasher = csv.writer(hfile)
    for k,v in nodes.items():
        hasher.writerow([k,v])

print(n)
print(count)
print(len(list(nodes.keys())))