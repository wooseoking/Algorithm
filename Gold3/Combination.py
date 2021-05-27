import sys
sys.setrecursionlimit(1000000000)

d = [[-1]*2001 for _ in range(2001)]

def go(n,k,p):
    if d[n][k] != -1:return d[n][k]
    if k==0 or k==n:
        d[n][k] = 1
        return 1
    d[n][k] = go(n-1,k-1,p)%p + go(n-1,k,p)%p
    d[n][k]%=p
    return d[n][k]

n,k,m = map(int,input().split())

ans = 1
while n or k:
    ans *=go(n%m,k%m,m)
    ans %=m
    n//=m
    k//=m
print(ans)