import heapq,math

def dijikstra(n,graph,gates,summits):
    vsummits = [False]*(n + 1)
    q = []
    intensity = [math.inf]*(n + 1)

    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(q,[0,gate])

    for summit in summits:
        vsummits[summit] = True

    while q:
        cost, cur = heapq.heappop(q)

        if vsummits[cur]:continue
        if intensity[cur] < cost : continue

        for nextNode,nextCost in graph[cur]:
            nextCost = max(intensity[cur],nextCost)
            if nextCost < intensity[nextNode]:
                intensity[nextNode] = nextCost
                heapq.heappush(q,[nextCost,nextNode])

    return intensity
def solution(n, paths, gates, summits):
    g = [[] for _ in range(n + 1)]

    for x,y,c in paths:
        g[x].append([y,c])
        g[y].append([x,c])

    intensity = dijikstra(n,g,gates,summits)
    res = []
    for summit in summits:
        res.append([summit,intensity[summit]])
    res.sort(key= lambda x:(x[1],x[0]))
    answer = res[0]
    return answer
