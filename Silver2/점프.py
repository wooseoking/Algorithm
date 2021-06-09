n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0]=1

for i in range(n):
    for j in range(n):
        for k in range(j):
            if k+a[i][k]==j:
                d[i][j]+=d[i][k]
        for k in range(i):
            if k+a[k][j]==i:
                d[i][j] +=d[k][j]

print(d[n-1][n-1])