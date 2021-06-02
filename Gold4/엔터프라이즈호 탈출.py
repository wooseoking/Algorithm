import heapq
import sys
input = sys.stdin.readline
INF = 1e9

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x,h_,w_):
    return 0<=y<h_ and 0<=x<w_

def go(arr,y,x):
    ans = INF
    height = len(arr)
    width =len(arr[0])
    d = [[INF]*width for _ in range(height)]
    d[y][x]=0
    q = []
    heapq.heappush(q,(0,y,x))
    breakpoint = False
    while q:
        cost,y,x = heapq.heappop(q)

        if d[y][x] < cost:continue
        for k_ in range(4):
            ny = y+dy[k_]
            nx = x+dx[k_]
            if not inside(ny,nx,height,width):
                breakpoint = True
                ans = cost
                break
            next_cost = cost + arr[ny][nx]
            if next_cost < d[ny][nx]:
                d[ny][nx] = next_cost
                heapq.heappush(q,(next_cost,ny,nx))
        if breakpoint:break
    return ans

t = int(input())
for _ in range(t):
    k,w,h = map(int,input().split())
    table = dict()
    table["E"] = 0
    sy=0
    sx=0
    for _ in range(k):
        what,cost = input().split()
        table[what] = int(cost)
    temp = [list(input().rstrip()) for _ in range(h)]
    a = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if temp[i][j]=="E":
                sy=i
                sx=j
            a[i][j] = table[temp[i][j]]
    d = go(a,sy,sx)
    print(d)
