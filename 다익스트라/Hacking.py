import heapq
import sys
input = sys.stdin.readline
INF = 1e9
t = int(input())

for _ in range(t):
    n ,m,start = map(int,input().split())
    q = []
    a = [[] for _ in range(n+1)]
    d = [INF]*(n+1)

    for _ in range(m):
        v2,v1,cost = map(int,input().split())
        a[v1].append((cost,v2))

    d[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        cost , now = heapq.heappop(q)
        if d[now] < cost : continue
        for next_c, next_ in a[now]:
            next_cost = next_c + cost
            if next_cost < d[next_]:
                d[next_] = next_cost
                heapq.heappush(q,(next_cost,next_))

    number = 0
    time = 0
    for i in range(1,n+1):
        if d[i]==INF:continue
        number+=1
        time = max(time,d[i])

    print(number,time)