import copy

dy = [-1,0,1,0]
dx = [0,1,0,-1]
WALL = 6
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

cctvs =[]
res = []
for y in range(n):
    for x in range(m):
        if 1<=board[y][x]<=5:cctvs.append((y,x,board[y][x]))

def inside(y_,x_):
    return 0<=y_<n and 0<=x_<m

def is_cctv(y_,x_):
    return 1<=board[y_][x_]<=5

def move(y_,x_,dir_):
    global board

    ny,nx = y_,x_
    while True:
        ny+=dy[dir_]
        nx+=dx[dir_]
        if not inside(ny,nx) or board[ny][nx]==WALL:break
        if is_cctv(ny,nx):continue
        board[ny][nx] = -1


def go(idx):
    global board
    if idx == len(cctvs):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:cnt+=1
        res.append(cnt)
        return

    y,x,cctv_num = cctvs[idx]
    origin_board = copy.deepcopy(board)

    if cctv_num==1:
        for k in range(4):
            move(y,x,k)
            go(idx+1)
            board = copy.deepcopy(origin_board)

    elif cctv_num==2:
        for k in range(2):
            move(y,x,k)
            move(y,x,k+2)
            go(idx+1)
            board = copy.deepcopy(origin_board)
    elif cctv_num==3:
        for k in range(4):
            move(y,x,k)
            move(y,x,(k+1)%4)
            go(idx+1)
            board = copy.deepcopy(origin_board)
    elif cctv_num==4:
        for k in range(4):
            move(y,x,k)
            move(y,x,(k+1)%4)
            move(y,x,(k+2)%4)
            go(idx+1)
            board = copy.deepcopy(origin_board)
    elif cctv_num==5:
        for k in range(4):
            move(y,x,k)
        go(idx+1)
        board = copy.deepcopy(origin_board)


go(0)
print(min(res))