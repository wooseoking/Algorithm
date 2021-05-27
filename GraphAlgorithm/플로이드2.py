import sys
input=sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
d = [[INF]*(n+1) for _ in range(n+1)]
v= [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):d[i][i] = 0
for _ in range(m):
    v1,v2,cost = map(int,input().split())
    d[v1][v2] = min(cost,d[v1][v2])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]
                v[i][j] = k
for i in range(1,n+1):
    for j in range(1,n+1):
        if d[i][j]==INF:print(0,end=' ')
        else:print(d[i][j],end=' ')
    print()

def Path(from_,to_):
    global pathes
    if v[from_][to_]==INF:
        return

    mid = v[from_][to_]
    pathes.append(mid)
    Path(from_,mid)
    Path(mid,to_)


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(0)
        else :
            pathes = []
            Path(i,j)
            pathes.insert(0,i)
            pathes.insert(len(pathes),j)
            print(len(pathes), end=' ')
            for k in range(len(pathes)):
                print(pathes[k],end=' ')
            print()
