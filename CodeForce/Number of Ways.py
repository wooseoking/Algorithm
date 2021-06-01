import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int,input().split()))
d = [0]*(n+1)

for i in range(1,n+1):
    d[i] = d[i-1] + a[i]
Total = d[n]
if Total % 3 != 0:
    print(0)
    exit(0)

target_num = Total//3
inner_cnt = 0
ans = 0
if d[1] == target_num : inner_cnt = 1
for i in range(2,n):
    if d[i]==target_num*2: ans +=inner_cnt
    if d[i]==target_num: inner_cnt+=1
print(ans)