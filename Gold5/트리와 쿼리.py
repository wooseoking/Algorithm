import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def maketree(current,parent):
    if visited[current]:return
    visited[current] = True
    for next_ in graph[current]:
        if next_==parent:continue
        child[current].append(next_)
        maketree(next_,current)

def Count(cur):
    size[cur] = 1
    for c in child[cur]:
        Count(c)
        size[cur]+=size[c]

n,r,q = map(int,input().split())
graph = [[]for _ in range(n+1)]
child = [[]for _ in range(n+1)]
parent =[-1]*(n+1)
visited = [False]*(n+1)
size = [0]*(n+1)
query = []
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for _ in range(q):
    query.append(int(input()))
maketree(r,-1)
Count(r)
for q in query:
    print(size[q])