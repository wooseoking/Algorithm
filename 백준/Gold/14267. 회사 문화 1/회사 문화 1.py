import sys
sys.setrecursionlimit(10**8)
# input
n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
parent = list(map(int,input().split()))
compliments = [0]*(n + 1)
d = [0]*(n + 1)

for _ in range(m):
    x,y = map(int,input().split())
    compliments[x] += y

for i in range(n):
    parentNode = parent[i]
    if parentNode == -1:continue
    graph[parentNode].append(i + 1)

visited = [False]*(n + 1)
def dfs(gotFromparent,cur):
    if visited[cur]:return
    visited[cur] = True
    d[cur] = gotFromparent + compliments[cur]

    for nextNode in graph[cur]:
        dfs(d[cur],nextNode)
dfs(0,1)

print(*d[1:],sep= ' ')