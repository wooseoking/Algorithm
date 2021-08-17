import heapq

n = int(input())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
start,end = map(int,input().split())
q = []
INF = 10**9
dist = [INF]*(n+1)
dist[start] = 0
heapq.heappush(q,(0,start))
while q:
    cost,now = heapq.heappop(q)
    if dist[now] < cost:continue

    for next_c , next in graph[now]:
        next_cost = cost + next_c
        if next_cost < dist[next]:
            dist[next] = next_cost
            heapq.heappush(q,(next_cost,next))
print(dist[end])