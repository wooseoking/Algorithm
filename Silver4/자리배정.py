m,n = map(int,input().split())
sy , sx = n-1,0
a = [[-1]*m for _ in range(n)]
end = int(input())
#    위 오른 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]
cnt = 0
def inside(y,x):
    return 0<=y<n and 0<=x<m

def go(y,x):
    global cnt
    if not inside(y,x):return
    if a[y][x]!=-1:return
    cnt+=1
    a[y][x] = cnt

    for k in range(4):
        while True:
            y+=dy[k]
            x+=dx[k]
            if not inside(y,x):break
            if a[y][x]!=-1:break
            cnt+=1
            a[y][x] = cnt
        y-=dy[k]
        x-=dx[k]
    go(y-1,x)


go(sy,sx)
ay,ax = -1,-1
for i in range(n):
    for j in range(m):
        if a[i][j]==end:
            ay,ax = i,j
if ax!=-1 or ay!=-1:
    print(ax+1,n-ay)
else:print(0)