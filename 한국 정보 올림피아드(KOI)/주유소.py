n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))
ans = 0
cur = cost[0]
for i in range(n-1):
    if cost[i]>=cur:
        ans+=cur*dist[i]
    else:
        cur = cost[i]
        ans+=cur*dist[i]
print(ans)