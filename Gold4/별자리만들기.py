import math

n = int(input())
points = []
for _ in range(n):
    v1,v2 = map(float,input().split())
    points.append((v1,v2))

rank = [0]*n
parent = [i for i in range(n)]
graph = [[]for _ in range(n)]
edges = []
for i in range(n-1):
    for j in range(i+1,n):
        v1,v2 = points[i]
        v3,v4 = points[j]
        dist = math.sqrt((v1-v3)**2 + (v2-v4)**2)
        dist = round(dist,2)
        edges.append((i,j,dist))

def getParent(x):
    if x==parent[x]:return x
    parent[x] = getParent(parent[x])
    return parent[x]

def union(x,y):
    x = getParent(x)
    y = getParent(y)
    if x==y:return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x]==rank[y]:rank[x]+=1

edges.sort(key=lambda l:l[2])
ans = 0
for v1,v2,cost in edges:
    if getParent(v1)!=getParent(v2):
        union(v1,v2)
        ans+=cost
print(ans)