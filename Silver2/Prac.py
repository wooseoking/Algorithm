a = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        a[i][j] = i*4+j
b = [[0]*4 for _ in range(4)]
m=4
n=4
for i in range(n):
    for j in range(m):
        b[i][j] = (i//2)*(n//2) + j//2
for row in b:
    print(*row,sep=' ')