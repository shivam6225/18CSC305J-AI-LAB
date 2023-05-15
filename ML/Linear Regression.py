import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sklearn.metrics as sm

X= np.array([3.78,2.44,1.71,1.02,0.89,3.44,4.55,3.90,5.88,4.80]).reshape(-1,1)
Y=np.array([0,0,0,0,0,1,1,1,1,1])

lm=LinearRegression()
lm.fit(X,Y)


y_predict=lm.predict(X)
y_predict

sm.r2_score(Y,y_predict)

