import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int,input().split())
a = [[] for _ in range(n+1)]
ans = [0]*(n+1)
visited = [False]*(n+1)
cnt = 0
for _ in range(m):
    v2,v1 = map(int,input().split())
    a[v1].append(v2)

def dfs(now):
    global visited,cnt
    if visited[now]:return
    visited[now] = True
    cnt+=1
    for next in a[now]:
        dfs(next)

for i in range(1,n+1):
    cnt = 0
    visited = [False]*(n+1)
    dfs(i)
    ans[i] = cnt
MaxV = max(ans[1:])
for i,v in enumerate(ans):
    if v==MaxV:print(i,end=' ')