
import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

year = "2018_"
name  = "1-3_to_4_4more_"    
name  = "2-4_to_5_4more_"    
name = '3-5_to_6_4more_'
name = '4-6_to_7_4more_' 
name = '5-7_to_8_4more_'
name = '6-8_to_9_4more_'
name = '7-9_to_10_4more_'
name = '8-10_to_11_4more_'
# name = '9-11_to_12_4more_'



path2 ="D:/"
good = pd.read_csv(path2+"year2018_train_data/good/"+year+name+"matchGraph_features_more4_growth_multiG.csv", header='infer')
good['label']=1
bad = pd.read_csv(path2+"year2018_train_data/bad/" +year+name+"matchGraph_features_more4_growth_die_multiG1.csv", header='infer')
sample = np.random.rand(len(bad)) < 0.17
bad1= bad[sample]
bad1['label']=0
total_data = pd.concat([good, bad1],axis=0, ignore_index=True)

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
    
    # print(X_data.isnull().any())
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
    df2.to_csv(path2+year+name+"logisticRegression_result.csv", mode = 'a',index=False,header=True)
#    xxx= sorted(feature_import_dict.values())
    
    y_pred=logistic_regression.predict(X_test1)
    confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
    sn.heatmap(confusion_matrix, annot=True)
    
    print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
    total_acc+=metrics.accuracy_score(y_test, y_pred)
    count+=1
    plt.show()
    
    
ave_acc = total_acc/count
print('Average Accuracy: ',ave_acc)


# with open(path2+name+"logisticRegression_result.csv", 'a', newline='') as file1:
#     writer1 = csv.writer(file1)
#     writer1.writerow('accuracy: ' + str(ave_acc))
    
with open(path2+year+name+"logisticRegression_result_gg.csv", 'a', newline='') as file1:
    writer1 = csv.writer(file1)
    writer1.writerow('accuracy: ' + str(ave_acc))
    writer1.writerow('#train: ' + str(len(X_train)))
    writer1.writerow('#test: ' + str(len(X_test)))
    writer1.writerow('#good: ' + str(len(good)))
    writer1.writerow('#bad: ' + str(len(bad)))