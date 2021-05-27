import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]


n,m = map(int,input().split())
a = [[0]*m for _ in range(n)]
d = [[-1]*m for _ in range(n)]

def inside(Y,X):
    return 0 <= Y < n and 0 <= X < m


for i in range(n):
    s = input()
    for j in range(m):
        a[i][j] = int(s[j])

d[0][0] = 0
q = deque()
q.append((0,0))

while q:
    y,x = q.popleft()

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not inside(ny,nx):continue
        if d[ny][nx]!=-1:continue
        if a[ny][nx]==0:continue
        d[ny][nx] = d[y][x]+1
        q.append((ny,nx))

print(d[n-1][m-1]+1)
