import sys
input = sys.stdin.readline
INF = -1e9
n = int(input())
a = list(map(int,input().split()))
#증가
ans1 = INF
pos = 0
change = 0
for k in range(n-1):
    if a[k] > a[k+1]:
        change+=1
        if change ==1 : pos = k

if change==1 or change==0:
    if change==0 : ans1 = 0
    else :
        if a[-1] <= a[0]:
            ans1 = pos+1
#감소
ans2 = INF
pos2 = 0
change2 = 0
for k in range(n-1):
    if a[k] < a[k+1]:
        change2+=1
        if change2==1:pos2 = k

if change2==0 or change2==1:
    if change2==0:ans2 = 0
    else:
        if a[-1] >= a[0]:
            ans2 = pos2 +1

if ans1==INF and ans2==INF:
    print(-1)
else:
    if ans1 !=INF and ans2!=INF:print(min(ans1,ans2))
    elif ans1 ==INF and ans2!=INF:print(ans2)
    elif ans1 !=INF and ans2==INF:print(ans1)