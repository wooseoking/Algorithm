from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

n,q = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(2**n)]
query = list(map(int,input().split()))

def printboard():
    for rs in a:
        print(*rs,sep=' ')

def rotate(y, x, length_):
    tmpa = [rows[x:x + length_] for rows in a[y:y + length_]]
    rotate_tmpa = [[0] * length_ for _ in range(length_)]
    for i in range(length_):
        for j in range(length_):
            rotate_tmpa[i][j] = tmpa[length_ - j - 1][i]
    for i in range(length_):
        for j in range(length_):
            a[y+i][x+j] = rotate_tmpa[i][j]

def inside(y,x):
    return 0<=y<2**n and 0<=x<2**n

def go():
    brokeice = [[False]*2**n for _ in range(2**n)]

    for i in range(2**n):
        for j in range(2**n):
            if a[i][j]==0:continue
            cnt = 0
            for k in range(4):
                ny,nx = i+dy[k],j+dx[k]
                if not inside(ny,nx) or a[ny][nx]==0:cnt+=1

            if cnt>=2:
                brokeice[i][j] = True

    for i in range(2**n):
        for j in range(2**n):
            if brokeice[i][j]:
                a[i][j]-=1

def getsum():
    s = 0
    for i in range(2**n):
        for j in range(2**n):
            if a[i][j]==0:continue
            s+=a[i][j]
    return s

for c in query:
    length = 2**c

    for i in range(0,2**n,length):
        for j in range(0,2**n,length):
            rotate(i,j,length)

    go()

d = [[False]*2**n for _ in range(2**n)]
ans = 0

for i in range(2**n):
    for j in range(2**n):
        if not d[i][j] and a[i][j]>0:
            q = deque()
            q.append((i,j))
            d[i][j] = True
            cnt = 1
            while q:
                y,x = q.popleft()
                print(y,x)
                for k in range(4):
                    ny,nx = y+dy[k],x+dx[k]
                    if inside(ny,nx) and a[ny][nx]>0 and d[ny][nx]==-1:
                        d[ny][nx] = True
                        q.append((ny,nx))
                        cnt+=1

            ans = max(ans,cnt)


print(getsum())
print(ans)