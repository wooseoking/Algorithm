import math

n,m = map(int,input().split())
edges = []
dist = [math.inf]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur,next_,cost = edges[j][0],edges[j][1],edges[j][2]
            if dist[cur]!=math.inf and dist[cur] + cost < dist[next_]:
                dist[next_] = dist[cur] + cost
                if i==n-1:return True
    return False
negativecycle = bf(1)
if negativecycle:print(-1)
else:
    for node in range(2,n+1):
        print(dist[node] if dist[node]!=math.inf else -1)