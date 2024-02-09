from collections import deque

# input
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]

sy, sx = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            sy, sx = i, j

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inside(y, x):
    return 0 <= y < n and 0 <= x < m


q = deque()
q.append([sy, sx])
d[sy][sx] = 0

while q:
    y, x = q.popleft()

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if not inside(ny, nx): continue
        if d[ny][nx] != -1: continue
        if a[ny][nx] == 0: continue
        d[ny][nx] = d[y][x] + 1
        q.append([ny, nx])

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(a[i][j],end=' ')
        else:
            print(d[i][j],end=' ')
    print()
