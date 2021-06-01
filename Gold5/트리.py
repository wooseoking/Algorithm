n = int(input())
INF = 100000000
parent = list(map(int,input().split()))
delete_node = int(input())
root = 0
out_degree = [0]*n
for i in range(n):
    if parent[i]==-1:continue
    from_ = parent[i]
    out_degree[from_]+=1
    if i == delete_node:
        out_degree[from_]-=1

for i in range(n):
    if parent[i]==-1:
        root = i
        break
parent[root] = root

def findParent(now):
    if now == delete_node:return False
    if now == root:return True
    y = findParent(parent[now])
    return y

leaf = 0
for i,v in enumerate(out_degree):
    if v == 0:
        if findParent(i):leaf+=1

print(leaf)