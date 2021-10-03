import math

n = int(input())
m = int(input())
d = [[math.inf]*(n+1) for _ in range(n+1)]
for i in range(n+1):d[i][i] = 0
for _ in range(m):
    a,b = map(int,input().split())
    d[a][b] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])

for x in range(1,n+1):
    #갈수있는곳
    go1 = 0
    go2 = 0
    for to in range(1,n+1):
        if d[x][to]>0 and d[x][to]!=math.inf:go1+=1
    for f in range(1,n+1):
        if d[f][x]>0 and d[f][x]!=math.inf:go2+=1
    print(n - (go1+go2) -1)