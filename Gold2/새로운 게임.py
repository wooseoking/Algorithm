n,k = map(int,input().split())
mapcolor = [list(map(int,input().split()))for _ in range(n)]
a = [[[] for _ in range(n)] for _ in range(n)]
# 0 1 2 == 흰 빨 파
# 행 열 이동방향
#방향
dy = [0,0,-1,1]
dx = [1,-1,0,0]
where = []
direction = []
for i in range(k):
    row,col,dir = map(int,input().split())
    row-=1
    col-=1
    dir-=1
    a[row][col].append(i)
    direction.append(dir)
    where.append((row,col))

def finish():
    for i in range(n):
        for j in range(n):
            if len(a[i][j])>=4:
                return True
    return False

def inside(y,x):
    return 0<=y<n and 0<=x<n

def changedir(d):
    if d==0 :return 1
    if d==1 :return 0
    if d==2 : return 3
    if d==3 : return 2

def isBottom(w):
    r,c = where[w]
    if a[r][c][0] == w:return True
    return False

Success = False
cnt = 0
while True:
    if cnt>=1000:break
    if finish():
        Success = True
        break
    cnt += 1
    for who in range(k):
        if isBottom(who):
            y,x = where[who]
            d = direction[who]
            ny,nx = y + dy[d],x+dx[d]
            if not inside(ny,nx) or mapcolor[ny][nx]==2:
                direction[who] = changedir(d)
                nd = direction[who]
                ny,nx = y+dy[nd],x + dx[nd]
                if not inside(ny,nx) or mapcolor[ny][nx]==2:
                    direction[who] = d
                    continue
            if mapcolor[ny][nx]==0:
                temp = a[y][x]
                for inner_who in temp:
                    where[inner_who] = (ny,nx)
                a[ny][nx] += temp
                a[y][x].clear()
            if mapcolor[ny][nx]==1:
                temp = a[y][x]
                for inner_who in temp:
                    where[inner_who] = (ny,nx)
                temp.reverse()
                a[ny][nx] += temp
                a[y][x].clear()
if Success:
    print(cnt)
else:print(-1)