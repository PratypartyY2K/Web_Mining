#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler


# In[2]:


iris = pd.read_csv("iris.csv")
x = iris.iloc[:, [0, 1, 2, 3]].values


# In[3]:


iris.info()
iris[0:10]


# In[6]:


#Frequency distribution of species"
iris_outcome = pd.crosstab(index=iris["variety"], columns="count")      # Name the count column

iris_outcome


# In[7]:


iris_setosa=iris.loc[iris["variety"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["variety"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["variety"]=="Iris-versicolor"]


# In[13]:


sns.FacetGrid(iris,hue="variety",height=3).map(sns.distplot,"petal_length").add_legend()
sns.FacetGrid(iris,hue="variety",height=3).map(sns.distplot,"petal_width").add_legend()
sns.FacetGrid(iris,hue="variety",height=3).map(sns.distplot,"sepal_length").add_legend()
plt.show()


# In[14]:


sns.boxplot(x="variety",y="petal_length",data=iris)
plt.show()


# In[16]:


sns.set_style("whitegrid")
sns.pairplot(iris,hue="variety",height=3)
plt.show()


# In[19]:


#Finding the optimum number of clusters for k-means classification
from sklearn.cluster import KMeans
wcss = []

for i in range(1, 6):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)


# In[21]:


plt.plot(range(1, 6), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()


# In[22]:


kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)


# In[24]:


#Visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'purple', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'red', label = 'Centroids')

plt.legend()


# In[25]:


# 3d scatterplot using matplotlib

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'purple', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'red', label = 'Centroids')
plt.show()

print("19BCE0506 Pratyush Kumar")

