import heapq
import math

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    d = [[math.inf]*10001 for _ in range(n+1)]
    for _ in range(k):
        u,v,c,t_ = map(int,input().split())
        # 출발 -> (도착,비용,시간)
        graph[u].append((v,c,t_))
    d[1][0] = 0
    for cost in range(m+1):
        for now in range(1,n+1):
            if d[now][cost]==math.inf:continue

            for next,next_c,next_t in graph[now]:
                if cost+next_c > m:continue
                next_time = d[now][cost] + next_t
                if next_time < d[next][cost+next_c]:
                    d[next][cost+next_c] = next_time
    ans = min(d[n])
    print(ans if ans!=math.inf else "Poor KCM")