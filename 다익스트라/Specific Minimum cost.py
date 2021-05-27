import sys
import heapq
input = sys.stdin.readline
INF = 1e9
n,m = map(int,input().split())
a = [[] for _ in range(n+1)]
S = [INF]*(n+1)
X1 = [INF]*(n+1)
X2 = [INF]*(n+1)

for _ in range(m):
    v1,v2,cost = map(int,input().split())
    a[v1].append((cost,v2))
    a[v2].append((cost,v1))
x1,x2 = map(int,input().split())

def dijikstra(start,Dist):
    Dist[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost_ , now_ = heapq.heappop(q)
        if Dist[now_] < cost_:continue

        for next_c ,next_ in a[now_]:
            next_cost = next_c +cost_
            if next_cost <Dist[next_]:
                Dist[next_] = next_cost
                heapq.heappush(q,(next_cost,next_))

dijikstra(1,S)
dijikstra(x1,X1)
dijikstra(x2,X2)

root1 = S[x1] + X1[x2] + X2[n]
root2 = S[x2] + X2[x1] + X1[n]

ans = min(root1,root2)
if ans>=1e9:print(-1)
else: print(ans)