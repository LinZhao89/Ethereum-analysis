# -*- coding: utf-8 -*-


#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```token_net_address_hash.csv: (address, hashID)                                         #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```token_net.csv: (hashed_from_address, hashed_to_address)                               #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.token_transfers`                 #
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
path ="/token transfer/"
g =path+ 'token_trf_2017.csv'

nodes = {}
n = 0
count= 0

with open(g, "r") as gFile:
    with open(path+"token_net_address_hash_2017.csv", "w", newline ='') as hfile:
        with open(path+"token_net_2017.csv", "w",  newline ='') as tfile:
            reader = csv.reader(gFile)
            hasher = csv.writer(hfile)
            writer = csv.writer(tfile)

            for rows in reader:
                if rows[1] != 'from_address':
                    if nodes.get(rows[1]) is None:
                        nodes.update({rows[1] : n})
                        n+=1
                    if nodes.get(rows[2]) is None:
                        nodes.update({rows[2]: n})
                        n+=1
                        
                    writer.writerow([nodes[rows[1]], nodes[rows[2]]])
                    count +=1

            for k,v in nodes.items():
                hasher.writerow([k,v])
            print(n)
            print(count)
            print(len(list(nodes.keys())))