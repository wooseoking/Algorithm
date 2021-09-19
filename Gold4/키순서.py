n,m = map(int,input().split())
adj = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a-1][b-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] + adj[k][j] == 2:
                adj[i][j] = 1
ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if adj[i][j]==1:cnt+=1
    for k in range(n):
        if adj[k][i]==1:cnt+=1
    if cnt == n-1:ans+=1
print(ans)