n,t = map(int,input().split())
a = [(-1,-1,-1)]
d = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    s,x,y = map(int,input().split())
    a.append((s,x,y))

def manhattan(i,j):
    xi,yi = a[i][1],a[i][2]
    xj,yj = a[j][1],a[j][2]
    return abs(xi-xj)+abs(yi-yj)

for i in range(1,n+1):
    for j in range(1,n+1):
        d[j][i] = d[i][j] = manhattan(i,j)


def near(u):
    where = -1
    distance = 1e9
    for v in range(1,n+1):
        if a[v][0]==0:continue
        if manhattan(u,v) < distance:
            distance = manhattan(u,v)
            where = v
    return where

def getDistance(u,v):
    ans = d[u][v]
    if a[u][0]==1 and a[v][0]==1:
        ans = min(ans,t)

    u_next = near(u)
    v_next = near(v)
    if u_next!=-1 and v_next!=-1 and a[u_next][0]==1 and a[v_next][0]==1:
            ans = min(d[u][u_next] + t + d[v_next][v],ans)
    return ans


m = int(input())
for _ in range(m):
    u,v = map(int,input().split())
    print(min(getDistance(u,v),d[u][v]))