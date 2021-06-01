import sys
sys.setrecursionlimit(10000000)
n = int(input())
a = [[]for _ in range(n+1)]
for _ in range(n-1):
    v1,v2,cost = map(int,input().split())
    a[v1].append((cost,v2))
    a[v2].append((cost,v1))

d = [-1]*(n+1)

def dfs(now,cur_cost):
    d[now] = cur_cost
    for cost_,next_ in a[now]:
        if d[next_]!=-1:continue
        next_cost = cost_ + cur_cost
        d[next_] = next_cost
        dfs(next_,next_cost)

dfs(1,0)
max_node = d.index(max(d))
d = [-1]*(n+1)
dfs(max_node,0)
ans = max(d)
print(ans)