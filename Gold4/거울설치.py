from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n = int(input())
a = [list(input())for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def inside(y,x):
    return 0<=y<n and 0<=x<n

sy,sx ,ey,ex= -1,-1,-1,-1
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j]=='#' and cnt == 0:
            sy,sx = i,j
            cnt+=1
        if a[i][j]=='#' and cnt==1:
            ey,ex = i,j

q = deque()
q.append((sy,sx,0))
ans = -1
visited[sy][sx] = True
while q:
    y,x,depth = q.popleft()

    if y==ey and x==ex:
        ans = depth
        break

    for k in range(4):
        ny,nx = y,x
        candi= []
        while True:
            ny+=dy[k]
            nx+=dx[k]
            if not inside(ny,nx):break
            if a[ny][nx]=='!' or a[ny][nx]=='#':
                candi.append((ny,nx))
            if a[ny][nx]=='*':break

        for n_y,n_x in candi:
            if inside(n_y,n_x) and not visited[n_y][n_x]:
                visited[n_y][n_x] = True
                q.append((n_y,n_x,depth+1))

print(ans - 1)
