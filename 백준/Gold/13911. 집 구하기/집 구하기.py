# input
import heapq
import math

n,m = map(int,input().split())
g = [[] for _ in range(n + 3)]
home = [True]*(n + 1)

for _ in range(m):
    x,y,c = map(int,input().split())
    g[x].append([y,c])
    g[y].append([x,c])

mn,x = map(int,input().split())
mcdonalds = list(map(int,input().split()))
sn,y = map(int,input().split())
starbucks = list(map(int,input().split()))

# 맥도날드, 스타벅스를 하나의 정점으로 대표집합으로 표현하기 ( 대표정점에서 각 집합 정점까지 cost = 0 으로 가상점 만들기)
#  n + 1 : 맥도날드 대표정점
#  n + 2 : 스타벅스 대표정점

for mcdonald in mcdonalds:
    home[mcdonald] = False
    g[n+1].append([mcdonald,0])
for starbuck in starbucks:
    home[starbuck] = False
    g[n+2].append([starbuck,0])

# 맥도날드 , 스타벅스에서 각각 다익스트라

def dijkstra(start):
    d = [math.inf]*(n + 3)
    d[start] = 0
    q = []
    heapq.heappush(q,[0,start])

    while q:
        cost,cur = heapq.heappop(q)

        if d[cur] < cost: continue

        for nextNode,edgeCost in g[cur]:
            nextCost = cost + edgeCost
            if nextCost < d[nextNode]:
                d[nextNode] = nextCost
                heapq.heappush(q,[nextCost,nextNode])
    return d

mcDijkstra = dijkstra(n + 1)
starbuckDijikstra = dijkstra(n + 2)

res = []
for i in range(1,n+1):
    if not home[i]:continue

    if mcDijkstra[i] <= x and starbuckDijikstra[i] <= y:
        res.append(mcDijkstra[i] + starbuckDijikstra[i])

print(min(res) if res else -1)

