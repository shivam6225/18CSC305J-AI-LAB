graph = {
    (0,0): [(4,0), (0,3)],
    (4,0): [(4,3), (0,0), (1,3)],
    (0,3): [(4,3), (0,0), (3,0)],
    (4,3): [(0,3), (4,0)],
    (1,3): [(0,3),(1,0)],
    (3,0): [(0,0),(3,3),(0,3)],
    (3,3): [(0,3),(3,0),(4,2)],
    (1,0): [(1,3),(0,1)],
    (0,1): [(4,1),(1,0)],
    (4,1): [(0,1),(2,3),(4,0)],
    (2,3): [(2,0)],
    (4,2): [(0,2)],
    (0,2):[],
    (2,0):[]
}

visited_bfs = []
queue = []


def bfs(visited_bfs, graph, node):
  visited_bfs.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s, end=" ")
    if(s==(0,2) or s==(2,0)):
        return True

    for neighbour in graph[s]:
      if neighbour not in visited_bfs:
        visited_bfs.append(neighbour)
        queue.append(neighbour)


visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)



print("BFS:", end=" ")
bfs(visited_bfs, graph, (0,0))
print('\n')
print("DFS:", end=" ")
dfs(visited, graph, (0,0))
