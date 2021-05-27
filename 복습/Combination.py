import sys
input = sys.stdin.readline

d = [[0]*31 for _ in range(31)]
d[0][0] = 1


for i in range(1,31):
    for r in range(0,i+1):
        if r==0 or r==i:
            d[i][r] = 1
        else:
            d[i][r] = d[i-1][r-1] + d[i-1][r]

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(d[m][n])