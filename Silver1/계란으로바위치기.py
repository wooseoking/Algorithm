import sys
sys.setrecursionlimit(100000000)
n = int(input())
val = [0]*n
weight = [0]*n
for i in range(n):
    a,b = map(int,input().split())
    val[i] = a
    weight[i] = b
ans = 0

def go(idx,v,w,cnt):
    global ans
    if idx==n:
        ans = max(ans, cnt)
        return
    ans = max(ans, cnt)
    if v[idx] > 0:
        for next_idx in range(n):
            if next_idx == idx or v[next_idx]<=0 or v[idx]<=0:continue
            v[idx] -= w[next_idx]
            v[next_idx] -=w[idx]
            broken = 0
            if v[idx]<=0:broken+=1
            if v[next_idx]<=0 :broken+=1
            go(idx+1,v,w,cnt+broken)
            v[idx] += w[next_idx]
            v[next_idx] += w[idx]
    else:
        go(idx+1,v,w,cnt)


go(0,val,weight,0)
print(ans)