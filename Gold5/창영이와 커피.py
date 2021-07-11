import math

n,k = map(int,input().split())
a = list(map(int,input().split()))
d = [[math.inf]*(10**5+1) for _ in range(n)]
for i in range(n):
    d[i][a[i]] = 1

for i in range(1,n):
    for j in range(k+1):
        d[i][j] = min(d[i][j],d[i-1][j])
        if j-a[i]>=0:
            d[i][j] = min(d[i][j],d[i-1][j-a[i]]+1)

if k==0:
    print(0)
    exit(0)
if d[n-1][k]!=math.inf:print(d[n-1][k])
else:print(-1)