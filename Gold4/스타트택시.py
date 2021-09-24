from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def inside(r,c):
    return 0<=r<n and 0<=c<n

def bfs2(y,x,yy,xx):
    visited = [[False]*n for _ in range(n)]
    visited[y][x] = True
    q = [(y,x,0)]

    while q:
        y,x,d = q.pop(0)

        if y==yy and x==xx:
            return d

        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if inside(ny,nx) and a[ny][nx]!=1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny,nx,d+1))
    return -1

n,m,fuel = map(int,input().split())
a = [list(map(int,input().split()))for _ in range(n)]
taxiy,taxix=map(int,input().split())
taxiy-=1
taxix-=1

passengers_to_destination = []
passenger_location = [[0]*n for _ in range(n)]
passenger_visited = [[False]*n for _ in range(n)]
passenger_number = [[-1]*n for _ in range(n)]
passenger_destination = []
for i in range(m):
    fy,fx,ey,ex = map(int,input().split())
    fy-=1
    fx-=1
    ey-=1
    ex-=1
    passenger_location[fy][fx] = 1
    passengers_to_destination.append(bfs2(fy,fx,ey,ex))
    passenger_number[fy][fx] = i
    passenger_destination.append((ey,ex))

def bfs(ty,tx):
    candi = []
    visited = [[False]*n for _ in range(n)]
    q = [(ty,tx,0)]
    visited[ty][tx] = True

    while q:
        y,x,d = q.pop(0)
        if passenger_location[y][x]==1 and not passenger_visited[y][x]:
            candi.append((d,y,x,passenger_number[y][x]))
        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if inside(ny,nx) and a[ny][nx]!=1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny,nx,d+1))
    return sorted(candi)



for _ in range(m):
    cadidates = bfs(taxiy,taxix) #택시~사람위치

    if not cadidates:
        print(-1)
        exit(0)

    dist,py,px,idx = cadidates[0]
    passenger_visited[py][px] = True

    if fuel - dist <=0:
        print(-1)
        exit(0)

    fuel-=dist

    p_to_d = passengers_to_destination[idx]

    if p_to_d ==-1 or fuel - p_to_d<0:
        print(-1)
        exit(0)
    fuel-=p_to_d
    fuel+=p_to_d*2
    taxiy,taxix = passenger_destination[idx][0],passenger_destination[idx][1]
print(fuel)