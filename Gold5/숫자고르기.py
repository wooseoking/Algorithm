n = int(input())
graph = [0]*(n+1)
ans = set()
for i in range(1,n+1):
    graph[i] = int(input())

def dfs(now,depth,v):
    if v[now] and depth>=2:
        ans.add(now)
        return
    v[now] = True
    dfs(graph[now],depth+1,v)

for i in range(1,n+1):
    v = [False]*(n+1)
    dfs(i,0,v)
ans = list(ans)
ans.sort()
print(len(ans))
for ele in ans:
    print(ele)