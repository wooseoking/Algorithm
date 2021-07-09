n = int(input())
a = list(map(int,input().split()))
ans = 1
for length in range(1,n+1):
    for i in range(n-length+1):
        sublist = a[i:i+length]
        if abs(min(sublist)-max(sublist))<=2 and length>ans:
            ans = length
print(ans)