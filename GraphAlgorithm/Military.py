import sys
input = sys.stdin.readline
n,m = map(int,input().split())
c,d = map(int,input().split())
edges = []
for _ in range(m):
    v1,v2,cost = map(int,input().split())
    edges.append((v1,v2,cost))
edges.sort(key= lambda x : x[2],reverse=True)

parent = [i for i in range(n)]
rank = [0 for i in range(n)]

def findParent(x):
    if x==parent[x]:return x
    parent[x] = findParent(parent[x])
    return parent[x]

def union(x,y):
    x = findParent(x)
    y = findParent(y)
    if x==y:return
    if rank[x]<rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x]==rank[y]:rank[x]+=1

def cycle(x,y):
    x = findParent(x)
    y = findParent(y)
    return x==y

res = []
for v1,v2,cost in edges:
    if cycle(c,d):break
    if not cycle(v1,v2):
        res.append(cost)
        union(v1,v2)
print(min(res))