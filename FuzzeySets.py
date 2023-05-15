A=dict()
B=dict()
Y=dict()
X=dict()

A={'a':0.9,'b':0.4,'c':0.5}
B={'a':0.7,'b':0.6,'c':0.2}

print('Fuzzy Set A:',A)
print('Fuzzy Set B:',B)

for A_key,B_key in zip(A,B):
    Av=A[A_key]
    Bv=B[B_key]
    
    if Av>Bv:
        Y[A_key]=Av
        X[B_key]=Bv
    else:
        X[A_key]=Av
        Y[B_key]=Bv

print('Union Fuzzy Set Y:',Y)
print('Intersetion Fuzzy Set X:',X)
