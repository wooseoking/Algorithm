def inside(y,x):
    return 0<=y<n and 0<=x<n
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n = int(input())
a = [list(map(int,input().split()))for _ in range(n)]
def go(value):
    q = []
    q.append((0,0))
    visited = [[False]*n for _ in range(n)]
    while q:
        y,x = q.pop()
        if y==n-1 and x==n-1:return True

        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if not inside(ny,nx):continue
            if visited[ny][nx]:continue
            if abs(a[y][x]-a[ny][nx]) <=value:
                visited[ny][nx] = True
                q.append((ny,nx))
    return False

low = 0
high = 10**9
ans = 0

while low<=high:
    mid = (low+high)//2
    if go(mid):
        ans = mid
        high = mid-1
    else:
        low = mid+1
print(ans)