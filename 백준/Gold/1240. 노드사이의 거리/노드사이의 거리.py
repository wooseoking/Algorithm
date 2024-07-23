n,m =map(int,input().split())
g = [[] for _ in range(n + 1)]
pairs = []
for _ in range(n - 1):
    x,y,c = map(int,input().split())
    g[x].append([y,c])
    g[y].append([x,c])

for _ in range(m):
    x,y = map(int,input().split())
    pairs.append([x,y])

def getDistance(n1,n2):
    d = 0
    q = []
    visited = [False]* (n + 1)
    visited[n1] = True
    q.append([n1,d])

    while q:
        cur,curDistance = q.pop(0)
        if cur == n2: return curDistance
        for nextNode,nextDistance in g[cur]:
            if visited[nextNode]:continue
            nd = curDistance + nextDistance
            visited[nextNode] = True
            q.append([nextNode,nd])

    return -1


for n1,n2 in pairs:
    ans = getDistance(n1,n2)
    print(ans)