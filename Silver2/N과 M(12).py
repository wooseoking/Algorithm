import itertools

n,m = map(int,input().split())
a = list(map(int,input().split()))
result = []
a = list(set(a))
a.sort()

for s in itertools.combinations_with_replacement(a,m):
    success = True
    for v1,v2 in zip(s,s[1:]):
        if v1>v2:
            success = False
            break
    if success:
        result.append(s)

for s in result:
    for v in s:
        print(v,end=' ')
    print()
