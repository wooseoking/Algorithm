n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

edges = []

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if i < j:
            edges.append([i,j,row[j]])

for i in range(n):
    edges.append([i,n,a[i]])

#mst
rank = [0]*(n + 1)
parent = [i for i in range(n + 1)]

def findParent(x,parent):
    if parent[x] == x: return x
    parent[x] = findParent(parent[x],parent)
    return parent[x]

def union(x,y):
    x = findParent(x,parent)
    y = findParent(y,parent)

    if x == y:return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def mst(edges):
    edges.sort(key = lambda l:l[2])
    cost = 0
    graph = []
    for x,y,c in edges:
        if findParent(x,parent) != findParent(y,parent):
            cost += c
            union(x,y)
            graph.append([x,y,c])
    return cost

ans = mst(edges)
print(ans)