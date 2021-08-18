n = int(input())
a = list(map(int,input().split()))
if n==1:
    print(1)
    exit(0)
d1 = [1]*n
d2 = [1]*n
for i in range(1,n):
    if a[i] >= a[i-1]:
        d1[i] = d1[i-1]+1
for i in range(1,n):
    if a[i] <= a[i-1]:
        d2[i] = d2[i-1] + 1
print(max(max(d1),max(d2)))