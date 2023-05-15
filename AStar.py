from queue import PriorityQueue

v=7

graph=[[] for i in range(v)]

def a_star(s,t,n):
    visited=[False]*(n+1)
    pq=PriorityQueue()
    pq.put((0,s))
    visited[s]=True
    while pq.empty()==False:
        c,u=pq.get()
        print(u,'cost: ',c)
        if u==t:
            break
            
        for v,c in graph[u]:
            if visited[v]==False:
                pq.put((c,v))
                visited[v]=True

def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
    
addedge(1,2,6+1)
addedge(1,4,5+2)
addedge(2,3,12+2+1)
addedge(2,5,15+3+1)
addedge(4,6,7+2+4)
a_star(1,6,7)
