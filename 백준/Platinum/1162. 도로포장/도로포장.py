import heapq
import math

# input
n,m,k = map(int,input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    x,y,z = map(int,input().split())
    g[x].append([y,z])
    g[y].append([x,z])

# dijkstra
d = [[math.inf]* (k + 1) for _ in range(n + 1)]
start = 1
d[start][0] = 0

q = []
heapq.heappush(q,[0,start,0])

while q:
    cost,cur,cnt = heapq.heappop(q)

    if d[cur][cnt] < cost : continue

    for nextNode,edgeCost in g[cur]:
        nextCost = cost + edgeCost
        if nextCost < d[nextNode][cnt]:
            d[nextNode][cnt] = nextCost
            heapq.heappush(q,[nextCost,nextNode,cnt])

        if cnt < k and cost < d[nextNode][cnt + 1]:
            d[nextNode][cnt + 1] = cost
            heapq.heappush(q,[cost,nextNode,cnt + 1])

ans = min(d[n])
print(ans)