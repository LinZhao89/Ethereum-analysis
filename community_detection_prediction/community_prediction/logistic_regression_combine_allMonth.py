
import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
import os
import igraph
from igraph import *

import pandas as pd
import csv
import sys

path2 ="D:/"
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



sample = np.random.rand(len(bad_all)) < 0.15
bad1= bad_all[sample]
bad1['label']=0
total_data = pd.concat([good_all, bad1],axis=0, ignore_index=True)

random_state = [i for i in range(20)]
count = 0
total_acc=0
for each in random_state:
    X_train,X_test,y_train,y_test = train_test_split(total_data.iloc[:,0:12],total_data['label'],test_size=0.2,random_state=each, stratify=total_data['label'])
    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)
    
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    print(scaler.data_max_)
    X_train1 = scaler.transform(X_train)
    X_test1 = scaler.transform(X_test)
    
    w = {0:1, 1:1} #{class_label: weight, class_label: weight}
    logistic_regression= LogisticRegression(class_weight='balanced')
    logistic_regression.fit(X_train1,y_train)
    
    
    important=[]
    coef =[]
    feature_import_dict={}
    feature_import_lst =[]
    '''list all training features with its importance'''
    feature_importance = logistic_regression.coef_
    
    for each in feature_importance:
        for i in each:
            feature_import_lst.append(i)
        
    for idx in range(len(feature_import_lst)):
        if feature_import_lst[idx]>0:
            feature_import_dict[ X_test.columns[idx]] = feature_import_lst[idx]
    
    sorted_important_features = sorted(feature_import_dict.items(), key=lambda kv:(kv[1],kv[0]))
    print(f' key features {sorted_important_features}')
    df2=pd.DataFrame(sorted_important_features)
    df2.columns=['properties','importance']
    df2.to_csv(path2+"logisticRegression_result.csv", mode = 'a',index=False,header=True)
    
    y_pred=logistic_regression.predict(X_test1)
    confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
    sn.heatmap(confusion_matrix, annot=True)
    
    print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
    total_acc+=metrics.accuracy_score(y_test, y_pred)
    count+=1
    plt.show()
    
    
ave_acc = total_acc/count
print('Average Accuracy: ',ave_acc)

    
with open(path2+"2018_LR_result.csv", 'a', newline='') as file1:
    writer1 = csv.writer(file1)
    writer1.writerow('accuracy: ' + str(ave_acc))
    writer1.writerow('#train: ' + str(len(X_train)))
    writer1.writerow('#test: ' + str(len(X_test)))
    writer1.writerow('#good: ' + str(len(good)))
    writer1.writerow('#bad: ' + str(len(bad)))
