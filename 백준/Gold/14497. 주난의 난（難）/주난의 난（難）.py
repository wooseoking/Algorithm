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

def jump(y,x):
    q = []
    visited = [[False]*m for _ in range(n)]
    q.append([y,x])
    visited[y][x] = True

    locations = []

    while q:
        y,x = q.pop(0)
        locations.append([y,x])

        for k in range(4):
            ny,nx = y + dy[k] , x + dx[k]
            if not inside(ny,nx):continue
            if visited[ny][nx]:continue
            if board[ny][nx] == 0:
                visited[ny][nx] = True
                q.append([ny,nx])

    for y,x in locations:
        for k in range(4):
            ny,nx = y + dy[k],x + dx[k]
            if not inside(ny,nx):continue
            board[ny][nx] = 0
            if ny == ey and nx == ex:return True

    return False

ans = 0
while True:
    flag = jump(sy,sx)
    ans+=1
    if flag:break
print(ans)