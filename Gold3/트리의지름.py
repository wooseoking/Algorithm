import sys
import heapq
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

def dfs(now,dist,visited,d):
    if visited[now]:return
    visited[now] = True
    d[now] = dist
    for cost_,to in a[now]:
        dfs(to,dist+cost_,visited,d)

n = int(input())
a = [[] for _ in range(n+1)]
d = [0]*(n+1)
visited = [False]*(n+1)
for _ in range(n):
    info = list(map(int,input().split()))
    From_ = info[0]
    info.pop(0)
    info.pop(-1)
    #i 가려는 정점
    for j in range(0,len(info),2):
        to = info[j]
        cost = info[j+1]
        a[From_].append((cost,to))
dfs(1,0,visited,d)
max_node = d.index(max(d))
visited.clear()
d.clear()
visited = [False]*(n+1)
d = [0]*(n+1)
dfs(max_node,0,visited,d)
print(max(d))