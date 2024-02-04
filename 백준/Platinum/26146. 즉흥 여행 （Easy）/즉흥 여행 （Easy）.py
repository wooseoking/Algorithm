import sys
sys.setrecursionlimit(10 ** 7)

n,m = map(int,input().split())

graph = [[] for _ in range(n + 1)]
rgraph = [[] for _ in range(n + 1)]
stack = []
visited = [False] * (n + 1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    rgraph[y].append(x)

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]:continue
        dfs(y)
    stack.append(x)

def rdfs(x,scc):
    visited[x] = True
    scc.append(x)

    for y in rgraph[x]:
        if visited[y]:continue
        rdfs(y,scc)

# 1. 정방향 dfs
for node in range(1, n + 1):
    if visited[node]:continue
    dfs(node)

# 2. visit 초기화 + 역방향 dfs + scc 구하기
SCC = []
visited = [False]* (n + 1)

while stack:
    top = stack.pop()
    if visited[top]:continue
    scc = []
    rdfs(top,scc)
    SCC.append(scc)
print('Yes' if len(SCC) == 1 else 'No')