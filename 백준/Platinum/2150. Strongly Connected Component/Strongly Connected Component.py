import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n,m= map(int,input().split())

stack = []
id_ = 0
scc = []
finished = [False for _ in range(n+1)]
d = [0]*(n+1)

def dfs(x):
    global id_,finished,d,stack
    id_+=1
    d[x] = id_
    stack.append(x)
    parent = d[x]
    for y in a[x]:
        if d[y]==0:
            parent = min(parent,dfs(y))
        elif not finished[y]:
            parent = min(parent,d[y])

    if parent == d[x]:
        SCC = []
        while True:
            top = stack[-1]
            stack.pop()
            SCC.append(top)
            finished[top] = True
            if top==x:
                break
        scc.append(SCC)
    return parent

a = [[]for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    a[v1].append(v2)

Par = [0]*(n+1)
for i in range(1,n+1):
    if d[i]==0: dfs(i)
print(len(scc))
for i in range(len(scc)):
    scc[i].sort()
scc.sort()
for row in scc:
    row.append(-1)
    print(*row,sep=' ')