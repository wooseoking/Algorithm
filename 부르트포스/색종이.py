ROW = 100
COL = 100

a =[[0 for j in range(COL)] for i in range(ROW)]

n = int(input())
for _ in range(n):
    y,x = map(int,input().split())
    x-=1
    y-=1
    for i in range(y,y+10):
        for j in range(x,x+10):
            a[i][j] = 1

