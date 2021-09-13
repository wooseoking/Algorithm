n = int(input())
a = list(map(int,input().split()))
limit = int(input())
left = 1
right = max(a)
ans = None
while left<=right:
    mid = (left+right)//2
    s = 0
    for v in a:
        if v <= mid:
            s+=v
        else:s+=mid
    if s<=limit:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)