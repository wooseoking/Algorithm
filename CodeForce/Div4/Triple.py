tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    table = dict()
    success = False
    for e in a:
        if e not in table:
            table[e] = 1
        else:
            table[e]+=1
            if table[e]>=3:
                print(e)
                success = True
                break
    if not success:
        print(-1)
