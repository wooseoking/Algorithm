import math

A,B = map(str,input().split())
ans = math.inf
for i in range(len(B)-len(A)+1):
    cnt = 0
    for v1,v2 in zip(B[i:i+len(A)],A):
        if v1!=v2:cnt+=1
    ans = min(ans,cnt)
print(ans)