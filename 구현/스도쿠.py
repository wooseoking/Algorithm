import sys
sys.setrecursionlimit(1000000000)
a = [list(map(int,input().split())) for _ in range(9)]
grid = [[False]*10 for _ in range(10)]
garo = [[False]*10 for _ in range(10)]
sero = [[False]*10 for _ in range(10)]
for i in range(9):
    for j in range(9):
        if a[i][j]!=0:
            n = a[i][j]
            garo[i][n] = True
            sero[j][n] =True
            grid[(i//3)*3 + j//3][n] = True

def go(z):
    if z==9*9:
        for row in a:
            print(*row,sep=' ')
        return
    y = z//9
    x = z % 9

    if a[y][x]==0 :
        for num in range(1,10):
            if not grid[(y//3)*3 + x//3][num] and not garo[y][num] and not sero[x][num]:
                a[y][x] = num
                grid[(y//3)*3 + x//3][num] = True
                garo[y][num] = True
                sero[x][num] = True
                go(z+1)
                a[y][x] = 0
                grid[(y // 3) * 3 + x // 3][num] = False
                garo[y][num] = False
                sero[x][num] = False
    else : go(z+1)

go(0)
