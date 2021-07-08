n,m = map(int,input().split())
a = [[0]*m for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().strip()))
    a[i] = tmp
k = int(input())
