import sys
from queue import PriorityQueue
input = sys.stdin.readline

n ,m = map(int,input().split())
a = list(map(int,input().split()))
b= list(map(int,input().split()))

ans = []

for ele in a:
    ans.append(ele)
for ele in b:
    ans.append(ele)
ans.sort()
for ele in ans:
    print(ele,end = ' ')