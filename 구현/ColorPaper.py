import sys
sys.setrecursionlimit(100000000)
from collections import deque
import heapq
input = sys.stdin.readline
m,n = map(int,input().split())
a = [list(input().strip())for _ in range(n)]
graph = [[]for _ in range(n*m)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
sy = None
sx = None
fy = None
fx = None
INF = 1e9
def inside(y,x):
    return 0<=y<n and 0<=x<m

for i in range(n):
    for j in range(m):
        if a[i][j]=='E':
            fy = i
            fx = j
        elif a[i][j]=='T':
            sy = i
            sx = j
            a[i][j] = '0'

start = sy*m+sx
finish = fy*m+fx
visited = [[False]*m for _ in range(n)]

def dfs(y,x):
    if visited[y][x] : return
    visited[y][x] = True
    now = y*m + x
    for k in range(4):
        cost = 0
        ny = y
        nx = x
        ok = True
        while True:
            ny+=dy[k]
            nx+=dx[k]
            if not inside(ny,nx):
                ok = False
                break
            if a[ny][nx] =='H':
                ok = False
                break
            if a[ny][nx] == 'E' or a[ny][nx] =='R':
                break
            cost += int(str(a[ny][nx]))
        if ok:
            if a[ny][nx]=='E':
                next_node = ny * m + nx
                graph[now].append((cost, next_node))
                dfs(ny, nx)
            else:
                ny-=dy[k]
                nx-=dx[k]
                next_node = ny * m + nx
                graph[now].append((cost,next_node))
                dfs(ny,nx)

dfs(sy,sx)
pq = []
heapq.heappush(pq,(0,start))
distance = [INF]*n*m
distance[start] = 0
while pq:
    cost, now = heapq.heappop(pq)
    if distance[now] < cost:continue

    for next_c , next_ in graph[now]:
        next_cost = cost+ next_c
        if next_cost < distance[next_]:
            distance[next_] = next_cost
            heapq.heappush(pq,(next_cost,next_))

if distance[finish]!=INF:print(distance[finish])
else:print(-1)