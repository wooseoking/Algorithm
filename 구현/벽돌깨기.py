import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
ans = -1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<h and 0<=x<w

def go(a,cnt,broken,N):
    global ans
    if cnt == N:
        ans = max(ans,broken)
        return
    for i in range(w):
        y = 0
        x = i
        while True:
            if a[y][x] !=0 or not inside(y,x):break
            y+=1
        if not inside(y,x):continue
        ret = simulation(a,y,x)
        go(a,cnt+1,broken+ret,N)
    return

def simulation(a,y,x,v):
    if v[y][x]:return
    v[y][x] = True
    a[y][x] = 0
    for k in range(4):
        ny = y
        nx = x
        for _ in range(a[y][x]-1):
            ny+=dy[k]
            nx+=dx[k]
            if not inside(ny,nx):continue
            simulation(a,ny,nx,v)
    ret = 1
    for i in range(len(v)):
        for x in v[i]:
            if x:ret+=1

    return ret

t = int(input().rstrip())
for testcase in range(1,t+1):
    n,w,h = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(h)]
    visit = [[False]*h for _ in range(w)]
    ans = -1
    print(simulation(board,2,2,visit))
    print("#"+str(testcase)+ " " + str(ans))