from collections import deque
N = 10
n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
EXIT = 'O'
WALL = '#'

def inside(y,x):
    return 0<=y<n and 0<=x<m

sby,sbx,sry,srx = -1,-1,-1,-1
exity,exitx = -1,-1
for i in range(n):
    for j in range(m):
        if a[i][j]=='B':
            sby ,sbx = i,j
            a[i][j] = '.'
        if a[i][j]=='R':
            sry,srx = i,j
            a[i][j] = '.'
        if a[i][j]=='O':
            exity,exitx = i,j
visited = [[[[False]*N for _ in range(N)]for _ in range(N)]for _ in range(N)]
q = deque()
q.append((sby,sbx,sry,srx,0))
visited[sby][sbx][sry][srx] = True

ans = -1
while q:
    by,bx,ry,rx,cnt = q.popleft()

    if ry==exity and rx == exitx:
        ans = cnt
        break

    for k in range(4):
        nby,nbx,nry,nrx = by,bx,ry,rx
        #Blue ball
        bluecount,redcount = 0,0
        while a[nby][nbx]!=WALL and a[nby][nbx]!=EXIT:
            nby+=dy[k]
            nbx+=dx[k]
            bluecount+=1

        if a[nby][nbx]==WALL:
            nby-=dy[k]
            nbx-=dx[k]
        elif a[nby][nbx] == EXIT:continue

        #Red Ball
        while a[nry][nrx] != WALL and a[nry][nrx] != EXIT:
            nry+=dy[k]
            nrx+=dx[k]
            redcount+=1

        if a[nry][nrx]=='#':
            nry-=dy[k]
            nrx-=dx[k]

        # 위치가 같은경우
        if nry==nby and nrx==nbx:
            if redcount>bluecount:
                nry-=dy[k]
                nrx-=dx[k]
            else:
                nby-=dy[k]
                nbx-=dx[k]

        if not visited[nby][nbx][nry][nrx]:
            visited[nby][nbx][nry][nrx] = True
            q.append((nby,nbx,nry,nrx,cnt+1))
print(ans)