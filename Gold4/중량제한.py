n,m = map(int,input().split())
a = [[]for _ in range(n+1)]
for _ in range(m):
    v1,v2,cost = map(int,input().split())
    a[v1].append((v2,cost))
    a[v2].append((v1,cost))

start,end = map(int,input().split())
def search(value):
    q = []
    q.append(start)
    v = [False]*(n+1)
    v[start] = True
    while q:
        now = q.pop()
        if now == end:return True
        for next_,c in a[now]:
            if not v[next_] and value<=c:
                v[next_]= True
                q.append(next_)
    return False

low = 1
high = 10**9
ans = 0
result = []
while low<=high:
    mid = (low+high)//2

    if search(mid):
        result.append(mid)
        low = mid+1
    else:
        high = mid-1
print(max(result))