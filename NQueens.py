N=int(input())

B=[[0]*N for _ in range(N)]

def attack(i,j):
    for k in range(N):
        if B[k][j]==1 or B[i][k]==1:
            return True
    
    for k in range(N):
        for l in range(N):
            if(k+l==i+j)or(k-l==i-j):
                if B[k][l]==1:
                    return True
    return False


def NQueen(n):
    if n==0:
        return True
    for i in range(N):
        for j in range(N):
            if(not(attack(i,j)) and B[i][j]!=1):
                B[i][j]=1
                if NQueen(n-1)==True:
                    return True
                B[i][j]=0
    return False

NQueen(N)
B
