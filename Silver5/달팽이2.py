import sys
sys.setrecursionlimit(100000000)
m,n = map(int,input().split())
visited = [[False]*n for _ in range(m)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
ans = -1
def inside(y,x):
    return 0<=y<m and 0<=x<n

total = m*n
def dfs(y,x,cnt,k):
    global ans
    if cnt == total:
        print(ans)
        exit(0)
        return

    visited[y][x] = True
    ny = y+dy[k]
    nx = x+dx[k]
    if not inside(ny,nx):
        ans+=1
        next_d = (k+1)%4
        dfs(y+dy[next_d],x+dx[next_d],cnt+1,next_d)
    if visited[ny][nx]:
        ans+=1
        next_d = (k + 1) % 4
        dfs(y + dy[next_d], x + dx[next_d], cnt + 1, next_d)
    dfs(ny,nx,cnt+1,k)


dfs(0,0,0,0)