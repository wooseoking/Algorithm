from collections import deque
n = int(input())
a = list(map(int,input().split()))
q = deque()
for i in range(n):
    q.append((a[i],i+1))

idx = 0
deleted = 0
del_a = [False]*n
ans = []
while True:
    deleted+=1
    del_a[idx] = True
    move,num = q[idx]
    print(num,end=' ')
    if deleted==n:break
    moved = 0
    if move > 0:
        while moved!=abs(move):
            idx+=1
            idx%=n
            if del_a[idx]:continue
            moved+=1
    else:
        while moved != abs(move):
            idx -= 1
            idx %= n
            if del_a[idx]: continue
            moved += 1
    idx %=n