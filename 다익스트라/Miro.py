import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9
n = int(input())
def inside(y,x):
    return 0<= y <n and 0<=x <n
dy =[-1,1,0,0]
dx =[0,0,-1,1]

a = []
d = [[INF]*n for _ in range(n)]
d[0][0] = 0

for i in range(n):
    a.append(list(map(int,input().strip())))

q= deque()
q.append((0,0))
while q:
    y,x = q.popleft()

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not inside(ny,nx):continue
        if a[ny][nx] == 0:
            if d[y][x] + 1 < d[ny][nx]:
                d[ny][nx] = d[y][x]+1
                q.append((ny,nx))
        if a[ny][nx] == 1:
            if d[y][x]  < d[ny][nx]:
                d[ny][nx] = d[y][x]
                q.append((ny, nx))

print(d[n-1][n-1])