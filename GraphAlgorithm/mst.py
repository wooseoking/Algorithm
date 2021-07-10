N = 100
parent = [i for i in range(N)]
Rank = [0 for i in range(N)]

def findParent(x):
    global parent, Rank
    if parent[x]==x:return x
    parent[x] = findParent(parent[x])
    return parent[x]

def Union(x,y):
    global parent,Rank
    x = findParent(x)
    y = findParent(y)
    print(x,y)
    if x==y:return

    if Rank[x]<Rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if Rank[x]==Rank[y]:Rank[x]+=1

def solution(n, costs):
    answer = 0
    edges = []
    for n1,n2,cost in costs:
        edges.append((n1,n2,cost))
    edges.sort(key=lambda l:l[2])

    for n1,n2,c in edges:
        print(n1,n2,c)
        if findParent(n1)!=findParent(n2):
            Union(n1,n2)
            answer+=c

    return answer