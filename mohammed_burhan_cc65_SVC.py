# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:19:36 2018

@author: Lenovo
"""

import pandas as pd
import numpy as np

data=pd.read_csv("breast_cancer.csv")


data=data.drop("A",axis=1)
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputeer=imputer.fit(data)
data=imputer.transform(data)


features=np.delete(data,9,1)
labels=data[:,9]
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.svm import SVC
svc=SVC(kernel='rbf',random_state=0)
svc.fit(features_train,labels_train)

labels_predict=svc.predict(features_test)
score=svc.score(features_test,labels_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_predict)

prediction_of_tumor=svc.predict([6,2,5,3,2,7,9,2,4])


for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])
    
features=data.drop("K",axis=1)
labels=data["K"].values

features=features.values

