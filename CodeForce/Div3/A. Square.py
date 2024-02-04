import itertools

t = int(input())
for _ in range(t):
    a = []
    for _ in range(4):
        x,y = map(int,input().split())
        a.append([x,y])

    for s in itertools.combinations(a,2):
        x1,y1 = s[0]
        x2,y2 = s[1]

        if x1 != x2 and y1 != y2:
            print(abs(x1-x2) * abs(y1 - y2))
            break