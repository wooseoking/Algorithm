n,m = map(int,input().split())
query = list(map(int,input().split()))
arr = [i for i in range(1,n+1)]
ans = 0
for v in query:
    front = arr.index(v)
    back = len(arr)-front
    if front<back:
        ans+=front
        arr = arr[front:] + arr[:front]
        arr.pop(0)
    else:
        ans+=back
        arr = arr[-back:] + arr[:-back]
        arr.pop(0)

print(ans)