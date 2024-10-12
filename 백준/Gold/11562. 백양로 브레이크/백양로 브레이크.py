import math,heapq
n,m = map(int,input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u,v,b = map(int,input().split())
    if b == 0:
        g[u].append([v,0])
        g[v].append([u,1])
    else:
        g[u].append([v,0])
        g[v].append([u,0])

def dijikstra(graph,start,end):
    d = [math.inf]*(n + 1)
    d[start] = 0
    q = []
    heapq.heappush(q,[0,start])

    while q:
        cost , cur = heapq.heappop(q)

        if d[cur] < cost:continue

        for nextNode, edgeCost in graph[cur]:
            nextCost = cost + edgeCost
            if nextCost < d[nextNode]:
                d[nextNode] = nextCost
                heapq.heappush(q,[nextCost,nextNode])


    return d[end]

def floid(graph):
    d = [[math.inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][i] = 0

    for u in range(1, n + 1):
        for v,edgeCost in graph[u]:
            d[u][v] = edgeCost

    for k in range(1,n + 1):
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                d[i][j] = min(d[i][j] , d[i][k] + d[k][j])
    
    return d

k = int(input())
d = floid(g)
for _ in range(k):
    start,end = map(int,input().split())
    print(d[start][end])