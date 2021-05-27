import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = [0] + list(map(int,input().split()))
edges = []
for i in range(1,n+1):
    edges.append((0,i,arr[i]))
for i in range(1,n+1):
    if i==n: edges.append((1,i,0))
    else : edges.append((i,i+1,0))
CANT = dict()
for _ in range(m):
    v1,v2 = map(int,input().split())
    CANT[(v1,v2)]=True
parent = [i for i in range(0,n+1)]
RANK = [0]*(n+1)

def findParent(x):
    if x == parent[x]:return x
    parent[x] = findParent(parent[x])
    return parent[x]

def Union(x,y):
    x = findParent(x)
    y = findParent(y)
    if RANK[x]<RANK[y]:
        parent[x] = y
    else:
        parent[y] = x
        if RANK[x] == RANK[y]:RANK[x]+=1

edges.sort(key=lambda x : x[2])

if m<=1:
    print("YES")
    exit(0)
total = 0
edge_n = 0

for v1,v2,cost in edges:
    if (v1,v2) in CANT or (v2,v1) in CANT:
        continue
    if findParent(v1)!=findParent(v2):
        edge_n+=1
        total+=cost
        Union(v1,v2)
if total<=k and edge_n == n:print("YES")
else : print("NO")