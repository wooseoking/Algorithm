import math
from collections import deque
t = int(input())
wall = '#'
fire = '*'
me = '@'
space = '.'
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<n and 0<=x<m

for _ in range(t):
    m,n = map(int,input().split())
    a = [list(input().rstrip()) for _ in range(n)]
    sy,sx = -1,-1
    firetime = [[math.inf] * m for _ in range(n)]
    fq = deque()
    q = deque()

    for i in range(n):
        for j in range(m):
            if a[i][j]==me:
                sy,sx = i,j
                a[i][j] = space
            if a[i][j]==fire:
                fq.append((i,j))
                firetime[i][j] = 0

    while fq:
        y,x = fq.popleft()

        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if not inside(ny,nx):continue
            if a[ny][nx]==wall:continue
            if firetime[ny][nx]!=math.inf:continue
            firetime[ny][nx] = firetime[y][x] +1
            fq.append((ny,nx))

    q.append((sy,sx,0))
    visited = [[False]*m for _ in range(n)]
    visited[sy][sx] =True
    ans = -1
    while q:
        y,x,time = q.popleft()

        if y==0 or y==n-1 or x==0 or x==m-1:
            ans = time
            break
        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if not inside(ny,nx):continue
            if visited[ny][nx]:continue
            if a[ny][nx]==wall:continue
            if firetime[ny][nx] > time + 1:
                visited[ny][nx] = True
                q.append((ny,nx,time+1))

    print(ans+1 if ans!=-1 else 'IMPOSSIBLE')