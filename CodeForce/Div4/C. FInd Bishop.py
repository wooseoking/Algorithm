tc = int(input())
dy = [-1,-1,1,1]
dx = [-1,1,-1,1]
def inside(y,x):
    return 0<=y<8 and 0<=x<8
def draw(y,x):
    ret = [['.']*8 for _ in range(8)]
    ret[y][x] = '#'
    for k in range(4):
        ny,nx = y,x

        while True:
            ny+=dy[k]
            nx+=dx[k]
            if not inside(ny,nx):break
            ret[ny][nx] = '#'

    return ret


for _ in range(tc):
    input()
    a = [list(input()) for _ in range(8)]
    row,col = 0,0
    for i in range(8):
        for j in range(8):
            tmp = draw(i,j)
            ok = True
            for r1,r2 in zip(a,tmp):
                if r1 != r2:
                    ok = False
                    break
            if ok:
                row,col = i+1,j+1


    print(row,col)