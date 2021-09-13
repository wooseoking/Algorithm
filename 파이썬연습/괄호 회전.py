dy = [0,0,1,-1]
dx = [1,-1,0,0]
cnt = 0
def inside(y,x,n,m):
    return 0<=y<n and 0<=x<m

def go(initk,board,i,j,k,n,m,visit):
    global cnt

    if visit[i][j] and cnt>=2 and  k == initk:
        return cnt
    visit[i][j] = True
    cnt+=1
    nk = -1
    if k==0:
        if board[i][j]=='S':
            nk = 0
        elif board[i][j]=='R':
            nk = 2
        elif board[i][j] == 'L':
            nk = 3
    elif k==1:
        if board[i][j]=='S':
            nk = 1
        elif board[i][j]=='R':
            nk = 3
        elif board[i][j] == 'L':
            nk = 2
    elif k==2:
        if board[i][j]=='S':
            nk = 2
        elif board[i][j]=='R':
            nk = 1
        elif board[i][j] == 'L':
            nk = 0
    elif k==3:
        if board[i][j]=='S':
            nk = 3
        elif board[i][j]=='R':
            nk = 0
        elif board[i][j] == 'L':
            nk = 1
    ny,nx = i+dy[nk],j+dx[nk]
    if ny== -1:
        ny =  n-1
    elif ny==n:
        ny = 0
    if nx == -1:
        nx = m-1
    elif nx==m:
        nx = 0

    go(initk,board,ny,nx,nk,n,m,visit)


def solution(grid):
    global cnt
    answer = []
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            for k in range(4):
                visited = [[False]*m for _ in range(n)]
                cnt = 0
                inik = k
                go(inik,grid,i,j,k,n,m,visited)
                print(cnt)
    return answer