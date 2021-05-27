import sys
import heapq
input = sys.stdin.readline
n , m = map(int,input().split())
RANK = [0]*(n+1)
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

def findParent(x):
    if x == parent[x]:return x
    parent[x] = findParent(parent[x])
    return parent[x]


def Union(x,y):
    x = findParent(x)
    y = findParent(y)
    if x==y:return

    if RANK[x] < RANK[y]:
        parent[x] = y
    else:
        parent[y] = x
        if RANK[x]==RANK[y]:RANK[x]+=1

edges = []
for _ in range(m):
    v1,v2,cost =map(int,input().split())
    edges.append((v1,v2,cost))
edges.sort(key= lambda x : x[2])
ans = []


for v1,v2,cost in edges:
    if findParent(v1) != findParent(v2):
        ans.append(cost)
        Union(v1,v2)

ans.pop(-1)
print(sum(ans))