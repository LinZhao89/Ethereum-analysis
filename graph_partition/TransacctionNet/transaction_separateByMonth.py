
"""
separate by month 

"""

import csv
import sys
import datetime
import pandas as pd
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
path1 ="D:/"
path2 = path1
year = "byMonth/2019_"
jan1 = path2+year+"jan.csv"
feb1 = path2+year+"feb.csv"
mar1 = path2+year+"mar.csv"
apr1 = path2+year+"apr.csv"
may1 = path2+year+"may.csv"
jun1 = path2+year+"jun.csv"
jul1 = path2+year+"jul.csv"
aug1 = path2+year+"aug.csv"
sep1 = path2+year+"sep.csv"
octo1 = path2+year+"oct.csv"
nov1 = path2+year+"nov.csv"
dec1 = path2+year+"dec.csv"

jan=[]
feb=[]
mar=[]
apr=[]
may=[]
jun=[]
jul=[]
aug=[]
sep=[]
octo=[]
nov=[]
dec=[]

f = path1+"transaction2019.csv"
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
print("start1: ", datetime.datetime.now())
with open(f, "r") as gFile:
    reader = csv.reader(line.replace('\0','') for line in gFile)
    # with open(path2+ "contract_net2019_bymonth.csv", "a+", newline ='') as tfile:
    #     writer = csv.writer(tfile)
    for rows in reader:
        try:
            if rows[3] != 'from_address':
                            if nodes.get(rows[3]) is None:
                                nodes.update({rows[3] : n})
                                n+=1
                            if nodes.get(rows[4]) is None:
                                nodes.update({rows[4]: n})
                                n+=1
                                
                            timestampInfo=rows[14].split('-')
                            # print(timestampInfo[1])
                            if(timestampInfo[1] in months):
                                
                                month = int(timestampInfo[1])
                                if(month==1):
                                    jan.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==2):
                                    feb.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==3):
                                    mar.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==4):
                                    apr.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==5):
                                    may.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==6):
                                    jun.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==7):
                                    jul.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==8):
                                    aug.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==9):
                                    sep.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==10):
                                    octo.append([nodes[rows[3]],nodes[rows[4]]])
                                elif(month==11):
                                    nov.append([nodes[rows[3]], nodes[rows[4]]])
                                elif(month==12):
                                    dec.append([nodes[rows[3]], nodes[rows[4]]])
                                    
                                # writer.writerow([nodes[rows[2]], nodes[rows[3]]])
                                count +=1 
        except IndexError:
            pass
        continue
           
print(f, " done")
a+=1
print("start: ", datetime.datetime.now())
xx=pd.DataFrame(jan)
xx.to_csv(jan1, index=False)
xx=pd.DataFrame(feb)
xx.to_csv(feb1, index=False)
xx=pd.DataFrame(mar)
xx.to_csv(mar1, index=False)
xx=pd.DataFrame(apr)
xx.to_csv(apr1, index=False)
xx=pd.DataFrame(may)
xx.to_csv(may1, index=False)
xx=pd.DataFrame(jun)
xx.to_csv(jun1, index=False)
xx=pd.DataFrame(jul)
xx.to_csv(jul1, index=False)
xx=pd.DataFrame(aug)
xx.to_csv(aug1, index=False)
xx=pd.DataFrame(sep)
xx.to_csv(sep1, index=False)
xx=pd.DataFrame(octo)
xx.to_csv(octo1, index=False)
xx=pd.DataFrame(nov)
xx.to_csv(nov1, index=False)
xx=pd.DataFrame(dec)
xx.to_csv(dec1, index=False)

#with open(path2+year+"transaction_net_address_hash2019_bymonth.csv", "w", newline ='') as hfile:
#    hasher = csv.writer(hfile)
#    for k,v in nodes.items():
#        hasher.writerow([k,v])

print(n)
print(count)
print(len(list(nodes.keys())))