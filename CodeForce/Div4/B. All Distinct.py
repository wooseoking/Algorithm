tc = int(input())
for _ in range(tc):
    n = int(input())
    a_list = list(map(int,input().split()))
    a_set = set(a_list)
    table = dict()
    for e in a_list:
        if e not in table:
            table[e] = 1
        else:
            table[e]+=1

    if len(a_set) == len(a_list):print(n)
    else:
        get_sum = 0
        for val in table.values():
            get_sum+=val-1
        if get_sum %2 == 0:
            print(len(a_set))
        else:
            print(len(a_set)-1)