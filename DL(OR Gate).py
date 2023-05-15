import numpy as np
import pandas as pd

def activation(z):
    if z>=0:
        Y=1
    else:
        Y=-1
    return Y

X= np.array([[-1,-1],[-1,1],[1,-1],[1,1]])
# Weights and bias
W=np.array([0.8,0.5])
b=0.1

T=np.array([-1,1,1,1])
a=1 #learningRate

T_vector=[-1,1,1,1]
Y_vector=[]
i=0

while True:
    print("EPOCH: ",i)
   
    Data=[]
    for j in range(0,len(X)):
        aggregation=(np.dot(W,X[j].T))+b
       
        Y=activation(aggregation)
        Y_vector.append(Y)
        if Y != T[j] :
            deltaW=a*X[j]*T[j]
            W=W+deltaW
            b=b+a*T[j]
        else:
            deltaW=[0,0]
       
        Data.append([X[j][0],X[j][1],T[j],round(aggregation,2),Y,W[0],W[1],round(b,2),deltaW[0],deltaW[1],a*T[j]])
   
    Final_Data= pd.DataFrame(Data,columns=['X1', 'X2', 'T', 'yin', 'Y', 'W1', 'W2', 'b', 'delW1', 'delW2', 'delb'])
    print(Final_Data)   
    print("------------------------------------------------------------")
    i=i+1
    if Y_vector == T_vector:
        break
    Y_vector=[]
