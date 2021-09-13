import math
from collections import deque
n,k = map(int,input().split())
q = deque()
table = dict()
q.append((n,0))
cnt = 0
minsec = math.inf
while q:
    now,level = q.popleft()
    table[now] = True
    if now == k and level<=minsec:
        minsec = level
        cnt+=1
    n1,n2,n3 = now-1,now+1,now*2
    lists = [n1,n2,n3]
    for v in lists:
        if not v in table and 0<=v<=100000:
            q.append((v,level+1))
print(minsec)
print(cnt)