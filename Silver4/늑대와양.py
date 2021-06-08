import sys
from collections import deque
input = sys.stdin.readline

row,col = map(int,input().split())
a = list(list(input().strip()) for _ in range(row))
visited = [[False]*col for _ in range(row)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<row and 0<=x<col

q = deque()

for i in range(row):
    for j in range(col):
        if a[i][j] == '.':
            a[i][j] = 'D'
        elif a[i][j] == 'W':
            visited[i][j] = True
            q.append((i,j))

Fail = False
while q:
    y,x = q.popleft()
    ok = True
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not inside(ny,nx):continue
        if visited[ny][nx]:continue
        if a[ny][nx] =='D':continue
        if a[ny][nx]=='S':
            ok = False
            break
        visited[ny][nx] = True
        if ok :
            q.append((ny,nx))
    if not ok:
        Fail = True
        break
if Fail:print(0)
else:
    print(1)
    for i in range(row):
        for j in range(col):
            print(a[i][j],end='')
        print()