import sys
sys.setrecursionlimit(1000000000)
n = int(input())
T = int(input())
broken = []
if T!=0:
    broken =list(map(int,input().split()))

if T==10 or T==0:
    if T==10 :print(abs(n-100))
    elif T==0:
        a1 = len(str(n))
        a2 = abs(n-100)
        print(min(a1,a2))
    exit(0)
res = []

for s in range(1000000):
    ok = True
    for v in str(s):
        if int(v) in broken:
            ok = False
    if ok:res.append(s)

temp = abs(res[0]-n)
idx = 0
for i ,v in enumerate(res):
    if abs(v-n) < temp:
        temp = abs(v-n)
        idx = i
ans1 = abs(n-100)
res.sort(key=lambda x : abs(x-n) + len(str(x)))
ans2= len(str(res[0])) + abs(res[0]-n)
print(min(ans1,ans2))