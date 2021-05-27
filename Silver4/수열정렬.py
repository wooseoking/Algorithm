import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
temp = []
for i in range(n):
    temp.append((i,a[i]))
result = list(sorted(temp,key = lambda x : x[1]))
p = [0]*n
for i,v in enumerate(result):
    p[v[0]] = i

for v in p:
    print(v,end=' ')