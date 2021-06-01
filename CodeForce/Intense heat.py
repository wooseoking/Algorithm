import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
d = [0]*(n+1)

for i in range(1,n+1):
    d[i] = d[i-1] + a[i]
Total = d[n]
ans = -1e9
for i in range(k,n+1):
    if i-k>=0:
        for j in range(k,n+1):
            ans = max(ans,(d[i]-d[i-j])/j)
print(ans)