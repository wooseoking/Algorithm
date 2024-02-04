tc = int(input())
dy = [-1,-1,1,1]
dx = [-1,1,-1,1]

def inside(y,x):
    return 0<=y< n and 0<=x<m

def getSum(y,x,a):
    ret = a[y][x]

    for k in range(4):
        ny,nx = y,x
        while True:
            ny+=dy[k]
            nx+=dx[k]
            if not inside(ny,nx):break
            ret+=a[ny][nx]
    return ret

for _ in range(tc):
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    res = []
    for y in range(n):
        for x in range(m):
            res.append(getSum(y,x,a))
    print(max(res))