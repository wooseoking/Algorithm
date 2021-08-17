import copy

n = int(input())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
visited[1] = True
candidate = []
for friend in graph[1]:
    visited[friend] = True
    candidate.append(friend)
q = copy.deepcopy(candidate)
while q:
    now = q.pop()

    for nfriend in graph[now]:
        if not visited[nfriend]:
            visited[nfriend] = True
            candidate.append(nfriend)
print(len(candidate))