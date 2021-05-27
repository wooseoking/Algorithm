import sys
input = sys.stdin.readline
n,m = map(int,input().split())

a = [list(map(int,input().strip())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
for i in range(n):d[i][0] = a[i][0]
for j in range(m):d[0][j] = a[0][j]

ans = 0
for i in range(1,n):
    for j in range(1,m):
        if a[i][j]!=0:
            d[i][j] = min(d[i-1][j],d[i-1][j-1],d[i][j-1]) +1
            ans = max(ans,d[i][j])

for i in range(n):
    for j in range(m):
        ans = max(d[i][j],ans)
print(ans*ans)