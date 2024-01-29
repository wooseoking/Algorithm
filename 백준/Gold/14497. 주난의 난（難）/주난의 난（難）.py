from collections import deque

n,m = map(int,input().split())
sy,sx,ey,ex = map(int,input().split())
sy-=1
sx-=1
ey-=1
ex-=1
board = [list(input()) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            board[i][j] = 1
        else:
            board[i][j] = 0

def inside(y,x):
    return 0<=y < n and 0<=x < m

# (y,x) 에서 시작
def bfs(y,x):
    dq = deque()
    countBoard = [[-1] * m for _ in range(n)]
    countBoard[y][x] = 0
    dq.append([y,x])
    while dq:
        y,x = dq.popleft()
        cnt = countBoard[y][x]

        for k in range(4):
            ny,nx = y + dy[k] , x + dx[k]
            if not inside(ny,nx):continue
            if countBoard[ny][nx] != -1:continue

            if board[ny][nx] == 1:
                countBoard[ny][nx] = cnt + 1
                dq.append([ny,nx])
            elif board[ny][nx] == 0:
                countBoard[ny][nx] = cnt
                dq.appendleft([ny,nx])

    ans = countBoard[ey][ex] + 1
    return ans
ans = bfs(sy,sx)
print(ans)