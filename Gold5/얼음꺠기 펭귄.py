import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n,s,p = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dist = []
v = [False]*(n+1)

def dfs(cur,cnt):
    if cur==p:
        dist.append(cnt)
        return
    if v[cur]:return
    v[cur] =True
    for next_ in graph[cur]:
        dfs(next_,cnt+1)

for i in range(1,s+1):
    dfs(i,0)
dist.sort()
ans = n - (dist[0]+dist[1]+1)
print(ans)