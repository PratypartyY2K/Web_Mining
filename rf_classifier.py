#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd 
dataset = pd.read_csv('C:/Users/DELL/Downloads/6th semester/Web Mining/Lab/iris.csv')
print(dataset.head())
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values


# In[36]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[37]:


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=42) 
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


# In[42]:


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
import numpy as np
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
print(recall_score(y_test, y_pred, average='weighted'))
print(precision_score(y_test, y_pred, average='weighted'))
print(f1_score(y_test, y_pred, average='weighted'))
print(classification_report(y_test, y_pred))

