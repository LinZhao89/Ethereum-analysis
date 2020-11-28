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

year = "2019_"

name  = "1-3_to_4_4more_"    
# name  = "1-3_to_4_"
#name  = "2-4_to_5_"  
name  = "2-4_to_5_4more_"   
name = '3-5_to_6_4more_'
### name = '4-6_to_7_'
#name = '4-6_to_7_4more_'
name = '5-7_to_8_4more_'
### name = '6-8_to_9_'
#name = '6-8_to_9_4more_'
##name = '7-9_to_10_4more_'
name = '8-10_to_11_4more_'
name = '9-11_to_12_4more_'
#name = '10-12_to_1_'
# name = '4-6_to_next6_'
# name = '5-7_to_next7_'
# name = '3-5_to_next5_'
# name = '1-3_to_next3_'
# name = '6-8_to_next8_'
# name = '7-9_to_next9_'
# name = '8-10_to_next10_'
# name = '2-4_to_next4_'
# name = '9-11_to_next11_'
# name = '10-12_to_next12_'

path2 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/byMonth/3month_data/multilabel/"
good = pd.read_csv(path2+year+name+"matchGraph_features_more4_growth_multiG.csv", header='infer')
good['label']=1
bad = pd.read_csv(path2+year+name+"matchGraph_features_more4_growth_die_multiG1.csv", header='infer')
bad['label']=0
sample = np.random.rand(len(bad)) < 0.15
bad1= bad[sample]
bad1['label']=0
total_data = pd.concat([good, bad1],axis=0, ignore_index=True)

random_state = [i for i in range(0,20)]
count = 0
total_acc=0
for each in random_state:
    print(f' --------current state: {each}--------\n')

    X_train,X_test,y_train,y_test = train_test_split(total_data.iloc[:,0:13],total_data['label'],test_size=0.2,random_state=each,stratify=total_data['label'])
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    #print(scaler.data_max_)
    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)
    
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
    