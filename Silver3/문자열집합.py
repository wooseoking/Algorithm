import sys
input = sys.stdin.readline
S = set()
n,m = map(int,input().split())
ans =0
for _ in range(n):
    S.add(input().strip())
for _ in range(m):
    temp = input().strip()
    if temp in S:ans+=1
print(ans)