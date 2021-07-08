import itertools

n,r = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
Set = set()
for s in itertools.combinations(a,r):
    if s not in Set:
        for v in s:
            print(v, end=' ')
        print()
        Set.add(s)