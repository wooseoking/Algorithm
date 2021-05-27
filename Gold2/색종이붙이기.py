import sys
sys.setrecursionlimit(1000000000)
n = 10
board = [list(map(int,input().split()))for _ in range(n)]
c = [[False]*n for _ in range(n)]
check_finish = 0
for i in range(n):
    for j in range(n):
        if board[i][j]==0:c[i][j] = True
        else : check_finish+=1


ret = []
d = [0 for _ in range(6)]

def inside(y,x,l):
    return 0<= y+l-1<n and 0<=x+l-1<n

def check(y,x,l):
    for i in range(y,y+l):
        for j in range(x,x+l):
            if c[i][j] :return False
    return True

def Visit(y,x,l):
    for i in range(y, y + l):
        for j in range(x, x + l):
            c[i][j] = not c[i][j]

def go(z,cnt):
    if z == n*n:
        ret.append(sum(d))
        return
    if cnt == check_finish:
        ret.append(sum(d))
        return
    y = z//n
    x = z%n
    if c[y][x] or board[y][x]==0:go(z+1,cnt)
    else :
        #1,#2,#3,#4,#5 확인
        for l in range(1,6):
            if inside(y,x,l) and check(y,x,l) and d[l]<5:
                Visit(y,x,l)
                d[l] +=1
                go(z+1,cnt + l*l)
                d[l]-=1
                Visit(y,x,l)


go(0,0)
if len(ret)==0:print(-1)
else: print(min(ret))