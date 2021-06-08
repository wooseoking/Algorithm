n,m,h = map(int,input().split())
d = [[False]*(n+1) for _ in range(h+1)]
INF = 10**9
for _ in range(m):
    a,b = map(int,input().split())
    d[a][b] = True

ans = INF
def dfs(y,cnt,selected):
    global ans
    if cnt==selected:
        for start in range(1,n+1):
            now = start
            for i in range(1,h+1):
                if d[i][now]:
                    now+=1
                    continue
                elif d[i][now-1]:
                    now-=1
            if now!=start:
                return
        print(cnt)
        exit(0)
        return
    for i in range(y,h+1):
        for j in range(1,n):
            if d[i][j] or d[i][j-1] or d[i][j+1]:continue
            d[i][j]= True
            dfs(i,cnt+1,selected)
            d[i][j] = False
    return

for k in range(4):
    dfs(0,0,k)
print(-1)