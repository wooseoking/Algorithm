import sys
sys.setrecursionlimit(10**9)
n = int(input())
a = [list(map(int,input().split()))for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
d = [[0]*n for _ in range(n)]

def inside(y,x):
    return 0<=y<n and 0<=x<n

def go(y,x):
    if d[y][x]!=0:return d[y][x]
    for k in range(4):
        ny,nx = y+dy[k],x+dx[k]
        if not inside(ny,nx):continue
        if a[y][x] < a[ny][nx]:
            d[y][x] = max(d[y][x],go(ny,nx))
    d[y][x]+=1
    return d[y][x]
ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans,go(i,j))

print(ans)