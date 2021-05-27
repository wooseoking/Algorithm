import sys
from collections import deque
sys.setrecursionlimit(100000000)
n,m = map(int,input().split())
a = [list(input().strip()) for _ in range(n)]
sby = None
sbx = None
sry = None
srx = None
fry = None
frx = None
for i in range(n):
    for j in range(m):
        if a[i][j]=="R":
            sry =i
            srx = j
        elif a[i][j] =="B":
            sby = i
            sbx = j
        elif a[i][j] == "O":
            fry = i
            frx = j

dy = [-1,1,0,0]
dx = [0,0,-1,1]
visit = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
visited_Red = [[False]*m for _ in range(n)]
visited_Blue = [[False]*m for _ in range(n)]

q = deque()
visit[sry][srx][sby][sbx] = True
q.append((sry,srx,sby,sbx,0,False))
ans = False
while q:
    ry,rx,by,bx,cnt,success = q.popleft()

    if cnt == 11: continue
    if success:
        ans = True
        break

    for k in range(4):
        nry = ry
        nrx = rx
        nby = by
        nbx = bx

        while True:
            nry+=dy[k]
            nrx+=dx[k]
            if a[nry][nrx]=="#":break
            if a[nry][nrx] == "O":break
        while True:
            nby += dy[k]
            nbx += dx[k]
            if a[nby][nbx] == "#": break
            if a[nby][nbx] == "O": break

        if a[nry][nrx]=="#" and a[nby][nbx] == "#":
            nry-=dy[k]
            nrx-=dx[k]
            nby-=dy[k]
            nbx-=dx[k]
            if nry==nby and nrx == nbx:
                dist_red = abs(nry-ry) + abs(nrx - rx)
                dist_blue = abs(nby - by) + abs(nbx - bx)
                if dist_red > dist_blue:
                    nry-=dy[k]
                    nrx-=dx[k]
                    if visit[nry][nrx][nby][nbx]:continue
                    visit[nry][nrx][nby][nbx] = True
                    q.append((nry,nrx,nby,nbx,cnt+1,False))
                else:
                    nby -=dy[k]
                    nbx -=dx[k]
                    if visit[nry][nrx][nby][nbx]:continue
                    visit[nry][nrx][nby][nbx]= True
                    q.append((nry, nrx, nby, nbx, cnt + 1, False))
            else:
                if visit[nry][nrx][nby][nbx]: continue
                visit[nry][nrx][nby][nbx] = True
                q.append((nry, nrx, nby, nbx, cnt + 1, False))
        elif a[nry][nrx]=="O" and a[nby][nbx] == "#":
            nby-=dy[k]
            nbx-=dx[k]
            q.append((nry,nrx,nby,nbx,cnt+1,True))

if ans:print(1)
else :print(0)