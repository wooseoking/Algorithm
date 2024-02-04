t = int(input())

for _ in range(t):
    n = int(input())
    s1 = list(input())
    s2 = list(input())

    tmp = [0]*2

    for c1,c2 in zip(s1,s2):
        if c1 != c2 and c1 == '0':
            tmp[0]+=1
        elif c1 != c2 and c1 == '1':
            tmp[1] += 1

    print(max(tmp))