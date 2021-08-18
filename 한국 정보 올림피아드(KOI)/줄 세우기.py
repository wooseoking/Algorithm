n = int(input())
a = list(map(int,input().split()))
result = [1]
for i in range(1,n):
    bef = a[i]
    result.insert(bef,i+1)
for i in range(n-1,-1,-1):
    print(result[i],end=' ')