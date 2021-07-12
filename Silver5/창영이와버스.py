n,m = map(int,input().split())
a = list(map(int,input().split()))
cost = [list(map(int,input().split()))for _ in range(n)]
ans = 0
for v1,v2 in zip(a,a[1:]):
    ans+=cost[v1-1][v2-1]
print(ans)