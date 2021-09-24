n,c = map(int,input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
left = 0
right = a[-1] - a[0]
ans = -1
while left<=right:
    x = (left+right)//2
    cnt = 1
    cur = 0
    for i in range(1,n):
        if a[i] - a[cur] >= x:
            cnt+=1
            cur = i
    if cnt >=c:
        ans = x
        left = x+1
    else:
        right = x-1
print(ans)

