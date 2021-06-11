n,m = map(int,input().split())
a = list(list(map(int,input().split())) for _ in range(n))
group = [[0]*m for _ in range(n)]
c = [[False]*m for _ in range(n)]
g = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
edges = []

def inside(y,x):
    return 0<=y<n and 0<=x<m

def dfs(y,x,num):
    if c[y][x]:return
    group[y][x] = num
    c[y][x] =True
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if not inside(ny,nx):continue
        if a[ny][nx] == 1:
            dfs(ny,nx,num)

for i in range(n):
    for j in range(m):
        if a[i][j]==1 and not c[i][j]:
            g+=1
            dfs(i,j,g)

def go(y,x,start_num):
    for k in range(4):
        ny = y
        nx = x
        bridge = 0
        find = False
        while True:
            ny += dy[k]
            nx += dx[k]
            bridge += 1
            if not inside(ny,nx) : break
            if group[ny][nx]==start_num:break
            if group[ny][nx]!=0:
                find = True
                break
        if find and bridge>2:
            edges.append((start_num,group[ny][nx],bridge-1))

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 : continue
        start_num = group[i][j]
        go(i,j,start_num)

edges.sort(key = lambda l:l[2])

Rank = [0]*7
parent = [i for i in range(7)]

def getParent(x):
    if x==parent[x]:return x
    parent[x] = getParent(parent[x])
    return parent[x]

def union(x,y):
    x = getParent(x)
    y = getParent(y)
    if x==y:return
    if Rank[x] < Rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if Rank[x] == Rank[y]:Rank[x]+=1

edges.sort(key=lambda l:l[2])
ans = 0
cnt = 0

for v1,v2,cost in edges:
    if getParent(v1)!=getParent(v2):
        cnt+=1
        ans+=cost
        union(v1,v2)

if cnt==g-1:print(ans)
else :print(-1)