import sys
input = sys.stdin.readline
n = int(input())
c = [False]*(2000+1)
arr = map(int,input().split())
for ele in arr:
    c[ele+1000] = True

for i in range(len(c)):
    if c[i]:
        print(i-1000,end=' ')