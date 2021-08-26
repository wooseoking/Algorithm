import sys
n,m = map(int,input().split())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
v = [[False]*m for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<n and 0<=x<m

def go(y,x):
    v[y][x] = True
    q = [(y,x)]
    ref = a[y][x]
    na = [[False]*m for _ in range(n)]
    na[y][x] = True

    while q:
        y_,x_ = q.pop(0)

        for k in range(4):
            ny,nx = y_+dy[k],x_+dx[k]
            if not inside(ny,nx):continue
            if v[ny][nx]:continue
            if a[ny][nx]!=ref:continue
            v[ny][nx] = True
            na[ny][nx] = True
            q.append((ny,nx))
    rows = []
    cols = []
    for ii in range(n):
        if na[ii][x]:rows.append(ii)
    for jj in range(m):
        if na[y][jj]:cols.append(jj)
    return max(rows) - min(rows) +1,max(cols) - min(cols) +1

mr ,mc = 1000,1000

for i in range(n):
    for j in range(m):
        if not v[i][j]:
            row,col = go(i,j)
            mr = min(mr,row)
            mc = min(mc,col)

print(n//mr,m//mc)
for i in range(0,n,mr):
    string = ""
    for j in range(0,m,mc):
        string+=a[i][j]
    print(string)