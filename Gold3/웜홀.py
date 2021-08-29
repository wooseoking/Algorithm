import math

t = int(input())
def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur,next,cost = edges[j][0],edges[j][1],edges[j][2]
            if dist[cur] + cost < dist[next]:
                dist[next] = dist[cur] + cost
                if i==n-1:return True
    return False

for _ in range(t):
    n,m,w = map(int,input().split())
    edges = []
    dist = [1e9]*(n+1)
    for _ in range(m):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))
    Flag = bf(n)
    print(Flag)