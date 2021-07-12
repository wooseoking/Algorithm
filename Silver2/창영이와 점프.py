n,k = map(int,input().split())
a = list(map(int,input().split()))
result = []

def dfs(index,cnt):
    global jump

    if index==n-1:
        result.append(cnt)
        return
    if jump:
        if a[index]>k:
            result.append(cnt)
            return
        else:
            dfs(index+1,cnt+1)
    else:
        if a[index]>k:
            jump = True
            dfs(index+1,cnt+1)
            jump = False
        else:
            dfs(index+1,cnt+1)
for i in range(n-1):
    jump = False
    dfs(i,1)
print(max(result))