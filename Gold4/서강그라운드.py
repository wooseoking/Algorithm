import math

n,m,r = map(int,input().split())
item = [0] + list(map(int,input().split()))
d = [[math.inf]*(n+1) for _ in range(n+1)]
graph = [[]*(n+1) for _ in range(n+1)]
for i in range(n+1):d[i][i]=0

for _ in range(r):
    u,v,c = map(int,input().split())
    d[u][v] = d[v][u] = c
    graph[u].append(v)
    graph[v].append(u)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]

result = []

for i in range(1,n+1):
    temp = item[i]
    for j in range(1,n+1):
        if i==j:continue
        if d[i][j]<=m:
            temp+=item[j]
    result.append(temp)
print(max(result))