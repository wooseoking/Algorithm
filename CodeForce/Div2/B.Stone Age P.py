import sys
n,q =map(int,input().split())
a = list(map(int,input().split()))
SUM = sum(a)

for _ in range(q):
    tmp = list(map(int,sys.stdin.readline().split()))
    if tmp[0] == 1:
        idx,num = tmp[1],tmp[2]
        idx-=1
        SUM-=a[idx]
        SUM+=num
        a[idx] = num
        print(SUM)
    else:
        SUM = tmp[1]*n
        print(SUM)
