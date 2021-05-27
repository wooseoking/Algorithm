import sys
from itertools import permutations
input = sys.stdin.readline

a = list(input())

a.pop(-1)


for i in range(len(a)):
    a[i] = int(a[i])
a.sort(reverse=True)
Sum = sum(a)
if Sum%3==0 and a[-1] ==0:
    for ele in a:
        print(ele,end='')
else:
    print(-1)