import copy

tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(input())
    p = list(map(int,input().split()))
    cnt = 0
    original_a = copy.deepcopy(a)

    while True:
        cnt+=1
        newa = ['']*n
        for e in p:

            newa.append(a[e-1])
        a = newa
        if a == original_a:break
    print(cnt)