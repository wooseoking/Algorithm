A,B,C = map(int,input().split())
capacity = [A,B,C]
temp = [0,0,C]
Set = []
visited = [[[False]*201 for _ in range(201)] for _ in range(201)]
ans = []
def go(arr):
    a,b,c = arr[0],arr[1],arr[2]
    if visited[a][b][c] :return
    if a==0:ans.append(c)
    visited[a][b][c] = True

    for i in range(3):
        if arr[i]==0:continue
        for j in range(3):
            if i==j or arr[i]==0 and arr[j]==0:continue
            # i -> j
            cnt = 0
            while arr[i]!=0 and arr[j]!=capacity[j]:
                arr[i]-=1
                arr[j]+=1
                cnt+=1
            go(arr)
            arr[i]+=cnt
            arr[j]-=cnt


go(temp)
ans = set(ans)
ans = list(ans)
ans.sort()
for v in ans:
    print(v,end=' ')