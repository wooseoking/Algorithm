import math

N,K = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
ans= math.inf

for k in range(1,N):
    v1 = k * a[0]
    v2 = (N-k) * a[k]
    time,r = divmod(K,v1+v2)
    if r!=0:
        time+=1

    ans = min(ans,time)
print(ans)