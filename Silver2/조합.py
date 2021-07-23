n,m = map(int,input().split())
d = [[0]*101 for _ in range(101)]

def comb(n,m):
    if n==m or m==0: return 1
    if d[n][m]!=0:return d[n][m]
    d[n][m] = comb(n-1,m-1) + comb(n-1,m)
    return d[n][m]
print(comb(n,m))