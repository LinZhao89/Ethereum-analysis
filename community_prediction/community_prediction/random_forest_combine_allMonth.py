# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:59:28 2020

@author: zhao lin 

implement random forest algorithm for training 
"""
from sklearn.ensemble import RandomForestClassifier 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
import csv

import os
import igraph
from igraph import *

import pandas as pd
import csv
import sys
maxInt = sys.maxsize




year = "2018_"
name = 'all_'
path2 ="D:/blockchain data at sch/New folder/blockchain/submission/original/contract/byMonth/3month_data/multilabel/year2018_train_data/"
entries = os.listdir(path2+"good/")

good_all = pd.DataFrame()
for entry in entries:
    print(f'good: {entry}')
    if entry.endswith('.csv'):
        good = pd.read_csv(path2 + "good/" + entry, header = 'infer')
        good['label']=1
        good_all = good_all.append([good])

entries = os.listdir(path2+"bad/")
bad_all = pd.DataFrame()
for entry in entries:
    print(f'bad: {entry}')
    if entry.endswith('.csv'):
        bad = pd.read_csv(path2 + "bad/" + entry, header = 'infer')
        bad['label']=0
        bad_all = bad_all.append([bad])


good_all.to_csv(path2+"good_all_data_summary.csv", index = False, header = True)
bad_all.to_csv(path2+"bad_all_data_summary.csv", index = False, header = True)

sample = np.random.rand(len(bad_all)) < 0.16
bad1= bad_all[sample]
bad1['label']=0
total_data = pd.concat([good_all, bad1],axis=0, ignore_index=True)

random_state = [i for i in range(0,20)]
count = 0
total_acc=0
for each in random_state:
    print(f' --------current state: {each}--------\n')

    X_train,X_test,y_train,y_test = train_test_split(total_data.iloc[:,0:13],total_data['label'],test_size=0.2,random_state=each,stratify=total_data['label'])
    # scaler = MinMaxScaler()
    # scaler.fit(X_train)
    #print(scaler.data_max_)
    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)
    
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    X_train1 = scaler.transform(X_train)
    X_test1 = scaler.transform(X_test)
    
    w = {0:1, 1:1} #{class_label: weight, class_label: weight}
    rf = RandomForestClassifier(n_estimators=100,max_features='auto',criterion='entropy',max_depth=None,min_samples_leaf=1, class_weight=w)
    # rf = RandomForestClassifier()
    rf.fit(X_train1,y_train)
    
    score = rf.score(X_test1, y_test)
    feature_importances = pd.DataFrame(rf.feature_importances_, index = X_train.columns, columns = ['importance']).sort_values('importance', ascending=False)
    df2=pd.DataFrame(feature_importances)
    # df2.columns=['properties','importance']
    df2.to_csv(path2+year+name+"RF_result.csv",mode='a', index=True,header=True)
    print(f'score: {score}')
    print(f'feature_importance {feature_importances}')
    
    y_pred = rf.predict(X_test1)
    confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
    sn.heatmap(confusion_matrix, annot=True)

    total_acc+=score
    count+=1
    plt.show()
    
    
ave_acc = total_acc/count
print('Average Accuracy: ',ave_acc)

# df2=pd.DataFrame(feature_importances)
# # df2.columns=['properties','importance']
# df2.to_csv(path2+name+"RF_result.csv", index=True,header=True)

with open(path2+year+name+"RF_result.csv", 'a', newline='') as file1:
    writer1 = csv.writer(file1)
    writer1.writerow('accuracy: ' + str(ave_acc))
    writer1.writerow('#train: ' + str(len(X_train)))
    writer1.writerow('#test: ' + str(len(X_test)))
    writer1.writerow('#good: ' + str(len(good)))
    writer1.writerow('#bad: ' + str(len(bad)))
    