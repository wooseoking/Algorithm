n = int(input())
q = []
q.append((n,0))
v = [False]*(10**6+1)
parent = [i for i in range(10**6+1)]
v[n] = True
while q:
    now,cnt = q.pop(0)
    if now==1:break

    if now%3==0:
        if not v[now//3]:
            v[now//3] = True
            parent[now//3] = now
            q.append((now//3,cnt+1))
    if now%2==0:
        if not v[now//2]:
            parent[now//2] = now
            v[now//2] = True
            q.append((now//2,cnt+1))
    if not v[now-1]:
        v[now-1] = True
        parent[now-1] = now
        q.append((now-1,cnt+1))
ans = []
def getParent(cur):
    if cur==n:
        ans.append(cur)
        return
    ans.append(cur)
    getParent(parent[cur])
getParent(1)
ans.reverse()
print(len(ans)-1)
for v in ans:
    print(v,end=' ')
