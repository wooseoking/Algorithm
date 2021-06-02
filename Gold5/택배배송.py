import heapq
n,m = map(int,input().split())
a = [[]for _ in range(n+1)]
d = [1e9]*(n+1)
for _ in range(m):
    v1,v2,cost = map(int,input().split())
    a[v1].append((cost,v2))
    a[v2].append((cost,v1))

q = []
heapq.heappush(q,(0,1))
d[1] = 0
while q:
    cur_cost,now = heapq.heappop(q)
    if d[now] < cur_cost:continue

    for next_c , next in a[now]:
        next_cost = cur_cost + next_c
        if next_cost < d[next]:
            d[next] = next_cost
            heapq.heappush(q,(next_cost,next))
print(d[n])