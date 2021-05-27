import sys
input = sys.stdin.readline

n = 10000000
six = "666"
ans = []

for i in range(666,n):
    temp = str(i)
    if six in temp:
        ans.append(temp)

idx = int(input())
print(ans[idx-1])

