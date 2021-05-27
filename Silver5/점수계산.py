import sys
input = sys.stdin.readline

a = []
for i in range(8):
    temp = int(input())
    a.append((temp,i+1))

a.sort(reverse=True)
ans = []
SUM = 0
for i in range(5):
    SUM +=a[i][0]
    ans.append(a[i][1])

ans.sort()
print(SUM)
for ele in ans:
    print(ele,end=' ')