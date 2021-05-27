import sys
import itertools
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
n,s,p = map(int,input().split())
a = [[] for _ in range(n+1)]
for _ in range(n-1):
    v1,v2 = map(int,input().split())
    a[v1].append(v2)
    a[v2].append(v1)

d = []
v = [False]*(n+1)

def dfs(node,dist):
    if node == p:
        d.append(dist)
        return
    if v[node]:return
    v[node] =True
    for next_node in a[node]:
        if not v[next_node]:
            dfs(next_node,dist+1)

for num in range(1,s+1):
    dfs(num,0)
d.sort()
ans = n - d[0] - d[1] -1
print(ans)