a = [list(map(int,input().split())) for _ in range(9)]
CONST_N = 9
garo = [[False]*10 for _ in range(9)]
sero = [[False]*10 for _ in range(9)]
section = [[False]*10 for _ in range(9)]

for i in range(CONST_N):
    for j in range(CONST_N):
        if a[i][j]!=0:
            number = a[i][j]
            garo[i][number] = True
            sero[j][number] = True
            section[(i//3)*3 + (j//3)][number] = True


def go(z):
    if z== 81:
        #정답
        for rows in a:
            print(*rows,sep=' ')
        exit(0)
        return

    y,x = z//9,z%9

    if a[y][x]!=0:go(z+1)
    else:
        sec = (y//3)*3 + (x//3)

        for num in range(1,10):

            if not garo[y][num] and not sero[x][num] and not section[sec][num]:
                garo[y][num] = True
                sero[x][num] = True
                section[sec][num] = True
                a[y][x] = num
                go(z+1)
                a[y][x] = 0
                garo[y][num] = False
                sero[x][num] = False
                section[sec][num] = False

go(0)