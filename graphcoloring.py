colors=[i for i in range(1,4)]

nodes=['A','B','C','D','E']

neighbours={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['B','E'],
    'E':['C','D'],
}

sc={}
def promising(node,color):
    for neighbour in neighbours.get(node):
        cn=sc.get(neighbour)
        if color==cn:
            return False
    return True

for node in nodes:
    for color in colors:
        if(promising(node,color)):
            sc[node]=color

print(sc)
        
