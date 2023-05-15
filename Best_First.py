from queue import PriorityQueue
v=7
graph=[[] for i in range(v)]

def best_first_search(source,target,n):
    visited =[False]*n
    pq=PriorityQueue()
    pq.put((0,source))
    visited[source]=True
    while pq.empty()==False:
        c,u=pq.get()
        print(u,'cost:',c)
        if u==target:
            break
        
        for v,c in graph[u]:
            if visited[v]==False:
                visited[v]=True
                pq.put((c,v))
    print()
                
def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
    
addedge(1,2,6)
addedge(1,4,5)
addedge(2,3,12)
addedge(2,5,15)
addedge(4,6,7)

best_first_search(1,6,7)
        
