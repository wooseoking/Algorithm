t = int(input())
for _ in range(t):
    n = int(input())
    sets = set()
    a =[]
    res = []
    for _ in range(n):
        thing,kind = input().split()
        a.append(kind)
        sets.add(kind)
    for v in sets:
        res.append(a.count(v))
    ans = 1
    for v in res:
        ans*=v+1

    print(ans-1)