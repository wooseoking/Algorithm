import sys
input = sys.stdin.readline
n = int(input())
a =[0]*501
for _ in range(n):
    i,v = map(int,input().split())
    a[i] = v
d = [0]*501
for i in range(1,501):
    if a[i]!=0:
        d[i] =1
        for j in range(1,i):
            if a[j] < a[i]:
                if d[j]+1 > d[i]:
                    d[i] = d[j]+1
    else:
        d[i]=-1
print(n - max(d))