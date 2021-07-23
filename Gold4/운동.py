import math

n,m = map(int,input().split())
d = [[math.inf]*(n+1) for _ in range(n+1)]
for i in range(n+1):d[i][i] = 0

for _ in range(m):
    v1,v2,cost = map(int,input().split())
    d[v1][v2] = min(d[v1][v2],cost)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])
result = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:continue
        cost = d[i][j] + d[j][i]
        result.append(cost)
if not result:print(-1)
min_ = min(result)
if min_>=math.inf:print(-1)
else:print(min_)