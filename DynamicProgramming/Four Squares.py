import math

n = int(input())
INF = 1e9
d = [INF]*(n+1)
d[0]=0

for i in range(1,n+1):
    for k in range(1,int(math.sqrt(i))+1):
        if i-k**2>=0:
            d[i] = min(d[i],d[i-k**2]+1)
print(d[n])