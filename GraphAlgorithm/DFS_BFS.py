import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n,m,s = map(int,input().split())

a = [[] for _ in range(n+1)]

for _ in range(m):
    v1,v2 = map(int,input().split())
    a[v1].append(v2)
    a[v2].append(v1)

for i in range(1,n+1):
    a[i].sort()

visited = [False]*(n+1)

def DFS(a,node,visited):
    if visited[node]:
        return
    print(node,end = ' ')
    visited[node] = True
    for next in a[node]:
        DFS(a,next,visited)

DFS(a,s,visited)
print()

def BFS(a,node):
    visited = [False]*(n+1)
    q = deque()
    visited[node] = True
    q.append(node)
    while q:
        now = q.popleft()
        print(now,end=' ')
        for y in a[now]:
            if not visited[y]:
                visited[y] = True
                q.append(y)

BFS(a,s)