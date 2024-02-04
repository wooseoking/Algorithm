import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse= True)
a.insert(0,0)
prefix_a = [0]*(n+1)

for i in range(1,n+1):
    prefix_a[i] += prefix_a[i-1] + a[i]

for _ in range(m):
    x,y = map(int,input().split())
    ans = prefix_a[x] - prefix_a[x-y]
    sys.stdout.write(str(ans) + '\n')