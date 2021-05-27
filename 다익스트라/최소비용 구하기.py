import sys
import heapq
INF = 1e9
input = sys.stdin.readline

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]

for _ in range(m):
    v1,v2,cost = map(int,input().split())
    a[v1].append((cost,v2))

start,end = map(int,input().split())

q=[]
d = [INF] * (n+1)
d[start] = 0
heapq.heappush(q,(0,start))

while q:
    cost,now = heapq.heappop(q)
    if d[now] < cost:continue

    for next_c,next_ in a[now]:
        next_cost = cost+next_c
        if next_cost < d[next_]:
            d[next_] = next_cost
            heapq.heappush(q,(next_cost,next_))
print(d[end])