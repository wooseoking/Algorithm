import sys
sys.setrecursionlimit(10**8)

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<n and 0<=x<m

n,m,k_ = map(int,input().split())
a = [['*']*m for _ in range(n)]
for _ in range(k_):
    y,x = map(int,input().split())
    y-=1
    x-=1
    a[y][x] = '#'
v = [[False]*m for _ in range(n)]

def dfs(y,x):
    global area
    if v[y][x]:return
    area+=1
    v[y][x] = True
    for k in range(4):
        ny,nx = y+dy[k],x+dx[k]
        if inside(ny,nx) and a[ny][nx]=='#':
            dfs(ny,nx)
area = 0
ans = -1
for i in range(n):
    for j in range(m):
        if a[i][j]=='#' and not v[i][j]:
            area = 0
            dfs(i,j)
            ans = max(ans,area)
print(ans)