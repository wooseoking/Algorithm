import sys
from queue import PriorityQueue
import heapq

input = sys.stdin.readline
INF = 1e9

n,m = map(int,input().split())
start = int(input())

a = [[] for _ in range(n+1)]
d= [INF]*(n+1)

for _ in range(m):
    v1,v2,cost = map(int,input().split())
    a[v1].append((cost,v2))

d[start] = 0
q= []
heapq.heappush(q,(0,start))
while q:
    cost,now = heapq.heappop(q)

    if d[now] < cost:continue

    for n_c,next in a[now]:
        next_cost = cost + n_c
        if next_cost < d[next]:
            d[next] = next_cost
            heapq.heappush(q,(next_cost,next))

for i in range(1,n+1):
    if d[i]==INF:print("INF")
    else :print(d[i])