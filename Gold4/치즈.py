import copy

n,m = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def getCount(y,x,Out):
    cnt = 0
    for k in range(4):
        ny,nx= y+dy[k],x+dx[k]
        if not inside(ny,nx):continue
        if Out[ny][nx]:cnt+=1
    return cnt

def inside(y,x):
    return 0<=y<n and 0<=x<m

def finish():
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:return False
    return True

t = 0

while not finish():
    t+=1
    #True : out False : in
    Out = [[False]*m for _ in range(n)]
    Out[0][0] =True

    q= [(0,0)]
    while q:
        y,x = q.pop(0)
        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if inside(ny,nx) and not Out[ny][nx] and board[ny][nx]==0:
                Out[ny][nx] = True
                q.append((ny,nx))
    delcandidate = []
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and getCount(i,j,Out)>=2:delcandidate.append((i,j))
    for y,x in delcandidate:board[y][x] = 0
print(t)