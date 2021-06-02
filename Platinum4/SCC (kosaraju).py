import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x):
    global id,a,d,finished,stack,SCC,group
    id+=1
    d[x] = id
    parent = d[x]
    stack.append(x)

    for y in a[x]:
        if d[y]==0: parent = min(parent,dfs(y))
        elif not finished[y]: parent = min(parent,d[y])

    if parent ==d[x]:
        scc = []
        while True:
            top = stack.pop()
            finished[top] = True
            scc.append(top)
            group[top] = len(SCC)+1
            if x == top: break
        SCC.append(scc)
    return parent

def go(x):
    global visited,a,group,indegree
    if visited[x] : return
    visited[x] = True
    for y in a[x]:
        if group[x]!=group[y]:
            indegree[group[y]]+=1
        go(y)


n,m = map(int,input().split())
a = [[]for _ in range(n+1)]
d = [0]*(n+1)
finished = [False]*(n+1)
stack = []
id = 0
SCC = []
group = [0]*(n+1)
for _ in range(m):
    v1,v2 = map(int,input().split())
    a[v1].append(v2)
for i in range(1,n+1):
    if d[i]==0:dfs(i)
max_g = max(group)
indegree = [0]*(max_g+1)
visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        go(i)
ans = indegree[1:].count(0)
print(ans)