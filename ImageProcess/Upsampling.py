n,m = map(int,input().split())
a = [list(map(int,input().split()))for _ in range(n)]
out_n = n*m
img = [[0]*n*m for _ in range(out_n)]

for i in range(out_n):
    for j in range(out_n):
        img[i][j] = a[i//m][j//m]
        print(img[i][j],end=' ')
    print()