import itertools

n = int(input())
population = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]

def travel(area):
    visited = [False]*(n+1)
    start = area[0]
    visited[start] = True
    q = [start]
    while q:
        now = q.pop(0)
        for next in graph[now]:
            if not visited[next] and next in area:
                visited[next] = True
                q.append(next)

    for node in range(1,n+1):
        if node in area and not visited[node]:return False
    return True

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    tmp = tmp[1:]
    graph[i] = tmp

area = [i for i in range(1,n+1)]
res = []
for r in range(1,n):

    for s in itertools.combinations(area,r):
        area1 = list(s)
        area2 = [i for i in range(1,n+1) if i not in area1]
        if travel(area1) and travel(area2):
            sum1 ,sum2 = 0,0
            for v in area1:sum1+=population[v]
            for v in area2:sum2+=population[v]
            res.append(abs(sum1-sum2))
if not res:print(-1)
else :print(min(res))