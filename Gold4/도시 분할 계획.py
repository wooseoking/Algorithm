def getParent(x):
    if parent[x] == x:return x
    parent[x] = getParent(parent[x])
    return parent[x]

def union(x,y):
    x = getParent(x)
    y = getParent(y)

    if x==y:return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x]==rank[y]:rank[x]+=1

n,m = map(int,input().split())
nodes = []
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    nodes.append((a,b,c))
nodes.sort(key=lambda x : x[2])


res_cost = []
for v1,v2,cost in nodes:
    p1,p2 = getParent(v1),getParent(v2)
    if p1!=p2:
        res_cost.append(cost)
        union(v1,v2)
maximum_cost = max(res_cost)
ans = sum(res_cost) - maximum_cost
print(ans)