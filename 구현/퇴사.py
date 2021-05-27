import sys
input=  sys.stdin.readline
n = int(input())
t = [0]*(n+2)
p = [0] *(n+2)
d = [0]*(n+2)

for i in range(1,n+1):
    x,y = map(int,input().split())
    t[i] = x
    p[i] = y

M = 0
for i in range(1,n+1):
    M = max(M,d[i])
    if i + t[i] <=n+1:
        d[i+t[i]] = max(M + p[i],d[i+t[i]])
print(max(d))