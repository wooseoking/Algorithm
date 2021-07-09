import bisect

n = int(input())
a = list(map(int,input().split()))
rev_a = list(reversed(a))
arranged1 =[]
arranged2 = []
d1 = [0]*n
d2 = [0]*n
for i in range(n):
    if not arranged1 or arranged1[-1] < a[i]:
        arranged1.append(a[i])
    idx = bisect.bisect_left(arranged1,a[i])
    arranged1[idx] = a[i]
    d1[i] = idx+1

for i in range(n):
    if not arranged2 or arranged2[-1] < rev_a[i]:
        arranged2.append(rev_a[i])
    idx = bisect.bisect_left(arranged2,rev_a[i])
    arranged2[idx] = rev_a[i]
    d2[i] = idx+1
d2.reverse()
ans = 1
for v1,v2 in zip(d1,d2):
    ans = max(ans,v1+v2-1)
print(ans)