n,m = map(int,input().split())
a = list(map(int,input().split()))

left = 0
right = 0
s = a[0]
ans = 0
while left <= right < n:
    if s<m:
        right+=1
        if right<n:
            s+=a[right]
    elif s==m:
        ans+=1
        right+=1
        if right<n:
            s+=a[right]
    elif s>m:
        s-=a[left]
        left+=1
        if right < left < n:
            right=left
            s = a[right]
print(ans)