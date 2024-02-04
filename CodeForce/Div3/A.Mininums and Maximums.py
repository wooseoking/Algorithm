import sys
input = sys.stdin.readline
#print = sys.stdout.write
tc = int(input())
for _ in range(tc):
    l1,r1,l2,r2 = map(int,input().split())

    if r1 == l2:print(r1)
    elif r1 < l2:print(l1+l2)
    elif l1 <= l2 < r1 <=r2:print(l2)
    elif r2 < l1:print(l2+l1)
    elif r2 == l1:print(r2)
    elif l2<=l1 < r2<=r1:print(l1)