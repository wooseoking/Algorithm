import sys
sys.setrecursionlimit(10**8)
import heapq
import math

n,x,y = map(int,input().split())
graph = [[] for _ in range(n + 1)]
parents = [i for i in range(n + 1)]
finished = False
table = [dict() for _ in range(n + 1)]

for _ in range(n - 1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    table[a][b] = c
    table[b][a] = c
    if (a == x and b == y) or (a == y and b == x):
        finished = True

if finished:
    print(0)
    exit(0)

def dijkstra(start,graph):
    d = [math.inf] * (n + 1)
    d[start] = 0
    q = []
    heapq.heappush(q,[0,start])

    while q:
        cost,cur = heapq.heappop(q)
        if d[cur] < cost:continue

        for nextNode,edgeCost in graph[cur]:
            nextCost = d[cur] + edgeCost

            if nextCost < d[nextNode]:
                d[nextNode] = nextCost
                parents[nextNode] = cur
                heapq.heappush(q,[nextCost,nextNode])

    return d




d = dijkstra(x,graph)
totalCost = d[y]

maxEdge = 0
visited = [False]*(n + 1)
def getPaths(cur):
    global maxEdge
    if cur == x:return

    visited[cur] = True
    parent = parents[cur]
    maxEdge = max(maxEdge,table[cur][parent])
    getPaths(parent)

getPaths(y)

answer = totalCost - maxEdge
print(answer)