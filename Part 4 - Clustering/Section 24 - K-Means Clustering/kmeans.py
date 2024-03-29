# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:13:25 2019

@author: Lucky
"""
#K-Mean Clustering

#Imporint ibraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing datasets
datasets = pd.read_csv('Mall_Customers.csv')
X = datasets.iloc[:, [3, 4] ].values

#Using Elbow method to find optimal value of K(Clusters)
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300,n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('K')
plt.ylabel('wcss')
plt.show()

#Apllying Kmean to the mall dataset
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300,n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

#Visualising the clusters
plt.scatter(X[y_kmeans==0, 0], X[y_kmeans==0, 1] ,s=100, c='red', label='Carefull' )
plt.scatter(X[y_kmeans==1, 0],X[y_kmeans==1, 1] , s=100, c='blue', label='Standard' )
plt.scatter(X[y_kmeans==2, 0],X[y_kmeans==2, 1] , s=100, c='green', label='Target')
plt.scatter(X[y_kmeans==3, 0],X[y_kmeans==3, 1] , s=100, c='cyan', label='Careless')
plt.scatter(X[y_kmeans==4, 0],X[y_kmeans==4, 1] , s=100, c='magenta', label='Sensible')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',label='Cluster_Centroid')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()