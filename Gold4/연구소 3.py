import itertools
import math
from collections import deque
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def inside(y,x):
    return 0<=y<n and 0<=x<n

# -1 퍼트릴 수 없음, 시간 최소
def bfs(virus):
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for y,x in virus:
        q.append((y,x))
        d[y][x] = 0

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if not inside(ny,nx):continue
            if a[ny][nx]==1:continue
            if d[ny][nx]!=-1:continue
            d[ny][nx] = d[y][x]+1
            q.append((ny,nx))

    tmp = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]==0:
                tmp = max(tmp,d[i][j])

    for i in range(n):
        for j in range(n):
            if a[i][j]==0 and d[i][j]==-1:return -1
    return tmp

viruses = []
for i in range(n):
    for j in range(n):
        if a[i][j]==2:
            viruses.append((i,j))

times = []

for v in itertools.combinations(viruses,m):
    time = bfs(v)
    times.append(time)

ans = math.inf
flag = False
for t in times:
    if t!=-1:
        flag = True
        ans = min(ans,t)

if flag:print(ans)
else:print(-1)