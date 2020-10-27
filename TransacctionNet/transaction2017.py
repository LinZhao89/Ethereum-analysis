# -*- coding: utf-8 -*-

#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```transaction_net_address_hash.csv: (address, hashID)                                   #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```transaction_net.csv: (hashed_from_address, hashed_to_address)                         #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.transactions`                    #
#*****************************************************************************************#

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
        
path ="/transaction/"
g = path+"transactions2017.csv"

nodes = {}
n = 0
count= 0

with open(g, "r") as gFile:
    with open(path+"transaction_net_address_hash_2017.csv", "w", newline ='') as hfile:
        with open(path+"transaction_net_2017.csv", "w",  newline ='') as tfile:
            reader = csv.reader(gFile)
            hasher = csv.writer(hfile)
            writer = csv.writer(tfile)

            for rows in reader:
                if rows[3] != 'from_address':
                    if nodes.get(rows[3]) is None:
                        nodes.update({rows[3] : n})
                        n+=1
                    if nodes.get(rows[4]) is None:
                        nodes.update({rows[4]: n})
                        n+=1
                        
                    writer.writerow([nodes[rows[3]], nodes[rows[4]]])
                    count +=1

            for k,v in nodes.items():
                hasher.writerow([k,v])
            print(n)
            print(count)
            print(len(list(nodes.keys())))