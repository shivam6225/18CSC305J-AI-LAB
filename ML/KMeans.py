import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sklearn.metrics as sm

X= np.array([3.78,2.44,1.71,1.02,0.89,3.44,4.55,3.90,5.88,4.80]).reshape(-1,1)
Y=np.array([0,0,0,0,0,1,1,1,1,1])

from sklearn.cluster import KMeans

data=list(zip(X,Y))
kmeans=KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(X,Y,c=kmeans.labels_)

correct=sum(Y==kmeans.labels_)
correct/float(Y.size)

inertias=[]

for i in range(1,10):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(X,Y)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10),inertias)
