import sys
sys.setrecursionlimit(10**9)
N,e,w,s,n = map(int,input().split())
e /=100
w /=100
s /=100
n /=100
ans = 0
maxN = 100
ans = 0
a = [[False]*maxN for _ in range(maxN)]
# 동 북 서 남
dy = [0,-1,0,1]
dx = [1,0,-1,0]
a[maxN//2][maxN//2] = True
def Prob(p,dir):
    if dir == 0:
        p *= e
    elif dir == 1:
        p *= n
    elif dir == 2:
        p *= w
    elif dir == 3:
        p *= s
    return p

def BackTrack(y,x,size,p):
    global ans
    if size == N:
        ans+=p
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if a[ny][nx]:continue
        a[ny][nx] = True
        P = Prob(p,k)
        BackTrack(ny,nx,size+1,P)
        a[ny][nx] =False

    return

BackTrack(maxN//2,maxN//2,0,1)

print("%.9f" %ans)