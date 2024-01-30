from collections import deque

m,n = map(int,input().split())
board = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
sy,sx,ey,ex = 0,0,0,0

z = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'C' and z == 0:
            sy,sx = i,j
            board[i][j] = '.'
            z+=1
        elif board[i][j] == 'C' and z == 1:
            ey,ex = i,j
            board[i][j] = '.'

def inside(y,x):
    return 0<=y < n and 0<=x<m

dy = [-1,1,0,0]
dx = [0,0,-1,1]
q = deque()
q.append([sy,sx,-1])
visited[sy][sx] = True

while q:
    y,x,cnt = q.popleft()

    if y == ey and x == ex:
        print(cnt)
        break

    for k in range(4):
        ny,nx = y,x
        while True:
            ny += dy[k]
            nx += dx[k]

            if not inside(ny,nx):break
            if board[ny][nx] == '*':break
            if visited[ny][nx]:continue
            visited[ny][nx] = True
            q.append([ny,nx,cnt + 1])