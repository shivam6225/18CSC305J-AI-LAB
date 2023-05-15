MAX,MIN = 1000,-1000

def minmax(depth,nIndex,maximize,values,alpha,beta):
    
    if depth==3:
        return values[nIndex]
    
    if maximize:
        best=MIN
        
        for i in range(0,2):
            val=minmax(depth+1,nIndex*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            
            if beta<=alpha:
                break
        return best
    
    else:
        best=MAX
        
        for i in range(0,2):
            val=minmax(depth+1,nIndex*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            
            if beta<=alpha:
                break
                
        return best

values=[]
for i in range(0,8):
    x=int(input(f"Enter nodes {i}: "))
    values.append(x)
    
    
print("Optimal value is :", minmax(3,0,True,values,MIN,MAX))
