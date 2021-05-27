import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
h,w,r,c,fr,fc = map(int,input().split())
h-=1
w-=1
r-=1
c-=1
fr-=1
fc-=1
visited = [[-1]*m for _ in range(n)]

def inside(Y,X):
    return 0<=Y and 0<=X and Y+h<n and X+w<m

def check(Y,X):
    for i in range(Y,Y+h+1):
        if a[i][X]==1 or a[i][X+w]==1: return False
    for j in range(X,X+w+1):
        if a[Y][j]==1 or a[Y+h][j]==1:return False
    return True

q=deque()

q.append((r,c))
visited[r][c] = 0
dy = [-1,1,0,0]
dx =[0,0,-1,1]

while q:
    y,x = q.pop()
    if y==fr and x==fc:break
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not inside(ny,nx):continue
        if visited[ny][nx]!=-1:continue
        if not check(ny,nx) : continue
        visited[ny][nx] = visited[y][x]+1
        q.append((ny,nx))

print(visited[fr][fc])