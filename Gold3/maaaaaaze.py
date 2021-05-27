from collections import deque
import sys
import itertools
import copy
input = sys.stdin.readline
board = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

def inside(x,y,z):
    return 0<=x<5 and 0<=y<5 and 0<=z<5

def bfs(a):
    if a[0][0][0]==0 : return -1
    d = [[[-1]*5 for _ in range(5)] for _ in range(5)]
    d[0][0][0] =0
    q = deque()
    q.append((0,0,0))
    while q:
        z_,y_,x_ = q.popleft()

        for k in range(6):
            nz = z_ + dz[k]
            ny = y_ + dy[k]
            nx = x_ + dx[k]
            if not inside(nz,ny,nx):continue
            if a[nz][ny][nx]==0:continue
            if d[nz][ny][nx]!=-1:continue
            d[nz][ny][nx] = d[z_][y_][x_]+1
            q.append((nz,ny,nx))

    return d[4][4][4]

def get_rotated_2D_array(z):
    a = copy.deepcopy(z)
    for i in range(5):
        for j in range(5):
            a[i][j] = z[4-j][i]
    return a

orders = [i for i in range(5)]
ans = 1e9
U = list(itertools.permutations(orders,len(orders)))

for orders in U:
    b = copy.deepcopy(board)

    for i,k in enumerate(orders):
        b[i] = board[k]

    for l1 in range(4):
        for l2 in range(4):
            for l3 in range(4):
                for l4 in range(4):
                    for l5 in range(4):
                        ret = bfs(b)
                        if ret != -1:ans = min(ans,ret)
                        b[4] = get_rotated_2D_array(b[4])
                    b[3] = get_rotated_2D_array(b[3])
                b[2] = get_rotated_2D_array(b[2])
            b[1] = get_rotated_2D_array(b[1])
        b[0] = get_rotated_2D_array(b[0])
if ans!=1e9:print(ans)
else:print(-1)