import sys
import math
input = sys.stdin.readline
k,n = map(int,input().split())
arr =[]
for _ in range(k):
    arr.append(int(input()))

left = 1
right = pow(2,31)-1
ans = 0

while left<=right:
    cut = (left+right)//2
    temp = 0
    for ele in arr:
        temp += ele//cut
    if temp >= n:
        ans = cut
        left = cut+1
    else:
        right = cut-1

print(ans)