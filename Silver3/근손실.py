import itertools
n,k = map(int,input().split())
plan = list(map(int,input().split()))
U = list(itertools.permutations(plan,len(plan)))
cnt = 0
for schedule in U:
    now = 500
    ok = True
    for v in schedule:
        now+=v
        now-=k
        if now < 500:
            ok = False
            break
    if ok:cnt+=1
print(cnt)